# USCIS 页首公告的类型图谱

2026-09-09 对 `forms.yaml` 中 15 个表格做了一次全量通读，共 23 条公告。
2026-09-10 复核时 I-129 新增一条版本公告，现为 24 条。
2026-09-11 复核：表格扩到 26 个，公告 34 条（新增的 11 个表格带来 10 条）。
2026-09-12 复核：公告与前一日逐字相同，仍为 34 条；新记一个**面板措辞**的
边界情况（G-1145，见第三节）。
2026-09-15 复核：34 条公告自 09-11 起逐字节未变（09-13、09-14 两日无人复核，
一并核过）。新记一个**时间维度**的边界情况：A1 公告的强制换版日已到，
官网却尚未换版（I-765／I-539，见第三节）。
2026-09-16 复核：**前一日那个悬案有了答案** —— I-765／I-539 的换版被马萨诸塞州
联邦地区法院 9 月 14 日的禁令叫停，USCIS 明确「不接受 09/15/26 版」。
新增第六个版本类型 **A6**（第一节）、第十二个无关类型「提交地点变更」（第二节），
以及一个**跨表格日期串号**的边界情况（第三节）。公告 35 条。
2026-09-17 复核：35 条公告与前一日逐字节相同，无新类型。新记一个**人工覆盖被抓取
顶回来**的边界情况：`notes.yaml` 里的 `up: ""` 只在重新生成网页时生效，第二天的
抓取又会把「即将换版」标记加回来（见第三节）。
2026-09-18 复核：35 条公告自 09-16 起逐字节未变，无新类型。**时间维度那个边界情况
第二次出现**，这次是 I-485：09/18/26 版的强制换版日就是今天，官网却仍停在 09/04/26
（见第三节）。
2026-09-19 复核：**昨天那个悬案在一天之内兑现了** —— I-485 的 09/18/26 版已经发布，
面板更新为 09/18/26 且不再列旧版，原先那条将来时的 A1 预告被改写成已发布的措辞
（见第一节 A1 末尾）。公告仍为 35 条、命中仍为 8 条，无新类型。
2026-09-26 复核：35 条公告自 09-19 起逐字节未变（09-20 至 09-25 六天无人复核，
一并核过），命中仍为 8 条，无新类型，无过时的中文要点。
2026-09-27 复核：35 条公告自 09-19 起第八天逐字节未变，命中仍为 8 条，无新类型，
无过时的中文要点。I-864／I-864A 的 10 月 1 日是眼下最近的硬性切换日，还有 4 天。
2026-09-28 复核：35 条公告自 09-19 起第九天逐字节未变，命中仍为 8 条，无新类型，
无过时的中文要点。I-864／I-864A 的 10 月 1 日还有 3 天，**10 月 1 日那轮复核必须改写
这两条要点**。
2026-09-29 复核：35 条公告自 09-19 起第十天逐字节未变，命中仍为 8 条，无新类型，
无过时的中文要点。I-864／I-864A 的 10 月 1 日还有 2 天，9 月 30 日是旧版 10/17/24
可用的最后一天，**10 月 1 日那轮复核必须改写这两条要点**。
2026-09-30 复核：35 条公告自 09-19 起第十一天逐字节未变，命中仍为 8 条，无新类型，
无过时的中文要点。**今天就是 I-864／I-864A 旧版 10/17/24 可用的最后一天**，
两条要点今天仍然成立，明天（10 月 1 日）那轮复核必须改写。
2026-10-01 复核：**预定的改写已执行** —— I-864／I-864A 的宽限期昨天结束，
两条要点已改写为只接受 08/24/26 版。公告十二天来第一次有变动：I-765 与 I-589
各新增一条 FY2027 的 H.R.-1 费用通胀调整公告，公告数 35 → 37，命中仍为 8 条。
新增的是已记的「费用变动」类型，不是新类型，但它是「同样的措辞讲别的事」的第三例
（见第二节末）。另记 **A2 兑现时抓取侧零变化**这一观察（见第一节 A2 末尾）。
2026-10-02 复核：37 条公告与前一日逐字节相同（md5 仍是 `69e86c0f…`），命中仍为 8 条，
无新类型，无过时的中文要点。**昨天改写的 I-864／I-864A 两条要点经过切换日次日的复核仍然成立**，
面板 `cur` 仍是 08/24/26、`also` 仍为空，公告连 `will accept the 10/17/24 edition`
这个现在时都还留着 —— 第一节 A2 末尾那条观察又被印证一天。眼下最近的硬性切换日
是 I-129 的 11 月 9 日，还有 38 天。
2026-10-03 复核：37 条公告自 10-01 起第三天逐字节未变（md5 仍是 `69e86c0f…`），
命中仍为 8 条，无新类型，无过时的中文要点。按第四节第 1 点做的两条对账：
「切换日已过但 `cur` 未变」未命中；「切换日已过、公告措辞仍是现在时」第三天
仍命中 I-864／I-864A，公告原文一字未改，要点已在 10-01 改写到位，无需再动 ——
第一节 A2 末尾那条观察至此连续印证三天。最近的硬性切换日仍是 I-129 的
11 月 9 日，还有 37 天。
2026-10-04 复核：37 条公告自 10-01 起第四天逐字节未变（md5 仍是 `69e86c0f…`），
命中仍为 8 条，无新类型，无过时的中文要点。按第四节第 1 点做的两条对账：
「切换日已过但 `cur` 未变」未命中；「切换日已过、公告措辞仍是现在时」第四天
仍命中 I-864／I-864A，公告原文一字未改，要点已在 10-01 改写到位，无需再动 ——
第一节 A2 末尾那条观察至此连续印证四天。最近的硬性切换日仍是 I-129 的
11 月 9 日，还有 36 天。另记一个**与数据无关的操作陷阱**：本次会话克隆下来的
工作副本停在 09-30，10-01 至 10-03 三轮复核的提交要先 `git fetch` 才看得到，
**开始复核前应先 fetch 一次再判断「上次复核到哪天」**，否则会误以为中间几天
漏跑而重复改写已经改好的要点。
2026-10-05 复核：37 条公告自 10-01 起第五天逐字节未变（md5 仍是 `69e86c0f…`），
命中仍为 8 条，无新类型，无过时的中文要点。按第四节第 1 点做的两条对账：
「切换日已过但 `cur` 未变」未命中；「切换日已过、公告措辞仍是现在时」第五天
仍命中 I-864／I-864A，公告原文一字未改，要点已在 10-01 改写到位，无需再动 ——
第一节 A2 末尾那条观察至此连续印证五天。最近的硬性切换日仍是 I-129 的
11 月 9 日，还有 35 天。上一轮记下的 fetch 陷阱**今天第二次兑现**：本次会话克隆
下来的工作副本同样停在 09-30，落后 origin/main 八个提交，先 fetch 再判断
「上次复核到哪天」才避免了重复改写 I-864／I-864A 那两条已经改好的要点。
2026-10-06 复核：37 条公告自 10-01 起第六天逐字节未变（md5 仍是 `69e86c0f…`），
命中仍为 8 条，无新类型，无过时的中文要点。按第四节第 1 点做的两条对账：
「切换日已过但 `cur` 未变」未命中；「切换日已过、公告措辞仍是现在时」第六天
仍命中 I-864／I-864A，公告原文一字未改，要点已在 10-01 改写到位，无需再动 ——
第一节 A2 末尾那条观察至此连续印证六天。最近的硬性切换日仍是 I-129 的
11 月 9 日，还有 34 天。前两轮记下的 fetch 陷阱**这次没有出现**：本次会话克隆下来的
工作副本就停在 `main` 的最新提交（10-05 那条复核记录），无需追赶，
可见那个陷阱取决于克隆时机而非必然，**但判断「上次复核到哪天」之前仍应 fetch 一次**。
另记一个**抓取侧的观察**：10-05 当晚 22:58 那次 `schedule` 兜底触发（run 37385766056）
在「兜底触发时，若当天已抓过则跳过」这一步就跳过了后续全部步骤，11 秒结束、
`conclusion` 仍为 `success`。**这是设计行为不是失败**，但它意味着
`conclusion: success` 并不保证真的抓过 —— 判断某一轮有没有抓取要看耗时或 `last_checked.json`
的 `checked_at`，不能只看结论（本轮手动触发 run 37469860151 耗时 65 秒，26 个表格确实抓过）。
2026-10-07 复核：**公告六天来第一次有变动** —— I-485 与 I-130 各新增一条
「提交地点变更」公告（均写 10 月 7 日即当天改了收件地址），公告数 37 → 39，
命中仍为 8 条。新增的是已记的类型，不是新类型，但它是「同样的措辞讲别的事」的
**第四、第五例，且第一次撞上了另一张表真实的换版日**（见第二节末）。
I-130 自 09-11 纳入追踪以来**第一次有公告**（原先 `all` 为空）。
另记一个**比对方法上的陷阱**：I-485 页首两条公告的**先后顺序今天被官网换了**
（9 月 18 日那条移到了 9 月 4 日 Casa 禁令那条之前），文本逐字未改，
于是 `audit-alerts.json` 的 md5 变了而内容没变 —— **md5 有差异只是「要去 diff」的
信号，不等于内容有变动**（见第三节末）。

2026-10-08 复核：**昨天那条提交地点变更扩散成了一整波** —— 同一模板的公告今天又
新挂到 I-131、I-765、I-129、I-539、I-907、I-918、I-601、I-360 八张表上，
公告数 39 → 47，命中仍为 8 条。仍是已记的「提交地点变更」类型，八条均不含
`edition` 与 mm/dd/yy，规则正确挡在 `kept` 之外。I-907 与 I-601 由此
**第一次有公告**（原先 `all` 为空）。昨天那条「假阳性长得像真的」今天升级到最坏形态：
**这一波里有一条就挂在 I-129 自己页上**，于是同一张表的页首同时写着两个 11 月 9 日，
一个讲地址、一个讲换版（见第二节末）。
另记一类**新的边界情况**：USCIS 今天对三处公告做了纯文本润色，且每处只改了一部分
页面，可见**跨表格复用的公告会各自漂移** —— 历次复核记下的「两张表逐字相同」
不是稳定事实（见第三节末）。中文要点按今天的日期逐条核过，过时的一条都没有，`notes.yaml` 未改。

本文记录观察到的类型、当前筛选规则的依据，以及后续自动化的着手点。

数据来源：每个表格页面的 `div.messages__text` 节点，未经筛选的原文见仓库
历史中的抓取记录，或重新运行 `scraper.py` 获取。

---

## 为什么需要抓公告

`Edition Date` 面板只回答一个问题：**现在能用哪一版**。

它不回答：新版什么时候强制生效、旧版哪天开始被退件、有没有宽限期。
这些写在页首公告里。实测中有三个表格因此差点被漏掉：

| 表格 | 面板显示 | 公告里的实情 |
| --- | --- | --- |
| I-765 | 08/21/25 | 09/15/26 新版将强制生效，无宽限期 |
| I-539 | 08/28/24 | 09/15/26 新版将强制生效，无宽限期 |
| I-864 | 08/24/26 | 旧版 10/17/24 的宽限期 9/30 截止 |

三者的面板内容当时都尚未变动，只看面板等于什么都没发现。

---

## 一、与版本有关的公告（命中筛选，8/35 条）

### A1 新版预告 + 无宽限期 + 三段式切换规则

出现于 **I-765、I-539、I-485**。措辞高度模板化，三句话结构固定：

> On [日期], we will publish a revised edition of Form [X] (edition date: **MM/DD/YY**).
> … There is **no grace period** …
> Accept the [旧版] if postmarked or electronically submitted **before** [日期];
> Reject the [旧版] if postmarked or electronically submitted **on or after** [日期]; and
> Only accept the [新版] if postmarked or electronically submitted **on or after** [日期].

要点：以**邮戳或电子提交日**为准，不是收件日。切换是硬性的，没有缓冲。

**A1 兑现后会就地改写，不是新发一条**（2026-09-19 在 I-485 观察到）。
09/18/26 版发布后，页首那条 A1 的位置没变、条数没变，文本被换成了已发布的说法：

> On Sept. 18, 2026, USCIS **published** a revised edition of Form I-485 …
> There **is** no grace period for the revised edition … because this revision is
> necessary for USCIS to apply the final rule.
> Reject the [旧版] … on or after [日期]; and Only accept the [新版] … on or after [日期].

三处改动：`will publish` → `published`；`Because there will be no grace period,
USCIS is providing a preview version …` 整句换成不设宽限期的理由，预览版那句连同
`Before [日期], USCIS will only accept …` 一起删掉；末尾的 Accept/Reject 双句式保留不变。
与 A2／A4 的区别仍在**有没有并行期**：这里一天都没有，旧版当天即失效，
面板同步把「也接受的版本」清空。

**这说明 A1 的生命周期有两种结局**：兑现（就地改写成本形态，I-485）或被拦下
（整条被 A6 替换，I-765／I-539）。两者在抓取侧的表现完全不同 —— 前者 `cur` 变、
`also` 清空、`changed` 为 1，后者 `cur` 一动不动。

### A2 新版已发布 + 明确宽限期 + 旧版截止日

出现于 **I-864**，2026-09-11 在 **I-864A** 观察到同一模板（措辞逐句对应，
只换了表格号和"担保人／家庭成员"的称谓）：

> USCIS is providing a **30-day grace period** during which we will accept the [旧版].
> **Beginning [日期]**, we will only accept the [新版].

与 A1 的区别在于新版已生效、旧版尚在宽限期内，**两版并行且有明确终点**。
这类公告还常附带新版的实质性变化（I-864／I-864A 新版都含征信授权条款）。

I-864 与 I-864A 成对发布、日期完全一致（08/24/26 版，旧版 10/17/24 用到 9/30），
这是 USCIS 的惯例：**主表和它的附属合同表通常同步换版**。核对时两张一起看。

