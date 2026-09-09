"""抓取 USCIS 各表格页面的 Edition Date。

页面结构（2026-09 实测，15/15 表格一致）：
    <div class="accordion__header">Edition Date</div>
    <div class="accordion__panel"> <div class="first last"><p>版本日期与说明</p></div> ... </div>

panel 里除了真正的版本说明，还跟着一段所有表格都一样的通用提示
（"You can find the edition date at the bottom of the page..."），
只取第一个 div.first.last 就能拿到干净的那一句。
"""

import re
import time

import requests
from bs4 import BeautifulSoup

BASE = "https://www.uscis.gov/"
UA = (
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 "
    "(KHTML, like Gecko) Chrome/128.0 Safari/537.36"
)
DATE_RE = re.compile(r"\d{2}/\d{2}/\d{2}\b")
DELAY = 2.0  # 每个请求之间的间隔，礼貌抓取


def _clean(text: str) -> str:
    """压缩空白，并修掉 USCIS 页面里的花括号引号。"""
    text = text.replace("’", "'").replace("“", '"').replace("”", '"')
    # 版本日期后面跟着一个独立的句点 span，去掉中间多余的空格
    text = re.sub(r"\s+", " ", text).strip()
    return re.sub(r"\s+([.,;:])", r"\1", text)


def fetch_form(slug: str, session: requests.Session) -> dict:
    """抓取单个表格，返回一条原始记录。失败时 status 非 ok，绝不抛异常。"""
    url = BASE + slug
    rec = {"id": slug.upper(), "url": url, "title": "", "raw": "", "dates": []}

    try:
        resp = session.get(url, headers={"User-Agent": UA}, timeout=30)
        resp.raise_for_status()
        # USCIS 不总是在响应头里声明字符集，不显式指定会把撇号解成乱码
        resp.encoding = "utf-8"
        soup = BeautifulSoup(resp.text, "html.parser")

        h1 = soup.find("h1")
        if h1:
            # "I-485, Application to Register..." → 去掉前面重复的表格号
            rec["title"] = re.sub(r"^[A-Z]-?\d+[A-Z]*,\s*", "", h1.get_text(" ", strip=True))

        header = next(
            (
                d
                for d in soup.select("div.accordion__header")
                if d.get_text(strip=True).lower() == "edition date"
            ),
            None,
        )
        if header is None:
            rec["status"] = "no_section"
            return rec

        panel = header.find_next_sibling("div", class_="accordion__panel")
        block = panel.select_one("div.first.last") if panel else None
        # 取不到精确块时退回整个 panel，宁可多抓通用提示也不要丢信息
        rec["raw"] = _clean((block or panel).get_text(" ", strip=True))[:1200]
        rec["dates"] = DATE_RE.findall(rec["raw"])
        rec["status"] = "ok" if rec["dates"] else "no_date"

    except Exception as exc:  # 单个表格失败不应中断整轮抓取
        rec["status"] = "error"
        rec["error"] = f"{type(exc).__name__}: {exc}"[:200]

    return rec


def fetch_all(slugs: list[str], verbose: bool = True) -> list[dict]:
    """串行抓取全部表格。"""
    session = requests.Session()
    out = []
    for i, slug in enumerate(slugs):
        rec = fetch_form(slug, session)
        out.append(rec)
        if verbose:
            mark = "OK " if rec["status"] == "ok" else "!! "
            print(f"  {mark}{rec['id']:<8} {rec['status']:<10} {','.join(rec['dates'])}")
        if i < len(slugs) - 1:
            time.sleep(DELAY)
    return out
