"""把抓取结果加工成网页数据，并生成 docs/index.html。

职责分三段：
  merge()  —— 抓取记录 + notes.yaml 的人工解读 → 页面用的表格记录
  diff()   —— 与上一轮结果比对，标出变化
  render() —— 数据注入 docs/template.html
"""

import json
from datetime import datetime, timedelta, timezone
from pathlib import Path

import yaml

ROOT = Path(__file__).parent
DATA = ROOT / "data"
SITE = ROOT / "docs"
EASTERN = timezone(timedelta(hours=-4))  # 夏令时；仅用于显示

# 「有更新」标记保留多久
BADGE_DAYS = 30


def load_notes() -> dict:
    path = ROOT / "notes.yaml"
    return yaml.safe_load(path.read_text(encoding="utf-8")) or {} if path.exists() else {}


def load_previous() -> dict:
    """上一轮的结果，按表格号索引。首次运行时为空。"""
    path = DATA / "forms.json"
    if not path.exists():
        return {}
    prev = json.loads(path.read_text(encoding="utf-8"))
    return {f["id"]: f for f in prev.get("forms", [])}


def merge(records: list[dict], notes: dict) -> list[dict]:
    """抓取记录 + 人工解读 → 页面记录。"""
    forms = []
    for rec in records:
        note = notes.get(rec["id"]) or {}
        dates = rec.get("dates") or []
        cur = dates[0] if dates else ""
        # 当前版号常在原文里重复出现（如 I-693 的条件说明），去重后还要把它本身排除
        also = [d for d in dict.fromkeys(dates[1:]) if d != cur]
        forms.append(
            {
                "id": rec["id"],
                "cn": note.get("cn") or rec.get("title") or rec["id"],
                "en": rec.get("title", ""),
                "cur": cur,
                "also": also,
                "raw": rec.get("raw", ""),
                "note": (note.get("note") or "").strip(),
                "soon": bool(note.get("soon")),
                "status": rec.get("status", "error"),
                "error": rec.get("error", ""),
            }
        )
    return forms


def diff(forms: list[dict], previous: dict, today: str) -> list[dict]:
    """与上一轮比对，写入 changed / prev_cur / last_changed，并返回变更清单。"""
    changes = []
    for f in forms:
        old = previous.get(f["id"])

        # 抓取失败时沿用上一轮的数据，避免网页上凭空少一行
        if f["status"] != "ok":
            if old:
                f.update({k: old.get(k, f[k]) for k in ("cur", "also", "raw")})
                f["stale"] = True
            f["changed"] = False
            f["last_changed"] = (old or {}).get("last_changed", "")
            continue

        # 首次运行没有基准，一律不算「有更新」
        if old is None or not old.get("cur"):
            f["changed"] = False
            f["last_changed"] = ""
            continue

        moved = f["cur"] != old["cur"] or f["also"] != old.get("also", [])
        if moved:
            f["changed"] = True
            f["prev_cur"] = old["cur"]
            f["last_changed"] = today
            changes.append(
                {
                    "id": f["id"],
                    "cn": f["cn"],
                    "from": old["cur"],
                    "to": f["cur"],
                    "also": f["also"],
                    "url": f"https://www.uscis.gov/{f['id'].lower()}",
                }
            )
        else:
            f["changed"] = False
            f["last_changed"] = old.get("last_changed", "")
            if old.get("prev_cur"):
                f["prev_cur"] = old["prev_cur"]

    return changes


def decorate(forms: list[dict], today: datetime) -> None:
    """算出网页显示用的状态标记。"""
    for f in forms:
        fresh = False
        if f.get("last_changed"):
            try:
                changed_on = datetime.strptime(f["last_changed"], "%Y-%m-%d")
                fresh = (today - changed_on.replace(tzinfo=today.tzinfo)).days <= BADGE_DAYS
            except ValueError:
                fresh = False

        tags = []
        if fresh:
            tags.append("upd")
        if f["soon"]:
            tags.append("soon")
        if f["also"]:
            tags.append("multi")
        if not tags:
            tags.append("stable")

        f["tags"] = tags
        f["flag"] = "alert" if (fresh or f["soon"]) else ("warn" if f["also"] else "")


def render(forms: list[dict], checked_label: str) -> None:
    """把数据注入模板，写出 docs/index.html。"""
    template = (SITE / "template.html").read_text(encoding="utf-8")
    keys = ("id", "cn", "en", "cur", "also", "raw", "note", "flag", "tags")
    slim = [{k: f[k] for k in keys} for f in forms]

    html = template.replace(
        "{{FORMS_JSON}}", json.dumps(slim, ensure_ascii=False, indent=1)
    ).replace("{{CHECKED}}", checked_label)
    (SITE / "index.html").write_text(html, encoding="utf-8", newline="\n")


def save(forms: list[dict], changes: list[dict], now: datetime) -> None:
    DATA.mkdir(exist_ok=True)

    (DATA / "forms.json").write_text(
        json.dumps(
            {"generated_at": now.isoformat(timespec="seconds"), "forms": forms},
            ensure_ascii=False,
            indent=1,
        ),
        encoding="utf-8",
        newline="\n",
    )

    # 每天都写，即使无变化 —— 保证仓库天天有提交，
    # 否则 GitHub 会在 60 天无活动后自动停用定时工作流
    (DATA / "last_checked.json").write_text(
        json.dumps(
            {
                "checked_at": now.isoformat(timespec="seconds"),
                "forms_checked": len(forms),
                "ok": sum(1 for f in forms if f["status"] == "ok"),
                "changed": len(changes),
            },
            indent=1,
        ),
        encoding="utf-8",
        newline="\n",
    )

    if changes:
        history_path = DATA / "history.json"
        history = json.loads(history_path.read_text(encoding="utf-8")) if history_path.exists() else []
        history.insert(0, {"date": now.strftime("%Y-%m-%d"), "changes": changes})
        history_path.write_text(
            json.dumps(history, ensure_ascii=False, indent=1), encoding="utf-8", newline="\n"
        )