**A2 兑现时抓取侧零变化**（2026-10-01 在 I-864／I-864A 观察到）。
10 月 1 日这个硬性切换日到了，旧版 10/17/24 自此不再被接受，但：
公告原文**一字未改**（仍是 8 月 31 日那条，连 `will accept the 10/17/24 edition`
这个现在时都留着）、`cur` 本来就已经是 08/24/26、`also` 本来就是空的。
也就是说 `audit-alerts.json` 与 `forms.json` 在切换日前后**没有任何差异可比**，
`changed` 仍是 0。

**与 A1 兑现的对比很能说明问题**：A1（I-485）兑现时公告会就地改写、`cur` 会跳版、
`also` 会清空，抓取侧三处都动；A2 兑现时三处一处都不动。
原因在于 A2 的新版在发布那天就已经是 `cur` 了，切换日改变的只是**旧版还能不能用**，
而「旧版还能不能用」这件事只写在公告里，面板从头到尾没表达过。

**结论：A2 的到期只能靠日期去核，任何比对快照差异的检查都发现不了。**
这是第三节「时间维度」那条边界情况的**第三次出现，也是最隐蔽的一次** ——
前两次（I-765／I-539、I-485）至少还有「公告写的日期已过、`cur` 却没动」这个
可对账的矛盾，这次连矛盾都没有，因为 `cur` 本来就不该动。
这把第四节第 1 点那条对账检查的必要性又推高一层：它不能只报
「切换日已过但 `cur` 未变」，还得能报「切换日已过、公告措辞仍是现在时」，
后者才是 A2 到期的信号。

### A3 新版受法院禁令影响，暂缓实施

出现于 **I-485**：09/04/26 版因 *Casa Inc. v. Trump* 禁令，对该案认证集体成员
暂不实施。

**这类最危险**：版本号照常更新，但适用性存在例外。任何自动化都不应该
替使用者判断"该用哪版"，只能如实呈现原文。

### A4 新版已发布 + 两版并行，但公告里没有"宽限期"三个字（A2 的变体）

2026-09-10 在 **I-129** 首次观察到（09/09/26 版，配合 9-11 生物识别费终局规则发布）：

> Starting [日期], we will accept only the [新版] edition.
> **Until then**, you can also use the [旧版] edition.
> Accept the [旧版] … if postmarked or electronically submitted **before** [日期]; and
> Reject the [旧版] … if postmarked or electronically submitted **on or after** [日期].

实质与 A2 相同 —— 新版已生效、旧版尚可用、有硬性终点 —— 但两处不一样：

- **全文不含 `grace period`**，改用 `Until then` 表达并行期；
- 并行期不是 A2 那种固定 30 天，I-129 给了 61 天（09/09 → 11/09）。

后半段的 Accept/Reject 双句式又和 A1 一致。可见 USCIS 的模板并不统一，
**判断"有没有并行期"必须读日期，不能只认关键词**（见第四节的修订）。

这条同时说明：Edition Date 面板这次自己就写全了切换规则
（`Starting Nov. 9, 2026, we will accept only…`），公告与面板互为印证。
但不能因此就省掉公告 —— A1 那三个表格的面板当时什么都没写。

### A6 换版被法院叫停：预告公告被撤下，新版明确「不接受」

2026-09-16 在 **I-765、I-539** 首次观察到。这不是 A3 的重复，两者要分清：

| | A3（I-485） | A6（I-765／I-539） |
| --- | --- | --- |
| 新版是否发布 | 已发布，`cur` 已更新 | 从未发布，`cur` 仍是旧版 |
| 禁令的作用范围 | 只对认证集体成员暂缓 | 对所有人，整条规则暂缓生效 |
| 新版能不能用 | 能，除集体成员外 | **明确不接受** |
| 原公告 | 仍在，禁令是附加说明 | **被整条替换掉了** |

原文（两张表页首挂着同一条，逐字相同）：

> On Sept.14, 2026, the U.S. District Court for the District of Massachusetts issued
> an order **postponing the effective date** of the final rule … DHS is **preliminarily
> enjoined** … Until such time, USCIS will proceed under the previous regulatory
> provisions. Pursuant to the Sept. 14, 2026, order, USCIS **continues to accept** the
> 08/28/24 edition of Form I-539 and 08/21/25 edition of Form I-765 and **is not
> accepting** the 09/15/26 edition of Forms I-539 and I-765.

**最要紧的一点：A1 那条预告公告已经从官网上消失了**，不是改了措辞，是整条被这条
替换。也就是说 09-15 复核时记下的「公告规定的退件日已到、官网却没换版」（见第三节
时间维度那条）今天有了答案 —— 换版在生效前一天被法院拦下了。**当时没有替使用者
推断"今天该用哪一版"是对的**：三种猜测（当天晚些发布／页面滞后／换版推迟）都没猜中
真正的原因，而按公告字面去用 09/15/26 版恰好是错的。

**判别要点**：出现 `postponing the effective date`、`preliminarily enjoined`、
`is not accepting the [日期] edition` 时就是 A6。`is not accepting` 是最硬的信号 ——
A1–A5 里没有任何一类会说某个版本不被接受。

这类公告**必须保留**：它含 `edition` 与 mm/dd/yy，规则直接命中，这是对的。
真正的风险在于 `up` 字段 —— 见第三节新增的「跨表格日期串号」。

### A5 新版已发布 + 旧版无限期继续接受（**没有任何截止日**）

2026-09-11 在 **G-1450** 首次观察到（02/06/26 版）：

> The new edition, **02/06/26**, includes: An updated DHS Privacy Notice …; and
> A Card Verification Value (CVV) field on the fillable form. …
> USCIS will **continue to accept prior editions** of Form G-1450.

这是 A1–A4 的反面：前四类都有一个硬性切换日，A5 一个都没有。
改动限于隐私声明措辞和一个"USCIS 处理时不要求填写"的 CVV 栏，
属于**非实质性改版**，所以旧版不作废。

**为什么仍要保留这条**：它含 `edition` 与 `02/06/26`，规则直接命中，这是对的 ——
使用者需要知道"官网换了新版"这个事实，以及"旧版还能用"这个结论。
真正的风险在反面：若把它当成 A1/A2 处理，会凭空造出一个不存在的换版截止日。

**判别要点**：`continue to accept prior editions` / `also accept prior editions`
这类表述出现时，就是 A5。它同时会出现在 Edition Date 面板里，
`build.py` 认得这个表述并把"也接受的版本"记为「全部旧版」
（同样表述的还有 **I-912**：`prior editions (or a written request)`，
该表页首没有任何公告，这句话只出现在面板里）。

---

## 二、与版本无关的公告（未命中筛选，27/35 条）

筛选规则要挡掉的就是这些。类型如下：

| 类型 | 例子 |
| --- | --- |
| 通用提交提醒 | I-90、I-129F、I-601A：核对版本、所有页面须同版本（三处逐字相同） |
| 在线申请流程 | I-485、I-693：I-693 密封信封的处理方式；I-129：H-2A 未具名受益人不要主动上传 TLC |
| 诉讼与法院裁决 | I-131（BIA 先例）、I-129（H-1B 十万美元费用）、I-821D（DACA 三条） |
| 费用变动 | I-131/I-765/I-589（HR-1 费用暂停）、I-129（9-11 生物识别费）、I-765/I-589（FY2027 的 H.R.-1 费用通胀调整，2026-10-01 新增） |
| 缴费方式 | G-1450：纸质申请不再收支票／汇票，须用信用卡或 ACH |
| 配额用尽 | I-129：FY2026 的 H-3 特教交流访客名额已满；I-918：FY2025 的 U-1 一万个名额已满 |
| 材料规格 | I-765（照片不得修图）、I-693（退件后信封处理） |
| 表格适用范围 | I-90：条件绿卡持有者不应提交此表 |
| 特定群体流程 | I-131：乌克兰公民再假释的申请窗口；I-821D：DACA 续期建议提前 120–150 天；I-589：Ms. L 集体成员须纸质提交并在首页注明 |
| 法定义务提醒 | I-864／I-864A：担保人与家庭成员须对受助方领取的需经济审查公共福利承担偿还责任 |
| 代理人变动通知 | I-360：曾由某前移民律师代理的申请人须更新地址，否则影响案件处理 |
| 提交地点变更 | I-589：曾被 USCIS 终局裁决过的申请人改交 Dallas／Chicago lockbox，不再交 Asylum Intake Unit；I-485／I-130（2026-10-07 新增）、I-131／I-765／I-129／I-539／I-907／I-918／I-601／I-360（2026-10-08 新增）：改按提交理由／居住地查 Direct Filing Addresses 页或 Where to File 栏目，旧地址给到 11 月 9 日 |

「法定义务提醒」是 2026-09-09 复核时补记的类型：它讲的是**提交之后**的法律后果，
与「表格适用范围」（讲谁该提交）不同，原表八类都装不下。不含 "edition"
也不含 mm/dd/yy 日期，现有规则已正确挡下，无需调整筛选。

「缴费方式」与「代理人变动通知」是 2026-09-11 随新增表格补记的：前者讲**怎么付钱**，
与讲**收多少钱**的「费用变动」不是一回事；后者是对特定代理人的客户群发的
程序性通知，虽然也针对特定群体，但触发点是代理关系而非移民身份或案件类型。
两类同样既不含 "edition" 也不含 mm/dd/yy，规则已正确挡下。

「提交地点变更」是 2026-09-16 补记的（I-589 当日新增）。它讲**交到哪里**，
与讲谁该提交、怎么付钱、收多少钱都不同，原表十一类装不下。

2026-10-07 这一类**从一张表扩到三张**：I-485 与 I-130 当天各新增一条同模板的公告
（I-130 是它纳入追踪以来的第一条公告）。两条措辞逐句对应，只换了表格名和
「按提交理由」／「按居住地」查地址这一处：

> On Oct. 7, 2026, we changed the filing location for Form [X] … see our Direct Filing
> Addresses for Form [X] … page to determine where to file your form based on
> [your reason for filing／where you live]. We will provide a **30-day grace period**
> and accept forms postmarked **on or before Nov. 9, 2026**, that are sent to any
> prior filing location.

与 I-589 那条的区别只在宽限期的写法：I-589 是 `postmarked before Oct. 15, 2026`
并另写一句 `will reject … on or after Oct. 15, 2026`，这两条是
`postmarked on or before Nov. 9, 2026`，不写退件句。实质相同，都是收件地址的 30 天缓冲。

这一条还有一个**超出它本身的意义**：它写着
`we will provide a 30-day grace period and accept forms postmarked before Oct. 15, 2026`
—— 措辞与 A2 的换版宽限期几乎一模一样，讲的却是收件地址，和版本毫无关系。
现有规则靠「必须同时含 edition 和 mm/dd/yy」把它挡住了（它两样都不含），
但这**正面证实了第四节第 2 点的担忧**：`grace period` 这个词本身不携带版本语义，
任何想靠它判断换版宽限期的做法都会在这条公告上翻车。
反过来说，两个条件缺一不可这件事又多了一个实证。

**「同样的措辞讲别的事」的第三例**（2026-10-01 在 I-765／I-589 新增，同一条挂两处）：
FY2027 的 H.R.-1 费用通胀调整公告写着
`The new inflation-adjusted fees are effective Oct. 16, 2026. If you submit a request
postmarked on or after Oct. 16, 2026 … Any request postmarked on or after Oct. 16, 2026
without the proper filing fee will be rejected.`
—— `postmarked on or after [日期]` 加 `will be rejected` 正是 A1／A2 判别强制换版日
所依赖的句式，这里讲的却是**该交多少钱**，与版本毫无关系。
它属于已记的「费用变动」类型，不是新类型。

现有规则仍然正确挡下了它（**既不含 `edition`，也不含任何 mm/dd/yy**）。
但它对第四节第 1 点是一个明确的警告：那条「抽取强制切换日」的正则
`on or after ([A-Z][a-z]+\. \d{1,2}, \d{4})` 若直接拿去扫**全部**公告，
会从这条费用公告里抽出一个 10 月 16 日的「换版日」。
**第 1 点那条抽取必须只在已命中筛选的公告里做，不能对 `all` 做** ——
筛选规则是它的前置条件，不是可以绕过的一步。
**「同样的措辞讲别的事」的第四、第五例，也是目前最危险的一例形态**
（2026-10-07 在 I-485／I-130 新增）：上面那两条提交地点变更公告写着
`We will provide a 30-day grace period and accept forms postmarked on or before
Nov. 9, 2026` —— `30-day grace period` 加一个确切的截止日，这正是 A2 的判别特征，
讲的却是**寄到哪个地址**。

**它比前三例危险的地方在于日期本身**：这个 11 月 9 日**恰好就是 I-129 真实的强制
换版日**（面板原文 `Starting Nov. 9, 2026, we will accept only the 09/09/26 edition`）。
前三例对 `all` 跑切换日抽取，得到的是一个凭空的日期，一眼就看得出不对；
这一例得到的日期**与另一张表真实存在的换版日完全重合**，看上去完全可信 ——
误抽出来的「I-485 将于 11 月 9 日换版」会和「I-129 将于 11 月 9 日换版」并列呈现，
而后者是真的。**一个假阳性长得像真的，比长得离谱要难发现得多。**
这把第四节第 1 点那条前置条件从「建议」抬成了硬性要求。
它同时也是「跨表格日期串号」（第三节）的另一种形态：那条是一条公告里的日期属于
别的表格，这条是一条公告里的日期**与别的表格的日期巧合相等**。

**2026-10-08 升级到最坏形态：那条假的 11 月 9 日和那条真的，现在挂在同一张表上。**
这一波提交地点变更公告扩散到八张表时，其中一条挂的就是 **I-129 自己**。于是 I-129
页首同时有两条写着 11 月 9 日的公告：

> （地址）… We will provide a **30-day grace period** and accept forms postmarked
> on or before **Nov. 9, 2026**, that are sent to any prior filing location.
>
> （版本）… **Starting Nov. 9, 2026**, we will accept only the 09/09/26 edition
> of Form I-129. Until then, you can also use the 02/27/26 edition.

