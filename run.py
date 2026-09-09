"""一次完整的检查：抓取 → 比对 → 生成网页 → 存档。

本地运行：   python run.py
CI 运行：     python run.py --ci     （检测到变化时额外写出 data/changes.md 供开 Issue 用）
"""

import sys
from datetime import datetime
from pathlib import Path

import yaml

import build
from scraper import fetch_all

ROOT = Path(__file__).parent

# Windows 控制台默认 GBK，会把中文输出成乱码
try:
    sys.stdout.reconfigure(encoding="utf-8")
except (AttributeError, OSError):
    pass


def write_changes_md(changes: list[dict], path: Path) -> None:
    """CI 用它作为 Issue 的标题与正文。第一行是标题。"""
    if len(changes) == 1:
        c = changes[0]
        title = f"{c['id']} 版本更新：{c['from']} → {c['to']}"
    else:
        title = f"{len(changes)} 个表格版本更新（{', '.join(c['id'] for c in changes)}）"

    lines = [title, "", "| 表格 | 名称 | 原版本 | 新版本 | 也接受 |", "|---|---|---|---|---|"]
    for c in changes:
        also = ", ".join(c["also"]) or "—"
        lines.append(f"| [{c['id']}]({c['url']}) | {c['cn']} | `{c['from']}` | **`{c['to']}`** | {also} |")
    lines += ["", "网页已自动更新。请核对官网原文后，视情况在 `notes.yaml` 中补充中文要点。"]

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

    failed = [f for f in forms if f["status"] != "ok"]
    print()
    print(f"完成：{len(forms) - len(failed)}/{len(forms)} 抓取成功")

    if failed:
        print(f"\n!! {len(failed)} 个表格抓取失败（网页沿用上一轮数据）：")
        for f in failed:
            print(f"   {f['id']:<8} {f['status']}  {f.get('error', '')}")

    if changes:
        print(f"\n>> 发现 {len(changes)} 处版本变化：")
        for c in changes:
            print(f"   {c['id']:<8} {c['from']} → {c['to']}   {c['cn']}")
        if ci:
            write_changes_md(changes, build.DATA / "changes.md")
    else:
        print("\n无版本变化。")

    # 全部失败通常意味着网络或页面结构变了，用非零退出码让 CI 亮红
    return 1 if len(failed) == len(forms) else 0


if __name__ == "__main__":
    raise SystemExit(main())
