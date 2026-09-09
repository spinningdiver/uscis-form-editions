"""版本变化时发邮件通知。

用法：
    python notify.py          读取 data/changes.md，有变化才发
    python notify.py --test   发一封样例邮件，用来验证配置是否正确

发信密码从环境变量 GMAIL_APP_PASSWORD 读取（GitHub Actions 里是仓库 Secret）。
没配置密码时静默跳过，不让整个任务失败 —— 网页和 Issue 通知不受影响。
"""

import json
import os
import smtplib
import sys
from datetime import datetime
from email.message import EmailMessage
from email.utils import formataddr
from pathlib import Path

import yaml

import build

ROOT = Path(__file__).parent
SMTP_HOST, SMTP_PORT = "smtp.gmail.com", 587

# 邮件客户端普遍会剥掉 <style> 标签，所以样式必须逐个内联
TD = "padding:9px 12px;border-bottom:1px solid #e4e8ec;font-size:14px;color:#1a2129"
TH = (
    "padding:8px 12px;border-bottom:2px solid #d5dbe1;font-size:11px;"
    "letter-spacing:.08em;text-transform:uppercase;color:#66727e;text-align:left"
)
MONO = "font-family:'SF Mono',Consolas,Menlo,monospace"


def load_changes() -> list[dict]:
    """从 history.json 取最近一次的变更（run.py 刚写进去的那条）。"""
    path = ROOT / "data" / "history.json"
    if not path.exists():
        return []
    history = json.loads(path.read_text(encoding="utf-8"))
    if not history:
        return []
    today = datetime.now(build.EASTERN).strftime("%Y-%m-%d")
    latest = history[0]
    return latest["changes"] if latest["date"] == today else []


def build_html(changes: list[dict], site_url: str) -> str:
    rows = "".join(
        f"<tr>"
        f'<td style="{TD};{MONO};font-weight:600;white-space:nowrap">'
        f'<a href="{c["url"]}" style="color:#17557f;text-decoration:none">{c["id"]}</a></td>'
        f'<td style="{TD}">{c["cn"]}</td>'
        f'<td style="{TD};{MONO};color:#8a929b;text-decoration:line-through">{c["from"]}</td>'
        f'<td style="{TD};{MONO};font-weight:700;color:#9e3527">{c["to"]}</td>'
        f'<td style="{TD};{MONO};color:#66727e">{", ".join(c["also"]) or "—"}</td>'
        f"</tr>"
        for c in changes
    )

    return f"""<div style="background:#f1f3f6;padding:28px 16px;font-family:-apple-system,'Segoe UI','Microsoft YaHei',sans-serif">
<div style="max-width:640px;margin:0 auto;background:#fff;border:1px solid #dce2e8;border-radius:8px;overflow:hidden">
  <div style="padding:20px 22px 16px;border-bottom:1px solid #eaeef2">
    <div style="{MONO};font-size:11px;letter-spacing:.12em;text-transform:uppercase;color:#66727e;margin-bottom:6px">USCIS Form Edition Tracker</div>
    <div style="font-size:19px;font-weight:600;color:#131a21">{len(changes)} 个表格版本有更新</div>
  </div>
  <table style="width:100%;border-collapse:collapse">
    <tr><th style="{TH}">表格</th><th style="{TH}">名称</th><th style="{TH}">原版本</th><th style="{TH}">新版本</th><th style="{TH}">也接受</th></tr>
    {rows}
  </table>
  <div style="padding:18px 22px;background:#f7f9fb;border-top:1px solid #eaeef2">
    <a href="{site_url}" style="display:inline-block;padding:9px 18px;background:#17557f;color:#fff;
       text-decoration:none;border-radius:6px;font-size:14px;font-weight:500">查看完整版本速查表</a>
    <div style="margin-top:14px;font-size:12px;color:#66727e;line-height:1.7">
      日期格式 mm/dd/yy · 以 <a href="https://www.uscis.gov/forms/all-forms" style="color:#17557f">USCIS 官网</a> 为准，本邮件仅供内部参考
    </div>
  </div>
</div></div>"""


def build_text(changes: list[dict], site_url: str) -> str:
    lines = [f"{len(changes)} 个表格版本有更新：", ""]
    lines += [f"  {c['id']:<8} {c['from']} -> {c['to']}   {c['cn']}" for c in changes]
    lines += ["", f"完整列表：{site_url}"]
    return "\n".join(lines)


def main() -> int:
    password = os.environ.get("GMAIL_APP_PASSWORD", "").strip()
    if not password:
        print("未配置 GMAIL_APP_PASSWORD，跳过邮件通知。")
        return 0

    cfg = yaml.safe_load((ROOT / "mail.yaml").read_text(encoding="utf-8")) or {}
    sender, recipients = cfg.get("from"), cfg.get("to") or []
    if not sender or not recipients:
        print("mail.yaml 缺少 from 或 to，跳过邮件通知。")
        return 0

    test = "--test" in sys.argv
    changes = (
        [{"id": "I-000", "cn": "配置测试邮件（非真实变更）", "from": "01/01/20",
          "to": "01/01/26", "also": [], "url": "https://www.uscis.gov/forms/all-forms"}]
        if test
        else load_changes()
    )
    if not changes:
        print("无版本变化，不发邮件。")
        return 0

    site_url = "https://spinningdiver.github.io/uscis-form-editions/"
    subject = (
        "[测试] USCIS 表格版本追踪 · 邮件配置正常"
        if test
        else (
            f"USCIS 表格版本更新：{changes[0]['id']} {changes[0]['from']} → {changes[0]['to']}"
            if len(changes) == 1
            else f"USCIS 表格版本更新：{len(changes)} 个表格（{', '.join(c['id'] for c in changes)}）"
        )
    )

    msg = EmailMessage()
    msg["Subject"] = subject
    msg["From"] = formataddr(("USCIS 表格版本追踪", sender))
    msg["To"] = ", ".join(recipients)
    msg.set_content(build_text(changes, site_url))
    msg.add_alternative(build_html(changes, site_url), subtype="html")

    try:
        with smtplib.SMTP(SMTP_HOST, SMTP_PORT, timeout=30) as smtp:
            smtp.starttls()
            smtp.login(sender, password)
            smtp.send_message(msg)
    except smtplib.SMTPAuthenticationError:
        print("!! Gmail 拒绝登录。请确认 GMAIL_APP_PASSWORD 是「应用专用密码」而非账号密码。")
        return 1
    except Exception as exc:
        print(f"!! 邮件发送失败：{type(exc).__name__}: {exc}")
        return 1

    print(f"已发送邮件至 {', '.join(recipients)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