前一天那个假阳性至少还出在**别的表**上（I-485／I-130），拿表格号一比就能分开；
现在两条同表、同日期、同是「宽限期 + 截止日」的句式，**唯一的分野只剩
`edition` 一词在不在句子里**。对 `all` 跑切换日抽取，I-129 会得到两个 11 月 9 日，
去重之后甚至看不出多抽了一条 —— 错误被正确答案完全掩盖。

**结论不变但更硬了**：第四节第 1 点的抽取只能在 `kept` 上做。顺带一个推论 ——
凡是「同一张表抽出多个相同切换日」的情形，**不能当作互相印证**，
它们可能来自两条讲完全不同事情的公告。

现有规则仍然正确挡下了这两条（**既不含 `edition`，也不含任何 mm/dd/yy**）。

这同时也说明，五例「同样的措辞讲别的事」里（I-589 与 I-485／I-130 的收件地址、
FY2027 的费用、再加上 `grace period` 本身），**版本语义始终只由 `edition` 一词携带**，
日期和切换句式都是共用的。

这些内容对业务有价值，但**不属于版本追踪的范围**，混进来会淹没真正的版本变动。
上表十二类已覆盖当前全部 27 条无关公告。

**一个反复出现的现象**：同一条公告会原样挂在多个表格页上
（HR-1 费用暂停出现在 I-131／I-765／I-589 三处，通用提交提醒出现在
I-90／I-129F／I-601A 三处）。所以公告条数会随表格数增长，
但**公告类型不会**——新增 11 个表格只带来了两个新类型。

---

## 三、当前筛选规则

```
公告文本同时满足：含 "edition" 一词（不分大小写） 且 含 mm/dd/yy 格式日期
```

26 个表格实测：34 条公告命中 8 条，全部为 A1–A5；漏报 0，误报 0。

历次复核的实测结果：

| 日期 | 表格 | 公告 | 命中 | 规则调整 |
| --- | --- | --- | --- | --- |
| 2026-09-09 | 15 | 23 | 5 | 无 |
| 2026-09-10 | 15 | 24 | 6 | 无（I-129 新增 A4） |
| 2026-09-11 | 26 | 34 | 8 | 无（I-864A 属 A2，G-1450 新增 A5） |
| 2026-09-12 | 26 | 34 | 8 | 无（公告与前一日逐字相同，无新类型） |
| 2026-09-15 | 26 | 34 | 8 | 无（公告自 09-11 起逐字节未变，无新类型） |
| 2026-09-16 | 26 | 35 | 8 | 无（I-765／I-539 换版被禁令叫停，新增 A6；I-589 新增一条提交地点变更） |
| 2026-09-17 | 26 | 35 | 8 | 无（公告与前一日逐字节相同，无新类型） |
| 2026-09-18 | 26 | 35 | 8 | 无（公告自 09-16 起逐字节未变；I-485 的强制换版日到期，属时间维度边界情况） |
| 2026-09-19 | 26 | 35 | 8 | 无（I-485 换版兑现，A1 就地改写；其余 34 条逐字节未变） |
| 2026-09-26 | 26 | 35 | 8 | 无（公告自 09-19 起逐字节未变，覆盖 09-20 至 09-25 六天） |
| 2026-09-27 | 26 | 35 | 8 | 无（公告自 09-19 起第八天逐字节未变，无新类型） |
| 2026-09-28 | 26 | 35 | 8 | 无（公告自 09-19 起第九天逐字节未变，无新类型） |
| 2026-09-29 | 26 | 35 | 8 | 无（公告自 09-19 起第十天逐字节未变，无新类型） |
| 2026-09-30 | 26 | 35 | 8 | 无（公告自 09-19 起第十一天逐字节未变，无新类型） |
| 2026-10-01 | 26 | 37 | 8 | 无（I-765／I-589 各新增一条 FY2027 费用调整公告，属已记的费用变动类；I-864／I-864A 宽限期到期，要点已改写） |
| 2026-10-02 | 26 | 37 | 8 | 无（37 条公告与前一日逐字节相同，无新类型；I-864／I-864A 改写后的要点经复核仍成立） |
| 2026-10-03 | 26 | 37 | 8 | 无（37 条公告自 10-01 起第三天逐字节未变，无新类型；A2 到期对账第三天仍命中 I-864／I-864A，要点无需再动） |
| 2026-10-04 | 26 | 37 | 8 | 无（37 条公告自 10-01 起第四天逐字节未变，无新类型；A2 到期对账第四天仍命中 I-864／I-864A，要点无需再动） |
| 2026-10-05 | 26 | 37 | 8 | 无（37 条公告自 10-01 起第五天逐字节未变，无新类型；A2 到期对账第五天仍命中 I-864／I-864A，要点无需再动） |
| 2026-10-06 | 26 | 37 | 8 | 无（37 条公告自 10-01 起第六天逐字节未变，无新类型；A2 到期对账第六天仍命中 I-864／I-864A，要点无需再动） |
| 2026-10-07 | 26 | **39** | 8 | 无（I-485／I-130 各新增一条提交地点变更公告，属已记类型，两者均不含 `edition` 与 mm/dd/yy，规则正确挡下；A2 到期对账第七天仍命中 I-864／I-864A，要点无需再动） |
| 2026-10-08 | 26 | **47** | 8 | 无（提交地点变更公告扩散到另外八张表，属已记类型，八条均不含 `edition` 与 mm/dd/yy，规则正确挡下；另有三处纯文本润色，见第三节末；A2 到期对账第八天仍命中 I-864／I-864A，要点无需再动） |

2026-10-08 的核对方式：先 `git fetch`（**fetch 陷阱第四次兑现**，且这次最隐蔽 ——
克隆下来的工作副本停在 10-05 那条复核记录、落后两个提交，而 `git status` 却报
「up to date with origin/main」，因为本地的远端跟踪引用本身就是克隆时的旧值。
**不能靠 `git status` 判断是否最新，必须先 fetch**）。再触发抓取
（run 37783399659，`workflow_dispatch`，conclusion `success`，13:19:06 → 13:20:13
共 67 秒，耗时证明真的抓过而非走了「当天已抓过则跳过」那条分支），
26/26 成功、`changed` 为 0、无 `error`、无 `stale`。

**`audit-alerts.json` 的 md5 变了**（`25b4b8b9…` → `4f1da2f3…`），`git diff` 逐行看过，
差异只有两类，无一处删改：

1. **八条真正的新增**：I-131、I-765、I-129、I-539、I-907、I-918、I-601、I-360
   各新增一条 10 月 7 日的提交地点变更公告，公告数 39 → 47。I-907 与 I-601 原先
   `all` 为空，这是两者纳入追踪以来的第一条公告。八条均不含 `edition`、不含
   mm/dd/yy，规则正确挡在 `kept` 之外，`kept` 仍是 8 条。
   （另注：I-918 那条官网把日期写成了 `On Oct. 7. 2026`，句号代替逗号，是官网的笔误，
   不影响筛选 —— 这类日期本来就不参与匹配。）
2. **三处纯文本润色**：I-765 的 A6 补了一个空格、I-90 的通用提交提醒换了句式、
   I-360 的代理人变动通知多了一个 `the`，**三处都没有改变含义，且每处只改了一部分
   页面**，由此记下「跨表格复用的公告会各自漂移」这条边界情况（见第三节末）。

`forms.json` 其余差异只有 `generated_at` 一行与 I-765 那条 A6 的空格、
`docs/index.html` 只有页脚检查时间一行与同一处空格（均已 `git diff` 逐行确认），
即 26 个表格的 `cur`／`also`／`up` 自 09-19 起仍未动过，`history.json` 未动。

本轮独立重跑正反向扫描而非引用前几日的结论。先用筛选规则本身（含 `edition` 且含
mm/dd/yy）对 47 条重跑并逐条与 `kept` 比对，**判定与 `kept` 完全一致，无一条错位**；
未命中的 39 条中**含 mm/dd/yy 的 0 条**，含 `edition` 的仍是那条通用提交提醒的三份
副本（I-90 为 792 字符、I-129F／I-601A 各 799 字符，今天起不再逐字相同），均为泛指。
47 条按文本去重是 43 条不同的公告，未命中的 39 条去重后是 35 条，
**逐条通读，全部落在第二节已记的十二类里，无新类型**。
反向扫描这次换了一张**以「另有一版存在、旧版该作废」但完全绕开 `edition` 一词**为
中心的词表（`revised form｜new form version｜new version｜updated form｜
form has been (revised|updated|replaced)｜we (have )?(revised|updated|republished|
reissued) the form｜supersed｜no longer (valid|current|accepted|acceptable)｜obsolete｜
out of date｜outdated｜use the (latest|newest|most recent|current) (form|version|release)｜
download the (new|latest|revised|current)｜(revision|print|printing|release) date｜
dated [月] D, YYYY｜revision｜iteration｜variant｜printing｜release｜both versions｜
either version｜two versions｜which version｜previous version｜prior version`），
在未命中的 39 条里**触发 0 条**。这张词表把 10-06 那轮的结论又验证了一次：
`edition` 的同义词（`revision`、`iteration`、`variant`、`printing`）在 47 条公告里
一次都没出现过，**USCIS 讲版本至今只用 `edition` 一个词**。
再按第二节第 2 点那个担忧查了非 mm/dd/yy 的版本号写法（`mm/dd/yyyy`、`yyyy-mm-dd`、
`mm-dd-yy`、`mm.dd.yy`，以及英文日期加 `edition`／`version`、`edition`／`version`
加英文日期两个方向），六种写法同样**全部触发 0 条**。
8 条命中的公告逐条通读，归类仍是 A1×1（I-485 兑现形态）、A2×2、A3×1（I-485 的
Casa Inc. v. Trump）、A4×1、A5×1、A6×2，**无误报无漏报**。

中文要点按今天的日期逐条核过，**过时的一条都没有**。带日期的要点里，已过去的日期
全部写在已然语态里（I-485 的 9 月 18 日发布日与 9 月 2 日 Casa 禁令日、I-693 的
2025 年 7 月 2／3 日签字日分界、I-129 的 9 月 9 日发布日、I-765／I-539 的 9 月 14 日
法院命令日与 7 月 17 日联邦公报日、I-864／I-864A 的 8 月 31 日发布日与 9 月 30 日
宽限期结束日），唯一的将来日期是 I-129 的 11 月 9 日，还有 32 天。
按第四节第 1 点在 `kept`（不是 `all`）上抽强制切换日，抽出 I-485 的 9/18、
I-864／I-864A 的 10/1、I-129 的 11/9 共四条，两条对账：
「切换日已过但 `cur` 未变」**未命中** —— 从否定句（`Reject`／`will not process any`／
`is not accepting`／`will not accept`）里取出的「要退件的版本」分别是 I-485 的
01/20/25、I-864／I-864A 的 10/17/24、I-129 的 02/27/26，而四张表的 `cur` 分别是
09/18/26、08/24/26、08/24/26、09/09/26，没有一张落在要退件的名单里。
**10-06 那条教训本轮第一次写就又踩了一遍**：头一版正则把 `only accept`／
`accept only` 也当成否定句，于是把 I-864／I-864A 的新版 08/24/26 抓进了「要退件」
名单，两张表双双假报矛盾 —— 这条对账**只能从否定句取版本号，不能从 `accept the` 取**，
因为同一条公告里新旧两版是并列写的。
「切换日已过、公告措辞仍是现在时」**第八天仍命中 I-864／I-864A**，公告里那句
`USCIS is providing a 30-day grace period during which we will accept the 10/17/24
edition` 自 8 月 31 日起一字未改，而面板 `cur` 本就已是 08/24/26、`also` 为空，
要点已在 10-01 按到期改写，本轮无需再动 —— 第一节 A2 末尾那条观察至此连续印证八天。

面板原文另逐字对了一遍：G-28 与 I-918 的「新版即将发布」均未变，I-693 的签字日
分版规则、G-1145 的 `You can also use previous editions`、G-1450 与 I-912 的
`also accept prior editions`（I-912 另含 `or a written request`）、I-129 的
`Starting Nov. 9, 2026` 两版并行句与各自要点逐字相符。
26 个表格 `up` 全部为空、`soon` 全部为假（页面上「即将换版」标记 0 个），
I-765／I-539 的 `up: ""` 覆盖经第十九轮抓取仍生效，`cn` 齐备（26/26）且
`notes.yaml` 与 `forms.yaml` 一一对应、无多余条目、无四个允许字段之外的键
（13 个表格有 `note`），`up` 非空却无要点的表格 0 个，`also` 非空的仍是 5 张
（I-129／I-693／G-28／G-1450／I-912）。无截断，公告最长 2310 字符（I-131／I-765／
I-589 共用的 HR-1 那条）余量 4.3 倍、Edition Date 原文最长 315 字符（I-693）余量 19 倍。

今天那八条新增公告没有给 `notes.yaml` 带来改动，理由与 09-16 的 I-589、10-07 的
I-485／I-130 一致：**提交地点变更不属于版本追踪的范围**，页面已原样展示公告原文
供员工核对。I-129 那条「两个 11 月 9 日同表并存」也没有写进要点 —— 该表要点已经
把版本规则的硬日期写清楚了，再去解释另一条讲地址的公告属于替使用者判断，
按同一条范围原则不做。

2026-10-07 的核对方式：先 `git fetch`（本次会话克隆下来的工作副本停在 10-05 那条
复核记录，落后 origin/main 两个提交，**fetch 陷阱第三次兑现**），再触发抓取
（run 37627704338，`workflow_dispatch`，conclusion `success`，13:20:23 → 13:21:30
共 67 秒 —— 按上一轮记下的那条，耗时而非 `conclusion` 才能证明真的抓过），
26/26 成功、`changed` 为 0、无 `error`、无 `stale`。

**`audit-alerts.json` 的 md5 变了**（`69e86c0f…` → `25b4b8b9…`），`git diff` 逐行看过，
差异只有两类，无一处删改：

