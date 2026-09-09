"""一次完整的检查：抓取 → 比对 → 生成网页 → 存档。

本地运行：   python run.py
CI 运行：     python run.py --ci     （检测到变化时额外写出 data/changes.md 供开 Issue 用）
"""

import json
import sys
from datetime import datetime
from pathlib import Path

import yaml

import build
from scraper import TRUNCATED, fetch_all

ROOT = Path(__file__).parent

# Windows 控制台默认 GBK，会把中文输出成乱码
try:
    sys.stdout.reconfigure(encoding="utf-8")
except (AttributeError, OSError):
    pass


SITE_URL = "https://spinningdiver.github.io/uscis-form-editions/"


def staff_notice(changes: list[dict]) -> list[str]:
    """给员工的通知文案，可直接复制转发。

    放在 Issue 正文的代码块里 —— GitHub 的代码块自带复制按钮，
    点一下就能整段拷走，不用手工框选。
    """
    effective = [c for c in changes if c["kind"] == "edition"]
    announced = [c for c in changes if c["kind"] != "edition"]

    body = ["各位同事：", "", "USCIS 表格版本有以下变动，请留意：", ""]

    if effective:
        body.append("【已生效】即日起请使用新版本")
        for c in effective:
            body.append(f"  · {c['id']}　{c['cn']}")
            body.append(f"    最新版本：{c['to']}（原为 {c['from']}）")
            if c["also"]:
                body.append(f"    旧版 {'、'.join(c['also'])} 目前仍被接受")
            body.append(f"    官网：{c['url']}")
        body.append("")

    if announced:
        body.append("【新版预告】尚未生效，请提前准备")
        for c in announced:
            body.append(f"  · {c['id']}　{c['cn']}")
            body.append(f"    新版本：{c['to']}　目前仍使用：{c['from']}")
            body.append(f"    官网：{c['url']}")
        body.append("")

    body += [
        "提交前请核对表格底部的版本日期，并确保所有页面来自同一版本，",
        "否则可能被退件。以 USCIS 官网为准。",
        "",
        f"全部表格版本查询：{SITE_URL}",
    ]
    return body


def write_changes_md(changes: list[dict], path: Path) -> None:
    """CI 用它作为 Issue 的标题与正文。第一行是标题。"""
    if len(changes) == 1:
        c = changes[0]
        verb = "版本更新" if c["kind"] == "edition" else "公告新版"
        title = f"{c['id']} {verb}：{c['from']} → {c['to']}"
    else:
        title = f"{len(changes)} 个表格有版本变动（{', '.join(c['id'] for c in changes)}）"

    lines = [title, "", "| 表格 | 名称 | 类型 | 原/当前 | 新版本 | 也接受 |", "|---|---|---|---|---|---|"]
    for c in changes:
        also = ", ".join(c["also"]) or "—"
        kind = "已生效" if c["kind"] == "edition" else "预告"
        lines.append(
            f"| [{c['id']}]({c['url']}) | {c['cn']} | {kind} | `{c['from']}` | **`{c['to']}`** | {also} |"
        )

    lines += ["", "---", "", "### 转发给员工的通知（点右上角图标复制）", "", "```text"]
    lines += staff_notice(changes)
    lines += ["```", "", f"网页已自动更新：{SITE_URL}"]

    path.write_text("\n".join(lines), encoding="utf-8", newline="\n")


def main() -> int:
    ci = "--ci" in sys.argv
    now = datetime.now(build.EASTERN)

    slugs = yaml.safe_load((ROOT / "forms.yaml").read_text(encoding="utf-8"))
    print(f"检查 {len(slugs)} 个表格 …")
    records = fetch_all(slugs)

    forms = build.merge(records, build.load_notes())
    changes = build.diff(forms, build.load_previous(), now.strftime("%Y-%m-%d"))
    build.decorate(forms, now)
    build.render(forms, now.strftime("%Y-%m-%d %H:%M ET"))
    build.save(forms, changes, now)

    # 复核用：把未经筛选的全部公告导出，供每日人工/模型审阅
    if "--audit" in sys.argv:
        audit = [
            {"id": r["id"], "url": r["url"], "kept": r["alerts"], "all": r["alerts_all"]}
            for r in records
        ]
        (build.DATA / "audit-alerts.json").write_text(
            json.dumps(audit, ensure_ascii=False, indent=1), encoding="utf-8", newline="\n"
        )
        total = sum(len(a["all"]) for a in audit)
        kept = sum(len(a["kept"]) for a in audit)
        print(f"\n已导出复核文件：公告共 {total} 条，筛选保留 {kept} 条")

    failed = [f for f in forms if f["status"] != "ok"]
    print()
    print(f"完成：{len(forms) - len(failed)}/{len(forms)} 抓取成功")

    if failed:
        print(f"\n!! {len(failed)} 个表格抓取失败（网页沿用上一轮数据）：")
        for f in failed:
            print(f"   {f['id']:<8} {f['status']}  {f.get('error', '')}")

    # 上限留了数倍余量，真被截断说明官网内容大幅变长或页面结构变了，值得看一眼
    clipped = [f["id"] for f in forms if TRUNCATED in (f["raw"] + "".join(f["alerts"]))]
    if clipped:
        print(f"\n!! 以下表格的文本被截断，请检查是否需要调高 scraper.py 的上限：{', '.join(clipped)}")

    if changes:
        print(f"\n>> 发现 {len(changes)} 处版本变化：")
        for c in changes:
            kind = "已生效" if c["kind"] == "edition" else "预告  "
            print(f"   {c['id']:<8} {kind}  {c['from']} → {c['to']}   {c['cn']}")
        if ci:
            write_changes_md(changes, build.DATA / "changes.md")
    else:
        print("\n无版本变化。")

    # 全部失败通常意味着网络或页面结构变了，用非零退出码让 CI 亮红
    return 1 if len(failed) == len(forms) else 0


if __name__ == "__main__":
    raise SystemExit(main())