1. **两条真正的新增**：I-485 与 I-130 各新增一条 10 月 7 日的提交地点变更公告
   （492／418 字符），公告数 37 → 39。I-130 原先 `all` 为空，这是它纳入追踪以来
   的第一条公告。两条均不含 `edition`、不含 mm/dd/yy，规则正确挡在 `kept` 之外，
   `kept` 仍是 8 条。
2. **一处纯顺序变动**：I-485 页首那两条公告在官网上调了个位置，9 月 18 日那条
   （A1 兑现形态）移到了 9 月 4 日 Casa 禁令那条（A3）之前，**两条文本逐字未改**。
   `forms.json` 里 I-485 的 `alerts` 数组顺序随之变了，`cur`／`also`／`up` 未动。

`forms.json` 其余差异只有 `generated_at` 一行、`docs/index.html` 只有页脚检查时间
一行与 I-485 那两条公告的顺序（均已 `git diff` 逐行确认），即 26 个表格的
`cur`／`also`／`up` 自 09-19 起仍未动过。

本轮独立重跑正反向扫描而非引用前几日的结论。先用筛选规则本身（含 `edition` 且含
mm/dd/yy）对 39 条重跑并逐条与 `kept` 比对，**判定与 `kept` 完全一致，无一条错位**；
未命中的 31 条中**含 mm/dd/yy 的 0 条**，含 `edition` 的仍是 I-90／I-129F／I-601A
那条逐字相同的通用提交提醒（各 799 字符），均为泛指。
39 条按文本去重是 33 条不同的公告（4 条跨表格复用），未命中的 31 条去重后是 26 条，
**逐条通读，全部落在第二节已记的十二类里，无新类型**。
反向扫描这次换了一张**以「规则／诉讼驱动的版本变动」与「预览版、截止日」为中心**的
词表（`preview version｜preview edition｜interim final rule｜final rule｜proposed rule｜
rulemaking｜Federal Register｜vacat｜stay(ed) the｜remand｜set aside the rule｜
effective date of the rule｜implement the (IFR|rule)｜enjoin｜injunction｜court order｜
district court｜last day to｜final day to｜deadline to (file|submit)｜through [月] D｜
until [月] D｜before [月] D, YYYY｜on or after [月] D, YYYY｜beginning [月] D, YYYY｜
starting [月] D, YYYY｜will reject｜be rejected｜not be accepted｜we will only accept｜
accept only｜grace period｜no grace period`），在未命中的 31 条里触发 11 条，逐条看过
全部落在已记的十二类里：`final rule`／`vacat`／`district court`／`injunction` 命中的是
I-129 的 9-11 生物识别费终局规则与十万美元费用裁决、I-821D 的 DACA 三条、I-589 的
Ms. L 集体成员流程（都是「诉讼与法院裁决」或「费用变动」，讲的是钱与资格而不是版本）；
`on or after Oct. 16, 2026` 加 `be rejected` 命中的是 I-765／I-589 的 FY2027 费用调整；
`grace period` 加 `before Nov. 9, 2026` 命中的正是今天新增的 I-485／I-130 那两条。
**这张词表的教训是它把「法院禁令」这个 A6 的核心信号从反面证了一遍**：
`injunction`／`district court`／`vacat` 在未命中的公告里出现了四次，全都与版本无关 ——
A6 之所以能被规则捞住，靠的不是禁令措辞，而是那句
`is not accepting the 09/15/26 edition` 里的 `edition` 加 mm/dd/yy。
**单靠诉讼词去识别版本公告会误报四条。**
再按第二节第 2 点那个担忧查了非 mm/dd/yy 的版本号写法（`mm/dd/yyyy`、`yyyy-mm-dd`、
`mm-dd-yy`、`mm.dd.yy`，以及「英文日期 + edition／version／form」、
「edition／version + 英文日期」、`dated [英文日期]` 三个方向），**七种写法全部触发 0 条**
—— USCIS 至今只用 mm/dd/yy 写版本号。
8 条命中的公告逐条通读，归类仍是 A1×1（I-485 兑现形态）、A2×2（I-864／I-864A）、
A3×1（I-485 的 *Casa Inc. v. Trump*）、A4×1（I-129）、A5×1（G-1450）、
A6×2（I-765／I-539，两张表逐字相同已程序比对确认），无误报无漏报。

中文要点按今天的日期逐条核过，**过时的一条都没有**。11 条带日期的要点里，已过去的
日期全部写在已然语态里（I-485 的 9 月 18 日发布日与 9 月 2 日 Casa 禁令日、I-693 的
2025 年 7 月 2／3 日签字日分界、I-129 的 9 月 9 日发布日、I-765／I-539 的 9 月 14 日
法院命令日与 7 月 17 日《联邦公报》日、I-864／I-864A 的 8 月 31 日发布日与 9 月 30 日
宽限期结束日），唯一的将来日期是 I-129 的 11 月 9 日，还有 33 天。
按第四节第 1 点在 `kept`（不是 `all`）上抽强制切换日，抽出 I-485 的 9/18、
I-864／I-864A 的 10/1、I-129 的 11/9 四条，两条对账：
「切换日已过但 `cur` 未变」**未命中** —— 从 `Reject`／`will not process any`／
`is not accepting`／`will not accept` 这类否定句里取出的「要退件的版本」分别是
I-485 的 01/20/25 与 09/04/26、I-864／I-864A 的 10/17/24、I-129 的 02/27/26，
而四张表的 `cur` 分别是 09/18/26、08/24/26、08/24/26、09/09/26，**没有一张落在
要退件的名单里**（上一轮记下的教训在这里又用了一次：否定句才能取，`accept the`
不能取，否则新旧两版并列会把三张表全部假报成矛盾）。
「切换日已过、公告措辞仍是现在时」**第七天仍命中 I-864／I-864A** —— 公告里
`USCIS is providing a 30-day grace period during which we will accept the 10/17/24
edition` 这个现在时自 8 月 31 日起一字未改，而面板 `cur` 本就已是 08/24/26、
`also` 为空，正是第一节 A2 末尾说的「A2 兑现时抓取侧三处一处都不动」，
要点已在 10-01 按到期改写，本轮无需再动。
面板原文另逐字对了一遍：G-28（`We will publish a new edition of this form soon`，
09/17/18 与 05/23/18 并列）与 I-918（同一措辞，01/20/25）的「新版即将发布」均未变，
I-693 的签字日分版规则（原文 `on or before July 2, 2025` 两版皆可、
`July 3, 2025 or later` 只收 01/20/25）、G-1145 的 `You can also use previous editions`、
G-1450 的 `We will also accept prior editions`、I-912 的
`prior editions (or a written request)`、I-129 的
`Starting Nov. 9, 2026, we will accept only the 09/09/26 edition. Until then, you can
also use the 02/27/26 edition.` 与各自要点逐字相符。

**今天新增的那两条公告没有给 `notes.yaml` 带来改动**，理由与 09-16 的 I-589 一致：
提交地点变更不属于版本追踪的范围（第二节），页面已原样展示公告原文供员工核对。
但它那个 11 月 9 日值得单独记一笔 —— 它与 I-129 真实的换版日重合，是五例
「同样的措辞讲别的事」里第一个**假阳性长得像真的**的例子（已补记入第二节末）。

26 个表格 `up` 全部为空、`soon` 全部为假，I-765／I-539 的 `up: ""` 覆盖经第十八轮
抓取仍然生效；`cn` 齐备（26/26），`notes.yaml` 与 `forms.yaml` 一一对应、无多余条目、
无「只允许改的四个字段」之外的键（13 个表格有 `note`），`up` 非空却没有中文要点的
表格 0 个。`also` 非空的仍是 5 张（I-129 的 02/27/26、I-693 的 03/09/23、
G-28 的 05/23/18、G-1450 与 I-912 的「全部旧版」）。
无截断（无一条以 `…` 收口），公告最长仍是 2310 字符（I-765 名下的 HR-1 费用暂停）
余量 4.3 倍、Edition Date 原文最长 315 字符（I-693）余量 19 倍。

未改 `notes.yaml` 与任何代码逻辑，无需重新生成网页。G-1145「也接受」栏为空仍是
已报在 #4 的识别遗漏，未重复开 Issue；本轮无需人工判断的新情形，未开新 Issue。

2026-10-06 的核对方式：先 `git fetch`（本次工作副本已停在 `main` 最新提交，无需追赶），
再触发抓取（run 37469860151，`workflow_dispatch`，conclusion `success`，耗时 65 秒），
抓取 26/26 成功、`changed` 为 0、无 `error`、无 `stale`。按 md5 比对 `audit-alerts.json`，
**自 10-01 起第六天逐字节相同**（仍是 `69e86c0f…`）；本轮抓取提交只动了三个文件，
`forms.json` 只差 `generated_at` 一行、`docs/index.html` 只差页脚检查时间一行、
`last_checked.json` 只差 `checked_at`（均已 `git diff` 逐行确认），`history.json` 未动，
即 26 个表格的 `cur`／`also`／`up` 六天没动过。
再独立重跑正反向扫描而非引用前几日的结论 —— 先用规则本身（含 `edition` 且含
mm/dd/yy）对 37 条重跑并逐条与 `kept` 比对，**判定与 `kept` 完全一致，无一条错位**；
未命中的 29 条中**含 mm/dd/yy 的 0 条**，含 `edition` 的仍是 I-90／I-129F／I-601A
那条逐字相同的通用提交提醒（各 799 字符），均为泛指。
反向扫描这次换了一张**以「另有一版存在、该换过去」但绕开 `edition` 一词为中心**的词表
（`revision｜iteration｜new release｜now available｜newly available｜download the
(new|revised|current|latest)｜latest (form|version|release)｜current (printing|release)｜
variant｜new copy｜updated copy｜we (have) (revised|updated|republished|reissued) (the|Form)｜
has been (replaced|superseded)｜switch to｜transition to｜begin using｜start using｜
change(d) the form｜form change｜only the (new|current|latest)｜use the (new|current|latest)｜
no longer (use|valid|current)｜two versions｜both versions｜either version｜which version｜
same version｜matching version｜printed on the form｜bottom of the (page|form)｜edition date`），
在未命中的 29 条里**只触发 3 条**，全是 I-90／I-129F／I-601A 那条通用提交提醒
（命中的是 `edition date` 与 `bottom of the page`，讲的是「去哪儿看版本日期」而不是
某一版的存废），挡下是对的。**这张词表的教训**：`edition` 的同义词（`revision`、
`iteration`、`variant`、`printing`）在 37 条公告里一次都没出现过，USCIS 讲版本只用
`edition` 一个词，这给「必须含 `edition`」这个条件又添一个实证。
再按第二节第 2 点那个担忧查了非 mm/dd/yy 的版本号写法（`mm/dd/yyyy`、`yyyy-mm-dd`、
`mm-dd-yy(yy)`、`mm.dd.yy(yy)`，以及「英文日期 + edition／version／form」与
「edition／version + 英文日期」两个方向），**六种写法全部触发 0 条** ——
USCIS 至今只用 mm/dd/yy 写版本号。
未命中的 29 条按文本去重后是 **24 条不同的公告**（三条跨表格复用：HR-1 费用暂停挂
I-131／I-765／I-589，通用提交提醒挂 I-90／I-129F／I-601A，FY2027 费用调整挂 I-765／I-589），
逐条通读，**全部落在第二节已记的十二类里，无新类型**。
8 条命中的公告逐条通读，归类仍是 A1×1（I-485 兑现形态）、A2×2（I-864／I-864A）、
A3×1（I-485 的 *Casa Inc. v. Trump*）、A4×1（I-129）、A5×1（G-1450）、A6×2（I-765／I-539），
无误报无漏报。无截断，公告最长 2310 字符（I-765 名下的 HR-1 费用暂停）余量 4.3 倍、
Edition Date 原文最长 315 字符（I-693）余量 19 倍。

中文要点按今天的日期逐条核过，**过时的一条都没有**。7 条带日期的要点里，
已过去的日期全部写在已然语态里（I-485 的 9 月 18 日发布日与 9 月 2 日 Casa 禁令日、
I-693 的 2025 年 7 月 2／3 日签字日分界、I-129 的 9 月 9 日发布日、
I-765／I-539 的 9 月 14 日法院命令日与 9 月 15 日那条被取代的换版日、
I-864／I-864A 的 8 月 31 日发布日与 9 月 30 日宽限期结束日），
唯一的将来日期是 I-129 的 11 月 9 日，还有 34 天，其「旧版 02/27/26 可用到 11 月 9 日
之前」与面板原文 `Starting Nov. 9, 2026, we will accept only the 09/09/26 edition.
Until then, you can also use the 02/27/26 edition.` 逐字对应。
按第四节第 1 点在 `kept`（不是 `all`）上抽强制切换日，抽出 I-485 的 9/18、
I-864／I-864A 的 10/1、I-129 的 11/9 四条，两条对账：
「切换日已过但 `cur` 未变」**未命中** —— 三条已过期的切换日里，公告点名要退件的版本
分别是 I-485 的 01/20/25 与 09/04/26、I-864／I-864A 的 10/17/24，
而三张表的 `cur` 分别是 09/18/26、08/24/26、08/24/26，没有一张的 `cur` 落在要退件的名单里；
**（本轮一个方法上的教训：第一次写这条对账时把「要退件的版本」正则写得太松，
连 `Only accept the 09/18/26` 里的新版也抓了进去，于是三张表全部假报矛盾。
这条对账只能从 `Reject`／`will not process any`／`is not accepting`／`will not accept`
这类否定句里取版本号，不能从 `accept the` 取 —— 同一条公告里新旧两版是并列写的。）**
「切换日已过、公告措辞仍是现在时」第六天仍命中 I-864／I-864A —— 公告里
`USCIS is providing a 30-day grace period during which we will accept the 10/17/24
edition` 这个现在时一字未改，而面板 `cur` 本就已是 08/24/26、`also` 为空，
正是第一节 A2 末尾说的「A2 兑现时抓取侧三处一处都不动」，要点已在 10-01 按到期改写，
本轮无需再动。
面板原文另逐字对了一遍：G-28（`We will publish a new edition of this form soon`，
09/17/18 与 05/23/18 并列）与 I-918（同一措辞，01/20/25）的「新版即将发布」均未变，
I-693 的签字日分版规则（原文 `on or before July 2, 2025` 两版皆可、`July 3, 2025 or later`
只收 01/20/25，要点写的 2025 年与原文一致）、G-1145 的 `You can also use previous
editions`、G-1450 的 `We will also accept prior editions`、I-912 的
`We will also accept prior editions (or a written request)` 与各自要点逐字相符。
另单独核了 10-01 那两条 FY2027 费用调整公告：其 10 月 16 日只剩 10 天，
但它是**费用生效日而非换版日**，句式与换版切换句一模一样，正是第四节第 1 点警告的陷阱；
本轮抽取按约定只对 `kept` 做，没有把它误抽成换版日，`notes.yaml` 不涉及费用，无需补要点。

26 个表格 `up` 全部为空、`soon` 全部为假，I-765／I-539 的 `up: ""` 覆盖经第十七轮抓取
仍然生效；`cn` 齐备（26/26），`notes.yaml` 与 `forms.yaml` 一一对应、无多余条目、
无「只允许改的四个字段」之外的键（13 个表格有 `note`），`up` 非空却没有中文要点的
表格 0 个。

未改 `notes.yaml` 与任何代码逻辑，无需重新生成网页。G-1145「也接受」栏为空仍是已报
在 #4 的识别遗漏，未重复开 Issue；本轮无新发现，未开新 Issue。

2026-10-05 的核对方式：先 `git fetch` 把工作副本从 09-30 追到 10-04，再触发抓取
（run 37316522984，`workflow_dispatch`，conclusion `success`），抓取 26/26 成功、
`changed` 为 0、无 `error`、无 `stale`。按 md5 比对 `audit-alerts.json`，
**自 10-01 起第五天逐字节相同**（仍是 `69e86c0f…`）；`forms.json` 与前一日的差异
只有 `generated_at` 一行、`docs/index.html` 只有页脚检查时间一行（均已 `git diff`
逐行确认），即 26 个表格的 `cur`／`also`／`up` 五天没动过。
再独立重跑正反向扫描而非引用前几日的结论 —— 先用规则本身（含 `edition` 且含
mm/dd/yy）对 37 条重跑并逐条与 `kept` 比对，**判定与 `kept` 完全一致，无一条错位**；
未命中的 29 条中**含 mm/dd/yy 的 0 条**，含 `edition` 的仍是 I-90／I-129F／I-601A
那条逐字相同的通用提交提醒（各 799 字符），均为泛指。
反向扫描这次换了一张**以「表格本身被改动」的动作与产物为中心**的词表
（`fillable｜downloadable｜new (pdf|file|form)｜form (and|&) instructions｜instructions
(have|were|are) been (updated|revised)｜print(ed) (date|version)｜re-issu｜re-publish｜
re-release｜replac* (the) form｜form number｜page count｜two-page｜new pages｜updated
(the) instructions｜signature (page|block)｜checkbox｜new (field|question|item)`），
在未命中的 29 条里触发 6 条，逐条看过全部落在第二节已记的十二类里：`checkbox` 三处
全是 Ms. L. v. ICE 的 HR-1 费用暂停公告（挂在 I-131／I-765／I-589，指的是 I-131
Part 9 里那个 EAD 勾选框，讲的是哪些人不用付费），`form and instructions` 三处
全是那条通用提交提醒（指版本日期印在表格末页），挡下都是对的 —— **这张词表的教训是
「表格被改动」的措辞在费用类和流程类公告里同样大量出现，靠它判断换版只会误报**。
另跑了一张「哪一版能用／不能用」的结论性措辞表（`accept only｜only accept｜
will not accept｜cannot accept｜stop accepting｜must (use|submit|file) the｜
required version｜valid version｜older (form|version)｜out-dated｜expired form｜
superseded｜null and void｜invalid`），在未命中的 29 条里**触发 0 条**。
再按第二节第 2 点那个担忧查了非 mm/dd/yy 的版本号写法（`mm/dd/yyyy`、`yyyy-mm-dd`、
`mm-dd-yy`、`mm.dd.yy`，以及「英文日期 + edition／version／form」），
**触发 0 条** —— USCIS 至今只用 mm/dd/yy 写版本号。
8 条命中的公告逐条通读，归类仍是 A1×1（I-485 兑现形态）、A2×2（I-864／I-864A）、
A3×1（I-485 的 *Casa Inc. v. Trump*）、A4×1（I-129）、A5×1（G-1450）、
A6×2（I-765／I-539），无误报无漏报。无截断，公告最长 2310 字符（I-765 名下的 HR-1
费用暂停）余量 4.3 倍、Edition Date 原文最长 315 字符（I-693）余量 19 倍。

中文要点按今天的日期逐条核过，**过时的一条都没有**。带日期的要点里，已过去的日期
全部写在已然语态里（I-485 的 9 月 18 日发布日、I-765／I-539 的 9 月 14 日法院命令日、
I-864／I-864A 的宽限期已于 9 月 30 日结束），唯一的将来日期是 I-129 的 11 月 9 日，
还有 35 天，其「旧版 02/27/26 可用到 11 月 9 日之前」与面板原文 `Starting Nov. 9,
2026, we will accept only the 09/09/26 edition. Until then, you can also use the
02/27/26 edition.` 逐字对应。按第四节第 1 点在 `kept`（不是 `all`）上抽强制切换日，
抽出 I-485 的 9/18、I-864／I-864A 的 10/1、I-129 的 11/9 四条，两条对账：
「切换日已过但 `cur` 未变」未命中（I-485 的 `cur` 正是 09/18/26、I-864／I-864A 正是
08/24/26）；「切换日已过、公告措辞仍是现在时」第五天仍命中 I-864／I-864A —— 公告里
`USCIS is providing a 30-day grace period during which we will accept the 10/17/24
edition` 这个现在时一字未改，而面板 `cur` 本就已是 08/24/26、`also` 为空，
正是第一节 A2 末尾说的「A2 兑现时抓取侧三处一处都不动」，要点已在 10-01 按到期改写，
本轮无需再动。
面板原文另逐字对了一遍：G-28（`We will publish a new edition of this form soon`，
09/17/18 与 05/23/18 并列）与 I-918（同一措辞，01/20/25）的「新版即将发布」均未变，
I-693 的签字日分版规则（7 月 2 日前签字两版皆可、7 月 3 日起只收 01/20/25）、
G-1145 的 `You can also use previous editions`、G-1450 的 `We will also accept prior
editions`、I-912 的 `We will also accept prior editions (or a written request)`
与各自要点逐字相符。
另单独核了 10-01 新增的那两条 FY2027 费用调整公告：其 10 月 16 日只有 11 天，
但它是**费用生效日而非换版日**（`Any request postmarked on or after Oct. 16, 2026
without the proper filing fee will be rejected`），句式与换版切换句一模一样，
正是第四节第 1 点警告的「只能在 `kept` 上抽切换日」那个陷阱；本轮抽取按约定只对
`kept` 做，没有把它误抽成换版日，`notes.yaml` 不涉及费用，无需补要点。

26 个表格 `up` 全部为空、`soon` 全部为假，I-765／I-539 的 `up: ""` 覆盖经第十六轮
抓取仍然生效；`cn` 齐备（26/26），`notes.yaml` 与 `forms.yaml` 一一对应、无多余条目、
无「只允许改的四个字段」之外的键，`up` 非空却没有中文要点的表格 0 个。
另核了 `docs/index.html` 页脚那个「已公告新版 1」的静态数字：它是模板里的占位值，
页面脚本按内嵌的 `FORMS` 重算（`index.html:740`），实际算出 0，与 26 个表格
`soon` 全为假相符，不是显示错误。

未改 `notes.yaml` 与任何代码逻辑，无需重新生成网页。G-1145「也接受」栏为空仍是已报
在 #4 的识别遗漏，未重复开 Issue；本轮无新发现，未开新 Issue。

2026-10-02 的核对方式：先按 md5 比对 `audit-alerts.json`，**与前一日逐字节相同**
（仍是 `69e86c0f…`），即昨天新增的那两条 FY2027 费用调整公告与原有 35 条今天都没再动。
`forms.json` 与前一日的差异只有 `generated_at` 一行、`docs/index.html` 只有页脚的
检查时间一行（均已 `git diff` 逐行确认），即 26 个表格的 `cur`／`also`／`up` 没动过，
`changed` 为 0，抓取 26/26 成功、无 `error`。
再独立重跑正反向扫描而非引用前一日的结论 —— 先用规则本身（含 `edition` 且含
mm/dd/yy）对 37 条重跑并逐条与 `kept` 比对，**判定与 `kept` 完全一致，无一条错位**；
未命中的 29 条中**含 mm/dd/yy 的 0 条**，含 `edition` 的仍是 I-90／I-129F／I-601A
那条逐字相同的通用提交提醒（各 799 字符），均为泛指。
反向扫描这次换了个做法，把判别词与噪音词分开跑：先只用版本语义的词
（`revised form|revised edition|new version|form version|older version|previous version|
latest edition|new edition|do not use the form|will not be accepted|not accepting|
outdated|obsolete|supersed|replaced by|reprint|re-?issued|version of the form|edition date`），
**在未命中的 29 条里只触发 3 条，全是 I-90／I-129F／I-601A 那条通用提醒命中的
`edition date`**，挡下是对的；再把月份名与 `may` 等噪音词单独跑一遍，触发 28 条，
逐条看过全部落在第二节已记的十二类里，无一条讲版本。另按第二节第 2 点那个担忧
专门查了**用文字日期表述版本号**的写法（`(月份名) D, YYYY edition|version`），
**触发 0 条** —— USCIS 至今没在公告里用文字日期指代版本，始终是 mm/dd/yy。
中文要点按今天的日期逐条核过：7 条带日期的要点里，已过去的日期全部写在
已然语态里（发布日、法院命令日、宽限期已结束），没有一条把过去的日期当成将来的承诺；
唯一的将来日期是 I-129 的 11 月 9 日，仍未到。按第四节第 1 点做的两条对账
——「切换日已过但 `cur` 未变」与「切换日已过、公告措辞仍是现在时」——
前者未命中，后者仍命中 I-864／I-864A（公告里 `will accept the 10/17/24 edition`
这个现在时自 8 月 31 日起一直没改），但要点昨天已按到期改写，无需再动。
26 个表格 `up` 全部为空、`soon` 全部为假，I-765／I-539 的 `up: ""` 覆盖经第十三轮
抓取仍生效，`cn` 齐备。无截断，最长仍为 2310 字符，余量 4.3 倍。

2026-10-01 的核对方式：先按 md5 比对 `audit-alerts.json`，**十二天来第一次变了**
（`67f3c752…` → `69e86c0f…`）。`git diff` 逐行看过，差异只有两处新增、无一处删改：
I-765 与 I-589 各新增同一条 FY2027 的 H.R.-1 费用通胀调整公告（各 621 字符，
9 月 30 日发布，10 月 16 日生效），公告数 35 → 37。原有 35 条**逐字节未变**，
其中 I-765／I-539 那条禁令公告（A6）与 I-864／I-864A 那两条 A2 都一字未动。
`forms.json` 除 `generated_at` 外内容未变，即 26 个表格的 `cur`／`also`／`up`
十二天没动过，`changed` 仍为 0，抓取 26/26 成功、无 `error`。
再独立重跑正反向扫描而非引用前几日的结论 —— 先用规则本身（含 `edition` 且含
mm/dd/yy）对 37 条重跑并逐条与 `kept` 比对，**判定与 `kept` 完全一致，无一条错位**；
未命中的 29 条中**含 mm/dd/yy 的 0 条**，含 `edition` 的仍是 I-90／I-129F／I-601A
那条逐字相同的通用提交提醒（各 799 字符），均为泛指。
反向扫描先用历次词表整体重扫，触发的 8 条全部落在第二节已记的十二类里；
再针对新增那条公告专门加 `will be rejected|without the proper|inflation|
fee adjustment|must include the new|increase certain|Federal Register notice|
new fee|are effective` 一组词，触发的正是 I-765／I-589 那两份副本，
逐条看过：**它是「同样的措辞讲别的事」的第三例**，`postmarked on or after` 加
`will be rejected` 的句式与 A1／A2 的换版切换句完全一样，讲的却是费用，
而它既不含 `edition` 也不含 mm/dd/yy，规则挡下是对的（已补记入第二节末，
并据此明确了第四节第 1 点的前置条件：切换日抽取只能在 `kept` 上做，不能对 `all` 做）。
`yyyy-mm-dd`、`mm/dd/yyyy` 与 `edition` 后跟英文日期的写法仍是一条都没有。
命中的 8 条逐条复看，A1 一条（I-485，兑现形态）、A2 两条、A3 一条、A4 一条、
A5 一条、A6 两条，归类不变，无误报无漏报。无截断，最长仍为 2310 字符
（HR-1 费用暂停公告，现记在 I-765 名下），余量 4.3 倍。

**本轮的实质动作是那条预定的改写**：按第四节第 1 点抽出 `kept` 里的强制切换日与
当天比对，I-864／I-864A 的 10 月 1 日**今天到期**（I-485 的 9 月 18 日已过且
`cur` 相符，I-129 的 11 月 9 日还有 39 天）。两条要点原写「旧版 10/17/24 的宽限期
到 9 月 30 日为止」，今天起已经过时，已改写为「宽限期已于 9 月 30 日结束，
现在只接受 08/24/26 版」，并把公告里的 8 CFR 103.2(b)(8) 与征信授权条款按原文
写足。**这次到期在抓取侧没有留下任何痕迹** —— 公告一字未改、`cur` 本就是
08/24/26、`also` 本就是空的，已把这个观察补记入第一节 A2 末尾。
其余中文要点按当天日期逐条核过，过期的一条都没有：I-485 已是兑现后的写法且面板
`cur` 为 09/18/26、`also` 为空与之相符，I-129 的两版并行到 11 月 9 日与面板原文
`Starting Nov. 9, 2026` 相符，I-765／I-539 与禁令公告原文逐字一致。
面板原文另逐字对了一遍：G-28 与 I-918 的「即将发布」（`We will publish a new edition
of this form soon`）均未变，I-693 的签字日规则、G-1145 的 `You can also use previous
editions`、G-1450 的 `We will also accept prior editions`、I-912 的
`prior editions (or a written request)` 与各自要点逐字相符。
26 个表格 `up` 全部为空、`soon` 全部为假，I-765／I-539 的 `up: ""` 覆盖经第十二轮
抓取仍然生效；`cn` 齐备（26/26），`up` 非空却没有中文要点的表格 0 个。
只改了 `notes.yaml` 的两条 `note`（未动 `cn`／`soon`／`up`），已 `--rebuild`
重新生成网页，未改任何代码逻辑。

2026-09-30 的核对方式：先按 md5 比对 `audit-alerts.json`，**09-19 至今十一天的文件逐字节
相同**（md5 仍是 `67f3c752…`）；`forms.json` 与前一日的差异只有 `generated_at` 一行、
`docs/index.html` 只有页脚的检查时间一行（均已 `git diff` 逐行确认），即 26 个表格的
`cur`／`also`／`up` 十一天没动过。再独立重跑正反向扫描而非引用前几日的结论 ——
先用规则本身（含 `edition` 且含 mm/dd/yy）对 35 条重跑一遍并逐条与 `kept` 比对，
**规则判定与 `kept` 完全一致，无一条错位**；未命中的 27 条中**含 mm/dd/yy 的 0 条**，
含 `edition` 的仍是 I-90／I-129F／I-601A 那条逐字相同的通用提交提醒（各 799 字符），
均为泛指。反向扫描在历次词表上再加 `do not use|will not be accepted|latest edition|
form version|older version|outdated|re-issued|last day|final day|until further notice|
indefinitely|form has been (updated|revised)|newly (revised|published)|effective date|
mandatory`，**触发 0 条** —— 这是历次反向扫描里第一次一条都没触发的词表，
说明「换版」这件事在 USCIS 的措辞里始终绕不开 `edition` 一词。
历次词表整体重扫触发的仍是那 7 条（I-131 乌克兰再假释窗口与 I-821D 的 DACA 三条命中
`expire`，讲的是身份与工卡的有效期；I-90 那条讲绿卡须保持有效；G-1450 那条命中
`no longer accept`，讲的是不再收支票；I-589 提交地点变更那条同时命中 `grace period`
与 `will reject`，讲的却是收件地址的 30 天缓冲），全部落在第二节已记的十二类里，
挡下都是对的。`edition` 后跟英文日期与 ISO 日期的写法仍是一条都没有。
命中的 8 条逐条复看，A1 一条（I-485，兑现形态）、A2 两条、A3 一条、A4 一条、A5 一条、
A6 两条，归类不变，无误报无漏报。无截断，最长仍为 2310 字符（HR-1 费用暂停公告），
余量 4.3 倍；Edition Date 原文最长 315 字符（I-693），余量 19 倍。

另按当天日期逐条核了中文要点的时效：**过期的一条都没有，但有一条今天到期**——
I-864／I-864A 写的是「旧版 10/17/24 的宽限期到 9 月 30 日为止，自 10/01/26 起只接受
08/24/26 版」，公告原文是 `USCIS will not process any 10/17/24 edition … postmarked or
electronically submitted on or after Oct. 1, 2026`，**以邮戳或电子提交日计，今天 9 月 30 日
是旧版可用的最后一天，要点今天仍然准确，所以本轮不改**；把首句改成「现在只接受
08/24/26 版」今天反而是错的。明天那轮复核须把这两条的首句改写为换版已兑现的说法
（面板 `cur` 本就已是 08/24/26、`also` 为空，旧版的可用性只写在公告里，
所以换版当天抓取侧不会有任何变化，`changed` 仍会是 0 —— 这两条要点只能靠日期去核）。
其余时间点：I-129 的 11 月 9 日还有 40 天，I-485 已是换版兑现后的写法且面板
`cur` 为 09/18/26、`also` 为空与之相符，I-765／I-539 与禁令公告原文逐字一致。
面板原文另逐字对了一遍：G-28 与 I-918 的「即将发布」（`We will publish a new edition
of this form soon`）均未变，I-693 的签字日规则、G-1145 的 `You can also use previous
editions`、G-1450 与 I-912 的 `also accept prior editions` 与各自要点逐字相符。
26 个表格 `up` 全部为空、`soon` 全部为假，I-765／I-539 的 `up: ""` 覆盖经第十一轮抓取
仍然生效；`cn` 齐备（26/26），`up` 非空却没有中文要点的表格 0 个；抓取 26/26 成功，
`changed` 为 0，无 `error`。
按第四节第 1 点抽出 `kept` 里的强制切换日与当天比对：I-485 的 9 月 18 日已过且
`cur` 已是 09/18/26（相符），I-864／I-864A 的 10 月 1 日、I-129 的 11 月 9 日均未到，
**「切换日已过但 `cur` 未变」的情形未出现**。
未改 `notes.yaml` 与任何代码逻辑，无需重新生成网页。

2026-09-29 的核对方式：先按 md5 比对 `audit-alerts.json`，**09-19 至今十天的文件逐字节
相同**（md5 仍是 `67f3c752…`）；`forms.json` 与前一日的差异只有 `generated_at` 一行
（已 `git diff` 逐行确认），即 26 个表格的 `cur`／`also`／`up` 十天没动过。
再独立重跑正反向扫描而非引用前几日的结论 —— 先用规则本身（含 `edition` 且含 mm/dd/yy）
对 35 条重跑一遍，逐条与 `kept` 比对，**规则判定与 `kept` 完全一致，无一条错位**；
未命中的 27 条中**含 mm/dd/yy 的 0 条**，含 `edition` 的仍是 I-90／I-129F／I-601A
那条逐字相同的通用提交提醒（各 799 字符），均为泛指。
反向扫描在历次词表上再加 `must (now )?use|required to use|no longer valid|expire|
revision date|print date|edition dated|takes? effect|becomes effective|supersede|
new printing|we (have )?(updated|revised) the form|use the (latest|current)|
preview version|transition (to|period)`，触发的 7 条逐条看过，全部落在第二节已记的
十二类里（I-131 乌克兰再假释窗口与 I-821D 的 DACA 三条命中 `expire`，讲的是身份与工卡
的有效期而非表格版本；I-90 那条命中的是「绿卡须保持有效」；I-589 提交地点变更那条
同时命中 `grace period` 与 `will reject`，讲的是收件地址的 30 天缓冲，与版本无关 ——
这条每次都值得重看一遍，它是「同样的措辞讲别的事」最典型的一例），挡下都是对的。
`edition` 后跟英文日期与 ISO 日期的写法仍是一条都没有，即 USCIS 至今只用 mm/dd/yy
写版本号。命中的 8 条逐条复看，A1 一条（I-485，兑现形态）、A2 两条、A3 一条、
A4 一条、A5 一条、A6 两条，归类不变，无误报无漏报。无截断，最长仍为 2310 字符
（HR-1 费用暂停公告），余量 4.3 倍；Edition Date 原文最长 315 字符（I-693），余量 19 倍。
另按当天日期逐条核了中文要点的时效：**过期的一条都没有** —— I-864／I-864A 的
10 月 1 日还有 2 天（写的是「旧版 10/17/24 的宽限期到 9 月 30 日为止」，今天仍成立，
9 月 30 日是可用的最后一天），I-129 的 11 月 9 日还有 41 天，I-485 已是换版兑现后的
写法且面板 `cur` 为 09/18/26、`also` 为空与之相符，I-765／I-539 与禁令公告原文一致。
面板原文另逐字对了一遍：G-28 与 I-918 的「即将发布」（`We will publish a new edition
of this form soon`）均未变，I-693 的签字日规则、G-1145 的 `You can also use previous
editions`、G-1450 与 I-912 的 `also accept prior editions` 与各自要点逐字相符。
26 个表格 `up` 全部为空、`soon` 全部为假，I-765／I-539 的 `up: ""` 覆盖经第十轮抓取
仍然生效；`cn` 齐备（26/26），`up` 非空却没有中文要点的表格 0 个；抓取 26/26 成功，
`changed` 为 0，无 `error`。
按第四节第 1 点抽出 `kept` 里的强制切换日与当天比对：I-485 的 9 月 18 日已过且
`cur` 已是 09/18/26（相符），I-864／I-864A 的 10 月 1 日、I-129 的 11 月 9 日均未到，
**「切换日已过但 `cur` 未变」的情形未出现**。
未改 `notes.yaml` 与任何代码逻辑，无需重新生成网页。

2026-09-28 的核对方式：先按 md5 比对 `audit-alerts.json`，**09-19 至今九天的文件逐字节
相同**（md5 仍是 `67f3c752…`）；`forms.json` 与前一日的差异只有 `generated_at` 一行
（已 `git diff` 逐行确认），即 26 个表格的 `cur`／`also`／`up` 九天没动过。
再独立重跑正反向扫描而非引用前几日的结论 —— 未命中的 27 条中**含 mm/dd/yy 的 0 条**，
含 `edition` 的仍是 I-90／I-129F／I-601A 那条逐字相同的通用提交提醒，均为泛指；
反向扫描在历次词表上再加 `replac(e|ed|es|ing)|sunset|phase(d)? out|withdrawn from use|
form dated|(begin|start) using|stop accepting`，以及 `edition` 后二十字符内跟英文日期的
写法（用来验证版本号若改用 `edition date: Sept. 18, 2026` 这类文字日期不会漏）和
`yyyy-mm-dd` 这种 ISO 日期格式，触发的 4 条逐条看过，全部落在第二节已记的十二类里
（通用提交提醒三处命中 `edition`、G-1450 缴费方式命中 `no longer accept`），与版本无关，
挡下是对的；`yyyy-mm-dd`、`mm/dd/yyyy` 与文字日期版本号一条都没有，即 USCIS 至今只用
mm/dd/yy 写版本号。命中的 8 条逐条复看，A1 一条（I-485，兑现形态）、A2 两条、A3 一条、
A4 一条、A5 一条、A6 两条，归类不变，无误报无漏报。无截断，最长仍为 2310 字符
（HR-1 费用暂停公告），余量 4.3 倍。
另按当天日期逐条核了中文要点的时效：**过期的一条都没有** —— I-864／I-864A 的
10 月 1 日还有 3 天（写的是「旧版 10/17/24 的宽限期到 9 月 30 日为止」，今天仍成立；
9 月 30 日仍是可用的最后一天，**10 月 1 日当天这两条即刻过时，届时要改写成只接受
08/24/26 版**）、I-129 的 11 月 9 日还有 42 天，I-485 已是换版兑现后的写法且面板
`cur` 为 09/18/26、`also` 为空与之相符，I-765／I-539 与禁令公告原文一致。
面板原文另逐字对了一遍：G-28（`We will publish a new edition of this form soon`，
09/17/18 与 05/23/18 并列）、I-918（同一措辞，01/20/25）的「即将发布」均未变，
I-693 的签字日规则、G-1145 的 `You can also use previous editions`、
I-912 的 `prior editions (or a written request)` 与各自要点逐字相符。
`up` 字段逐个核过：26 个表格当前全部为空，`soon` 全部为假，I-765／I-539 的 `up: ""`
覆盖在又经过一轮抓取后仍然生效。26 个表格的 `cn` 全部齐备，有 `up` 却无要点的表格 0 个。
第三节那条「切换日已过、`cur` 却未变」的时间维度边界情况本轮未出现：按第四节第 1 点
的思路把 kept 里的 `on or after`／`Beginning`／`Starting` 日期全抽出来与当天比对，
只有 I-485 的 9 月 18 日已过，而它的 `cur` 正是 09/18/26，对得上。

2026-09-27 的核对方式：先按 md5 比对 `audit-alerts.json`，**09-19 至今八天的文件逐字节
相同**（md5 仍是 `67f3c752…`）；`forms.json` 与前一日只差生成时间戳，即 26 个表格的
`cur`／`also`／`up` 八天没动过。再独立重跑正反向扫描而非引用前几日的结论 ——
未命中的 27 条中**含 mm/dd/yy 的 0 条**，含 `edition` 的仍是 I-90／I-129F／I-601A
那条逐字相同的通用提交提醒，均为泛指；反向扫描在历次词表上再加
`form has been (revised|updated)|newly revised|as of [月] [日], [年]|[月] [日], [年] edition`
以及 `mm/dd/yyyy` 这种四位年份的日期格式（用来验证版本号若改用别的日期写法不会漏），
触发的 9 条逐条看过，全部落在第二节已记的十二类里（HR-1 费用暂停三处、BIA 先例、
通用提交提醒三处、G-1450 缴费方式、I-918 配额用尽），与版本无关，挡下是对的；
`mm/dd/yyyy` 一条都没有，即 USCIS 至今没有用四位年份写过版本号。命中的 8 条逐条复看，
A1 一条（I-485，兑现形态）、A2 两条、A3 一条、A4 一条、A5 一条、A6 两条，归类不变，
无误报无漏报。无截断，最长仍为 2310 字符（HR-1 费用暂停公告，挂在 I-131／I-765／I-589
三处），余量 4.3 倍。
另按当天日期逐条核了中文要点的时效：**过期的一条都没有** —— I-864／I-864A 的
10 月 1 日还有 4 天（写的是「旧版 10/17/24 的宽限期到 9 月 30 日为止」，今天仍成立，
**10 月 1 日当天这两条就会过时，届时要改写成只接受 08/24/26 版**）、I-129 的 11 月 9 日
还有 43 天，I-485 已是换版兑现后的写法，I-765／I-539 与禁令公告原文一致，
G-28／I-918 的「即将发布」面板原文未变，G-1145／I-912 的旧版表述与面板逐字相符，
I-693 的签字日规则与面板逐字相符，其余无时间点。
`up` 字段逐个核过：26 个表格当前全部为空，`soon` 全部为假，I-765／I-539 的 `up: ""`
覆盖在又经过一轮抓取后仍然生效。26 个表格的 `cn` 全部齐备。
第三节那条「切换日已过、`cur` 却未变」的时间维度边界情况本轮未出现：按第四节第 1 点
的思路把 kept 里的 `on or after`／`Beginning`／`Starting` 日期全抽出来与当天比对，
只有 I-485 的 9 月 18 日已过，而它的 `cur` 正是 09/18/26，对得上。

2026-09-26 的核对方式：先按 md5 比对 `audit-alerts.json`，**09-19 至今七天的文件逐字节
相同**（md5 `67f3c752…`，09-20 至 09-25 六天无人复核，一并核过）；`forms.json` 除生成时间戳
与 I-485 那条要点文本外内容也未变，即 26 个表格的 `cur`／`also`／`up` 七天没动过。
再独立重跑正反向扫描而非引用前几日的结论 —— 未命中的 27 条中**含 mm/dd/yy 的 0 条**，
含 `edition` 的仍是 I-90／I-129F／I-601A 那条逐字相同的通用提交提醒，均为泛指；
反向扫描在历次词表上再加 `must use the|no longer valid|expired edition|use the new|
form version|updated to reflect|new edition of this form|do not use|invalid edition|
current version|correct edition|latest form|form edition`，触发的仍只是上面那条通用提交
提醒的三份副本（`form edition`，且不含任何 mm/dd/yy），挡下是对的。命中的 8 条逐条复看，
A1 一条（I-485，兑现形态）、A2 两条、A3 一条、A4 一条、A5 一条、A6 两条，归类不变，
无误报无漏报。无截断，最长仍为 2310 字符（HR-1 费用暂停公告），余量 4.3 倍。
另按当天日期逐条核了中文要点的时效：**过期的一条都没有** ——
I-864／I-864A 的 10 月 1 日（还有 4 天，是眼下最近的一个硬性切换日）、I-129 的 11 月 9 日
均未到，I-485 已是换版兑现后的写法，I-765／I-539 与禁令公告原文一致，
G-28／I-918 的「即将发布」面板原文未变，I-693 的签字日规则与面板逐字相符，其余无时间点。
`up` 字段逐个核过：26 个表格当前全部为空，I-765／I-539 的 `up: ""` 覆盖在又经过六轮抓取
后仍然生效（09-17 那条边界情况确认修好，不是只在当天有效）。26 个表格的 `cn` 全部齐备。
第三节那条「切换日已过、`cur` 却未变」的时间维度边界情况本轮未出现。

2026-09-19 的核对方式：先按 md5 比对 `audit-alerts.json`，与 09-18 只差 I-485 那一条
（其余 34 条逐字节相同）；再独立重跑正反向扫描而非引用前几日的结论 —— 未命中的 27 条中
**含 mm/dd/yy 的 0 条**，含 `edition` 的仍是 I-90／I-129F／I-601A 那条逐字相同的通用
提交提醒，均为泛指；反向扫描在历次词表上再加
`rescind|withdraw|effective immediately|as of [月] [日]|discontinue|retire|edition date`，
命中的 10 条逐条看过，全部落在第二节已记的十二类里（HR-1 费用暂停三处、BIA 先例、
通用提交提醒三处、G-1450 缴费方式、I-589 提交地点变更、I-918 配额用尽），与版本无关，
挡下是对的。命中的 8 条逐条复看，A1 一条（I-485，已改写成兑现形态）、A2 两条、
A3 一条、A4 一条、A5 一条、A6 两条，归类不变，无误报无漏报。
无截断，最长仍为 2310 字符（HR-1 费用暂停公告），余量 4.3 倍。
另按当天日期逐条核了中文要点的时效：I-485 已过期并改写（见下），
I-864／I-864A 的 10 月 1 日、I-129 的 11 月 9 日均未到，其余无时间点。
`up` 字段逐个核过：26 个表格当前全部为空，I-765／I-539 的 `up: ""` 覆盖经过一轮
抓取后仍然生效（09-17 那条边界情况已修好），I-485 因新版已成为 `cur`、
公告里不再有晚于它的日期而自然归零，没有需要覆盖的。

2026-09-18 的核对方式：先按 md5 比对 `audit-alerts.json`，与 09-16、09-17 逐字节相同
（35 条公告一条没变）；再独立重跑正反向扫描而非引用前几日的结论 —— 未命中的 27 条中
**含 mm/dd/yy 的 0 条**，含 `edition` 的仍是 I-90／I-129F／I-601A 那条逐字相同的通用
提交提醒，均为泛指；反向扫描在历次词表上再加
`updated the form|version of (the )?form|reissue|republish`，唯一命中的仍是 G-1450
那条讲缴费方式的公告，与版本无关，挡下是对的。命中的 8 条逐条复看，A1 一条（I-485）、
A2 两条、A3 一条、A4 一条、A5 一条、A6 两条，归类不变，无误报。无截断，最长仍为
2310 字符（HR-1 费用暂停公告），余量 4.3 倍。
另按当天日期逐条核了中文要点的时效：I-485 的 09/18 到期（见下），I-864／I-864A 的
9 月 30 日、I-129 的 11 月 9 日均未到期，其余无时间点。

2026-09-17 的核对方式：先按 md5 比对 `audit-alerts.json`，与 09-16 逐字节相同
（35 条公告一条没变）；仍按惯例独立重跑一遍正反向扫描而非引用前一日的结论 ——
未命中的 27 条中**含 mm/dd/yy 的 0 条**，含 "edition" 的仍是 I-90／I-129F／I-601A
那条逐字相同的通用提交提醒；反向扫描在历次词表上再加 `is not accepting|
postponing the effective|enjoin`（A6 的三个判别信号，用来验证同类公告不会漏），
未命中的公告里 0 条触发。命中的 8 条归类不变（A1 一条、A2 两条、A3 一条、A4 一条、
A5 一条、A6 两条）。最长仍为 2310 字符，无截断。

**本轮的发现同样不在筛选规则**，而在显示：昨天给 I-765／I-539 写的 `up: ""` 覆盖
被当天的抓取顶掉了，见第三节最后一条。

2026-09-16 的核对方式：35 条全部通读。未命中的 27 条中**含 mm/dd/yy 的 0 条**，
含 "edition" 的仍是 I-90／I-129F／I-601A 那条逐字相同的通用提交提醒；反向扫描在
历次词表上再加 `newer version|reissued|new printing|updated edition|version of the form|
publish a revised|publish a new`，唯一命中的仍是 G-1450 那条讲缴费方式的公告，挡下是对的。
命中的 8 条仍是 8 条，但**构成变了**：I-765／I-539 原先的两条 A1 被同一条 A6 法院公告
整条替换（A1 因此从 3 条降为 1 条，只剩 I-485），A6 新增 2 条。归类后为
A1 一条、A2 两条、A3 一条、A4 一条、A5 一条、A6 两条，无误报、无漏报。
最长仍为 2310 字符（HR-1 费用暂停公告，现记在 I-131 名下），无截断。

**本轮的重点不在筛选规则**（规则一如既往地正确命中），而在两处下游问题：
A6 公告的跨表格日期污染了 I-539 的 `up`（第三节），以及两张表的中文要点因禁令
而彻底失效（原要点会让员工去用一个 USCIS 明确不接受的版本）。

2026-09-15 的核对方式：先按 md5 逐日比对 `audit-alerts.json`，确认 09-11 至 09-15
五天的文件逐字节相同（09-13、09-14 无人复核，一并核过）；再独立重跑一遍正反向扫描
而非直接引用前几日的结论 —— 未命中的 26 条中**含 mm/dd/yy 的 0 条**，含 "edition"
的仍是 I-90／I-129F／I-601A 那条逐字相同的通用提交提醒（各 6 次，均为泛指）；
反向扫描在原有词表上再加 `new form|updated version|replaces the|prior edition|previous edition`，
唯一命中的仍是 G-1450 那条讲缴费方式的公告，与版本无关，挡下是对的。
命中的 8 条逐条复看，A1 三条、A2 两条、A3 一条、A4 一条、A5 一条，归类不变，无误报。
全部 34 条均未触发截断，最长仍为 2310 字符（HR-1 费用暂停公告），余量 4.3 倍。

2026-09-12 的核对方式同前：未命中的 26 条中**含 mm/dd/yy 的 0 条**，含 "edition"
的 3 条仍是那条逐字相同的通用提交提醒；反向扫描在原有措辞外又加了
`updated form|current edition|supersede|no longer accept|will only accept|accept only|obsolete`
等词，唯一命中的是 G-1450 那条讲**缴费方式**的公告（`no longer accepts payments
made by personal or business check`），与版本无关，规则挡下是对的。
当日 `audit-alerts.json` 与前一日逐字节相同，即官网 34 条公告一条没变。

2026-09-11 的核对方式：逐条检查未命中的 26 条，**含 mm/dd/yy 的 0 条**，
含 "edition" 的 3 条全是那条逐字相同的通用提交提醒（各出现 6 次 "edition"，
均为泛指，无版本日期）。反向检查也做了：用
`revised form|new version|revised edition|new edition|latest edition` 等
不含 "edition" 一词也可能表达换版的措辞去扫未命中的公告，**命中 0 条** ——
即目前还没有出现"用别的说法讲换版"的公告。

### 为什么两个条件缺一不可

- **只看 "edition"**：I-90 那条通用提醒里 "edition" 出现了五次，全是泛指，
  会误报。
- **只看日期**：费用类、诉讼类公告大量出现日期（多为 `Sept. 9, 2026` 这类
  英文写法，但也有例外），会误报。

英文日期写法（`Aug. 31, 2026`）不参与匹配，这是刻意的 —— 版本号在 USCIS
体系里一律用 mm/dd/yy 表示，用格式本身就能把"版本号"和"事件日期"区分开。

### 已知的边界情况

- **G-28**：公告区为空，但 Edition Date 面板里写着 "We will publish a new
  edition of this form soon"（无日期）。这类"无日期预告"由面板原文覆盖，
  不需要公告补充。
- **I-864／I-864A**：公告里的 10/17/24 早于当前版本 08/24/26，是仍被接受的旧版而非
  新版。因此 `build.py` 里只把**晚于当前版本**的日期认定为预告。

- **G-1450／I-912**：面板只写 `We will also accept prior editions`
  （I-912 还多一句 `or a written request`）而不给具体日期，逐日期提取会提不出
  "也接受的版本"，把多版本表格误标成单一版本。`build.py` 认得这个表述，
  记为「全部旧版」。**这不是异常**，见 A5。

- **G-1145：同一件事的第三种措辞，目前没被认出**（2026-09-12 复核发现）。
  面板写的是 `You can also **use** previous editions`，动词是 `use` 而不是
  `accept`，主语是申请人而不是 USCIS。`build.py:61` 的正则
  `accept (all )?(prior|previous) editions` 要求 `accept`，因此匹配不上，
  G-1145 被记成单一版本（`also` 为空），页面显示与官网原文矛盾。

  这正是上一条想防住的误标，只是换了个说法就漏了过去。已在 `notes.yaml`
  给 G-1145 补了中文要点说明实情；正则是否放宽到
  `(accept|use) (all )?(prior|previous) editions` 留给人决定，见复核 Issue。

  **教训与筛选规则那边一致**：USCIS 的措辞模板并不统一（A4 用 `Until then`
  代替 `grace period` 是同一类问题），凡是靠单一动词或单一关键词识别的地方，
  都要假定迟早会出现同义的另一种写法。

- **A1 公告的强制换版日已到，官网却还没换版**（2026-09-15 复核发现，
  I-765 与 I-539 同时出现）。两张表的公告都写着「On Sept. 15, 2026, we **will**
  publish a revised edition …（edition date: 09/15/26）」并规定 9 月 15 日当天
  及以后邮戳／电子提交的旧版一律退件；但当天美东 9:13 抓取时，
  面板仍是 08/21/25／08/28/24，公告一字未改仍为将来时，新版只有预览版。

  也就是说：**公告规定的退件日已经到了，官网的"当前版本"却还停在旧版**。
  抓取侧一切正常（`cur` 未变、`up` 仍为 09/15/26、`changed` 为 0），
  异常只存在于「公告写的时间」与「今天是几号」之间 —— 任何只比对快照差异的
  检查都发现不了，必须拿当天日期去读公告里的日期。

  这是**时间维度**的边界情况，与前几条的措辞维度不同。可能的原因（USCIS 当天
  晚些时候才发布、公告与页面不同步、换版被推迟）都需要人工向官网核实，
  **不要替使用者推断今天该用哪一版**。已在 `notes.yaml` 给两张表的中文要点
  写明「官网状态对不上、交件前先确认」，并开复核 Issue 提请人工判断。

  **给后续自动化的提示**：第四节第 1 点抽出强制切换日之后，值得顺手加一条
  「切换日已过、但 `cur` 仍等于旧版」的对账检查 —— 这正是本条想防住的情形。

  **2026-09-16 后续**：谜底揭晓 —— 换版在生效前一天（9 月 14 日）被马萨诸塞州
  联邦地区法院的禁令拦下了，见第一节 A6。当时列的三种可能一种都没中，
  这恰好印证了「不要替使用者推断今天该用哪一版」这条原则：按公告字面推断的话，
  会得出「用 09/15/26 版」这个与官网现在的说法正相反的结论。
  上面那条对账检查仍然值得做，但输出只能是「报出来让人看」，不能是自动结论。

  **2026-09-18 第二次出现，这次是 I-485**：公告写「On Sept. 18, 2026, USCIS will
  publish a revised edition …（edition date: 09/18/26）」，规定当天及以后邮戳／电子
  提交的 01/20/25 与 09/04/26 两版一律退件；当天美东 9:13 抓取时，面板仍是
  09/04/26（也接受 01/20/25），公告仍为将来时，新版只有预览版。与 09-15 那次
  逐项对应，连抓取侧的表现都一样（`cur` 未变、`up` 仍为 09/18/26、`changed` 为 0）。

  **2026-09-19 后续：这次的答案是「官网晚了一天」**。09-19 抓取时 I-485 的面板已更新为
  09/18/26、`also` 清空，那条 A1 也已就地改写成已发布的措辞（见第一节 A1 末尾）。
  也就是说同一个现象在 I-765／I-539 那次的成因是换版被法院拦下（A6），
  在 I-485 这次只是页面更新滞后了一天 —— **成因不唯一，看到这个现象时无法从现象本身
  反推原因**，这恰好再次说明当天不替使用者推断「今天该用哪一版」是对的。
  对第四节第 1 点那条对账检查的要求也随之明确：它只能报出「切换日已过但 `cur` 未变」
  这个事实并提请人看，不能附带任何成因结论。

  三天内在两组表格上各出现一次，**这已经不是偶发**：USCIS 的换版公告写的是计划，
  页面更新未必当天跟上。因此第四节第 1 点那条对账检查的优先级应当提高 ——
  它是唯一能自动发现这种情形的手段，而每次都只能靠人拿当天日期去读公告。
  与 09-15 那次的区别在于：I-485 这次 `up` 提取没有出错（09/18/26 确实是公告
  指定的新版，不像 I-765／I-539 那样被法院叫停），所以**不应该用 `up: ""` 覆盖** ——
  页面上的「即将换版 09/18/26」与官网说法一致，需要修正的只是中文要点的时态。

- **跨表格日期串号：一条公告写了两张表的版本号，`up` 提错了**
  （2026-09-16 复核发现，I-539）。A6 那条法院公告同时挂在 I-765 和 I-539 页首，
  且原文里同时出现三个版本号：`08/28/24`（I-539 的）、`08/21/25`（I-765 的）、
  `09/15/26`（两张表共同的、被叫停的新版）。

  `build.py` 的 `upcoming` 只做两件事：从公告里提所有 mm/dd/yy，去掉已知的
  `cur`／`also`，留下比 `cur` 晚的。对 I-539 来说 `cur` 是 `08/28/24`，于是
  **I-765 的当前版本 `08/21/25` 被当成了 I-539 的新版预告**（2025 年晚于 2024 年），
  还排在 `09/15/26` 前面被取为 `up`。Actions 据此开了一条 Issue #6
  「I-539 公告新版：08/28/24 → 08/21/25」，通知员工去准备一个根本不存在的版本。

  **根因**：日期提取是**按表格页面**做的，但公告内容是**跨表格共享**的
  （第二节早就记过「同一条公告原样挂在多个表格页上」，当时只当作条数膨胀的问题，
  没想到它还会污染日期提取）。公告里的日期未必属于当前这张表。

  **可能的修法**（不自行改动，留给人决定）：提日期时要求同一句里出现本表格号，
  例如把 `Form I-539` 附近的日期才算数；或者在 `is not accepting` 这类否定语境
  出现时干脆不提 `up`。两种都需要人判断取舍，见复核 Issue。

  **与 G-1145 那条的区别**：G-1145 是措辞没覆盖导致**漏**认，这条是跨表格污染导致
  **误**认，方向相反，但教训一致 —— 纯正则提取不理解「这个日期是谁的」。

- **页首公告的先后顺序会被官网调换，文本却一字未改**（2026-10-07 复核发现，I-485）。
  那天 I-485 的两条公告在页面上换了位置：9 月 18 日那条（A1 兑现形态）移到了
  9 月 4 日 Casa 禁令那条（A3）之前。抓取按页面顺序存数组，于是
  `audit-alerts.json` 与 `forms.json` 里 I-485 的 `alerts` 顺序跟着变了，
  **两条文本逐字节相同**，`cur`／`also`／`up` 一个没动。

  **影响的是复核方法而不是数据**：历次复核都拿 `audit-alerts.json` 的 md5 当第一道
  快筛，「md5 没变」确实能证明公告一个字没改，但反过来**「md5 变了」不等于内容有
  变动** —— 纯顺序调换就足以让 md5 变掉。这次 md5 变了之后 `git diff` 看出来的两类
  差异里，只有一类（两条新增公告）是真的，另一类纯粹是顺序。

  **做法**：md5 只当「要不要去 diff」的开关，不当结论；真正的判断要么逐行 diff，
  要么把公告按文本排序后再比。顺带一提，`build.py` 判 `cur`／`also`／`up`
  与 `scraper.py` 的筛选都不依赖公告顺序，所以这件事对页面显示和通知没有影响。

- **跨表格复用的同一条公告会各自漂移，「两张表逐字相同」不是稳定事实**
  （2026-10-08 复核发现）。USCIS 今天对三处公告做了纯文本润色，没有一处改变含义，
  但每一处都只改了**一部分**页面：

  | 公告 | 改动 | 结果 |
  | --- | --- | --- |
  | A6 法院公告（I-765／I-539） | `On Sept.14, 2026` → `On Sept. 14, 2026`（补一个空格） | **只改了 I-765**，I-539 仍是 `Sept.14`，两张表不再逐字相同（1124 / 1123 字符） |
  | 通用提交提醒（I-90／I-129F／I-601A） | `The current acceptable edition can be found under …` → `You can find the current acceptable edition under …` | **只改了 I-90**（792 字符），I-129F 与 I-601A 仍是原措辞（各 799 字符） |
  | 代理人变动通知（I-360） | `See Web Alert` → `See the Web Alert` | 该公告只此一处，无对照 |

  **为什么要记**：第二节早就记过「同一条公告原样挂在多个表格页上」，历次复核也
  一再把「两张表逐字相同」当成结论写进记录（10-07 那轮还专门程序比对确认过
  I-765／I-539 的 A6 一致）。今天证明那只是**当时的巧合**：同一条公告在不同表格页上
  是各自独立的副本，USCIS 改一处不保证改全部。

  **影响仅限复核方法，不影响数据**：三处改动都没有改变语义，`kept` 仍是 8 条
  （A6 含 `edition` 与 mm/dd/yy，补一个空格不影响命中），`cur`／`also`／`up`
  一个没动，通用提交提醒仍然是泛指、仍被正确挡在 `kept` 之外。但有两点要跟着改：
  一是**按文本去重的条数会无故变动**（今天 47 条去重后 43 条，I-765／I-539 的 A6
  与 I-90 的提醒各自从「复用」变成了「独有」），去重数的变化不能当成新增公告的信号；
  二是**不能再用「和另一张表逐字相同」来省掉逐条通读**，每张表的副本都得自己核。

  **与前几条的关系**：G-1145 是措辞没覆盖导致漏认，跨表格日期串号是日期归属错导致
  误认，顺序调换是 md5 失真，这一条是**同一条公告的多个副本各自演化** ——
  四条都指向同一件事：USCIS 的页面文本没有任何一致性保证，
  凡是把「两处相同」当前提的做法都迟早会失效。

- **人工覆盖只挡住了日期、没挡住标记，第二天被抓取顶回来**
  （2026-09-17 复核发现，I-765／I-539）。09-16 给 `build.py` 加了「`notes.yaml` 写了
  `up` 就以它为准」的覆盖，写 `up: ""` 即可去掉预告标记；当天 `--rebuild` 生成的页面
  确实是对的。但第二天 09:05 的定时抓取把标记又加了回来：两张表重新带上
  「即将换版」标记（因为 `up` 为空，标记后面连日期都没有），而 USCIS 明说
  `is not accepting` 这一版。

  **根因是两条代码路径不一致**：`rebuild()` 按 `up` 判 `soon`，`merge()`（抓取那条路）
  却仍按公告里提出来的 `upcoming` 判，于是覆盖只在重新生成网页时有效，一抓取就失效。
  本次已把 `merge()` 改成同样按 `up` 判。没写覆盖的表格 `up` 恒等于
  `upcoming[0]`，行为与改动前完全一致（26 个表格实测只有 I-765／I-539 两条变化）。

  **教训**：人工覆盖机制只有在**每条路径上都生效**才算数。凡是加「让人能改掉自动
  判断」的开关，都要顺着抓取、重新生成两条路各走一遍，否则覆盖会被下一轮抓取
  悄悄抹掉 —— 页面还会显得一切正常，因为标记本来就是自动加的。

---

## 四、后续自动化的着手点

按投入产出排序：

1. **抽取强制切换日**（价值最高）。A1/A2 的措辞极其模板化，
   `on or after ([A-Z][a-z]+\. \d{1,2}, \d{4})` 和
   `Beginning ([A-Z][a-z]+\. \d{1,2}, \d{4})` 两个正则就能覆盖已观察到的全部
   案例。拿到这个日期后可以做倒计时提醒（"距 I-765 强制换版还有 6 天"），
   比单纯的"有更新"有用得多。

   **前置条件：这个抽取只能在已命中筛选的公告（`kept`）上做，不能对 `all` 做。**
   2026-10-01 新增的 FY2027 费用调整公告写着
   `Any request postmarked on or after Oct. 16, 2026 without the proper filing fee
   will be rejected` —— 句式与换版切换句一模一样，讲的是费用。
   对 `all` 跑上面那个正则，会凭空得出一个 10 月 16 日的「换版日」
   （见第二节末的三例对照）。筛选规则是这一点的前提，不是可以绕过的一步。

   **还要顺带报出 A2 到期**（2026-10-01 的教训，见第一节 A2 末尾）。
   A2 兑现时抓取侧三处（公告文本、`cur`、`also`）一处都不动，所以这条检查
   不能只报「切换日已过但 `cur` 未变」那一种矛盾 —— 对 A2 来说 `cur` 本来就不该变。
   它还得能报「切换日已过、而公告措辞仍是现在时」，那才是 A2 到期的唯一信号，
   也是中文要点需要改写的触发点。输出仍然只能是报出来让人看，不能附带结论。

2. **区分有无宽限期**。原先以为检测 `no grace period` 与 `grace period` 即可，
   **A4 推翻了这个想法**：I-129 有 61 天并行期，公告里却一次 `grace period`
   都没出现，只写 `Until then`。关键词法会把它误判成"无宽限期"，
   提醒的紧急程度正好反了。

   可行的做法是先按第 1 点抽出强制切换日，再与公告发布日／当前版本日期比大小：
   两者不同就是有并行期，差几天就是几天。措辞可以变，日期算术不会骗人。
   `no grace period` 仍可作为**加强**信号（A1 的三个表格都明写了），
   但它的缺席不能反推成"有宽限期"。

   **A5 又给这条加了一个前提**：抽不到切换日时有两种可能 ——
   一是公告明说旧版继续有效（A5，`continue/also accept prior editions`），
   二是正则没覆盖到某种新措辞。两者必须区分：前者是"没有截止日"，
   后者是"没抽出来"。做法是先判 A5 的表述，命中就直接结论为无截止日；
   只有既非 A5、又抽不到日期时，才当作抽取失败报出来让人看。
   **不能把"抽不到日期"一律当成无截止日**，那会漏掉真正的强制换版。

3. **识别诉讼影响**。出现 `injunction`、`court`、`vacatur` 时给公告加一个
   醒目标记，提示"此版本适用性存在争议，需人工判断"。**不要试图自动解释
   法律效果。**

### 一条原则

自动化只做**提取**，不做**判断**。
版本号、日期、有无宽限期这类事实可以抽取；"你该用哪一版"必须留给人，
因为 A3 那种情况足以让任何规则失效。中文要点写在 `notes.yaml` 里，
由人维护，页面同时展示公告原文供核对。

---

## 文本长度

抓取时对公告和 Edition Date 原文都设了长度上限，作用是防止页面结构变化时
把整页内容抓进来，不是为了省空间：

| | 实测最长 | 上限 | 余量 |
| --- | --- | --- | --- |
| 公告 | 2310 字符（I-765，2026-09-11） | 10000 | 约 4.3 倍 |
| Edition Date 原文 | 315 字符（I-693） | 6000 | 约 19 倍 |

实测最长值随表格增加而上升：2026-09-09 时是 1260 字符（I-864），
2026-09-11 变成 2310 字符 —— 不是 I-864 变长了，而是新增表格带进来的
HR-1 费用暂停公告（同时挂在 I-131／I-765／I-589 上）本身就有 2310 字符。
余量从 8 倍降到 4.3 倍，仍然够用，但**这个数会继续涨**：
每次复核顺手看一眼，掉到 2 倍以内就该调高 `ALERT_MAX` 了。
2026-09-11 全部 34 条公告均未触发截断。

**公告的切换规则往往写在末尾**，截断会丢掉最关键的部分 —— 早期上限设为 700 时，
I-765 的公告正好断在三条切换规则之前。因此上限要留足余量，且截断时在最后一个
完整句子处收口。

真的发生截断时，运行日志会打印警告并列出表格号，提示调高
`scraper.py` 中的 `ALERT_MAX` / `RAW_MAX`。

---

## 维护

版本发生变动时，`notes.yaml` 里对应的中文要点很可能过时（日期、宽限期都会变）。
通知 Issue 里已包含提醒。建议每次收到通知后顺手核对一遍该表格的要点。

**但要点过时不止「版本变动」这一个触发点。** 2026-10-01 的 I-864／I-864A 是反例：
宽限期到期那天，版本没变、公告没改、抓取侧 `changed` 仍是 0，通知 Issue 一条都不会发，
而两条要点在那一天同时失效（见第一节 A2 末尾）。
**凡是要点里写了日期的，都要拿当天日期去核一遍，不能只在收到变动通知时才核。**

若日后发现新的公告类型，请补充到本文的第一或第二节，并说明筛选规则是否需要调整。
