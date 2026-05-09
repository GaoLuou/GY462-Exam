# GY462 Real Estate Finance — Key Topic Model Answers
# 老师划重点标准答案（英文答案 + 中文详解）

> **说明**：内容来自 GY462 课件（Olmo Silva 教授讲义）。按 Distinction 70分难度撰写：突出 2–3 个核心论点，考试时间内可写完。
>
> **优先级标记：** 🔴 及格必记 | 🟡 Merit加分（60+）| 🟢 Distinction（时间够再看）
> **只想及格：只读标 🔴 的章节**，其余跳过。

---

## 目录

**理论题 Theory Questions**
- [T1. Risks & Opportunities of Direct Real Estate Investment](#t1-risks--opportunities-of-direct-real-estate-investment)
- [T2. Risk Assessment Methods (Due Diligence / Partitioning IRR / Sensitivity Analysis incl. Monte Carlo)](#t2-risk-assessment-methods)
- [T3. Leverage: Effects on Return, Risk and Cash Flow](#t3-leverage-effects-on-return-risk-and-cash-flow)
- [T4. IO vs CPM: Who Prefers What and Why?](#t4-io-vs-cpm-tradeoffs)
- [T4.5. Participation Loan: Concept and Risk Allocation](#t45-participation-loan)
- [T5. Private Equity: GP/LP Structure and Waterfall](#t5-private-equity-gplp-and-waterfall)
- [T6. Development Finance: Interim vs Permanent Loan; Shortcut vs Full Evaluation](#t6-development-finance)
- [T7. Mortgage-Backed Securities: MBB, Pass-Through, CMO](#t7-mortgage-backed-securities)
- [T8. ESG: Impact on Investment Risk and Cost of Borrowing](#t8-esg)
- [T9. DCF Valuation: Pro Forma Structure & Risk-Adjusted Discount Rates](#t9-dcf-valuation-pro-forma--discount-rate-unbundling)
- [T10. Inflation Tilt Problem: GPM & ARM as Solutions](#t10-inflation-tilt-problem-gpm--arm-as-solutions)

**计算题 Calculation Questions**
- [C1. Negative Amortization & Partial Amortizing Loans](#c1-negative-amortization--partial-amortizing-loans)
- [C2. Effective Cost of Borrowing with Discount Points](#c2-effective-cost-of-borrowing-with-discount-points)
- [C3. ARM: Effective Cost of Borrowing & Prepayment](#c3-arm-effective-cost--prepayment)
- [C4. Leveraged vs Unlevered IRR (Simple Cash Flow)](#c4-leveraged-vs-unlevered-irr)

---

# 理论题 Theory Questions

---

## T1. Risks & Opportunities of Direct Real Estate Investment 🔴 及格必记

### Model Answer (English)

**Downside Risks:**

1. **Operating cost:** maintenance, insurance, management costs exceed budget → NOI decreases even at full occupancy.

2. **Natural disaster:** physical asset at a fixed location → cannot diversify geographically → concentrated loss exposure; unlike equities, cannot spread across locations.

3. **Vacancy:** no tenant → rental income = 0, fixed costs continue → NOI turns negative. Worse than leasing risk: no income at all.

4. **Leasing:** tenant in place but defaults mid-lease, or renews below market rent → NOI decreases; rent locked by contract → cannot renegotiate upward.

5. **Liquidity:** large lot size + indivisible → cannot sell quickly or in parts → forced sale (e.g., loan covenant breach) → sale price decreases sharply.

**Opportunities:**

1. **Operating cost:** cost control → NOI increases directly, independent of market conditions → most controllable opportunity.

2. **Terminal value:** resale price = largest single cash flow, but depends entirely on exit cap rate and market at time of sale → least controllable.

3. **Rental growth:** rent reviews + market upswing → NOI increases each period → asset value compounds over the holding period.

**Priority:** Operating cost + Rental growth > Terminal value. Resale price is anchored to NOI; relying on market timing adds risk without adding control.

---

### 中文详解

**课件五大风险逐点解析（Lec01，幻灯片10）：**

1. **运营成本（Operating Cost）**：维修、保险、管理费等超出预算 → NOI 被直接压缩。即使满租也会因为成本超支而亏损。

2. **自然灾害（Natural Disaster）**：物业是固定地点的物理资产，无法像股票那样分散到不同地区 → 火灾、洪水等集中风险。

3. **空置（Vacancy）**：完全没有租金收入，但固定成本仍在运转。**比 Leasing 更严重的风险**——因为连收入都没有，而 Leasing 风险至少还有合同租金（哪怕低于市场价）。

4. **租约（Leasing）**：租户在位但出现问题——拖欠租金（违约）或合同期满时无法按市场价续约。与 Vacancy 的区别：有合同保护但存在执行风险；与 Vacancy 的共同点：都直接冲击 NOI。

5. **流动性（Liquidity）**：大额（Large lot size）+ 不可分割（Indivisibility）→ 无法快速或部分出售。⚠️ **若子问题单独问流动性，这里就少说，留给那道子题**。

**课件三大机会逐点解析（Lec01，幻灯片11）：**

1. **运营成本优化（Operating Cost）**：节约成本直接提升 NOI，**最可控**——不依赖市场。

2. **终值（Terminal Value）**：出售所得通常是总收益中最大的一笔现金流，但**最不可控**——完全取决于出售时的 Cap Rate 和市场状况。

3. **租金增长（Rental Growth）**：通过租金审查和市场上涨实现 NOI 复利增长，属于可在一定程度上主动管理的机会。

**优先级排序（老师说"没有排序就丢分"）：**
- 第一：Operating cost + Rental growth（可控，主动管理）
- 最后：Terminal value（不可控，不应作为主要投资逻辑）
- 原因：资产售价归根结底由 NOI 决定；追求 NOI 增长 > 赌市场周期

> **⚠️ 注意：** Growth-Adjusted Cap Rate 属于估值方法（T9），不要写进本题。流动性如果有专门子题，Q1a 就少写，留给专门那问。

---

## T2. Risk Assessment Methods 🟡 Merit加分（老师 mock 反馈：大家普遍漏了关键点）

### Model Answer (English)

**1. Due Diligence:**
Verifies inputs before any quantitative analysis: financial projections, legal title, market conditions, physical condition.
Without it, IRR and NPV are built on unverified assumptions → conclusions are unreliable regardless of model precision.
⚠️ Most commonly omitted in exam answers; the course lists it first.

**2. Partitioning of IRR/NPV:**
Splits total IRR into: income return (operating cash flows) vs capital return (terminal value from resale).
High proportion from terminal value → investment depends heavily on exit cap rate → risk is higher than the headline IRR number suggests.
If most of the return is back-loaded, any deviation in exit market conditions has a disproportionate impact.

**3. Sensitivity Analysis** — three forms in increasing rigour:
- *Stress Testing*: one variable changed at a time → worst plausible value → identifies which single variable matters most.
- *Scenario Analysis*: all correlated variables shift together (e.g., recession scenario) → shows combined impact of a macro event.
- *Monte Carlo*: probability distributions assigned to each key input → thousands of random draws simultaneously → produces a full IRR/NPV distribution → tells you "probability that IRR falls below X%". ⚠️ Most commonly omitted within sensitivity analysis.

**Exam priority:** mention all three methods; within Sensitivity Analysis go stress → scenario → Monte Carlo in order.

---

### 中文详解

**⚠️ 注意：课件（Lec03）列出的三种方法与很多人背的不同！**

**课件（Lec03）的三种标准方法：**

1. **尽职调查（Due Diligence）**——课件第一个列出的方法，但几乎没人提！考试必须写。核心：在做定量分析之前，先验证所有输入假设（市场数据、法律产权、物业状况）是否可信。尽职调查是风险评估的基础，没有它，后面的 IRR 计算全是建在沙子上的。

2. **IRR分解/NPV分解（Partitioning of IRR/PV）**——课件第二个方法，也是高分点。核心思路：把 IRR 拆成"运营收益（income return）"和"资本增值/终值（capital/terminal value return）"两部分。如果大部分 IRR 来自终值（resale），说明这笔投资高度依赖市场时机，风险比表面数字大得多。

3. **敏感性分析（Sensitivity Analysis）**——课件第三个方法，内含三个层次：
   - **压力测试（Stress Testing）**：固定中心预测，逐个改变单一关键变量（租金、空置率、资本化率）
   - **情景分析（Scenario Analysis）**：多个变量同时变化，模拟完整的宏观状态（如经济衰退 vs 繁荣）
   - **模拟/蒙特卡洛（Simulation / Monte Carlo）**：⚠️ **老师明确说 mock 里几乎没人提**，是直接得分点。做法：对每个关键变量（租金增长率、空置率、资本化率）赋予概率分布（如正态分布），同时随机模拟数千次，生成 IRR/NPV 的完整概率分布。比情景分析更严谨——不是选几个离散情景，而是穷举所有可能的组合，得到"IRR 低于 X% 的概率是多少"这类答案。

**考试写法建议**：三大方法各一段，在 Sensitivity Analysis 下按层次递进（stress → scenario → Monte Carlo），最后点出 Partitioning 最常被忽略，Monte Carlo 在 Sensitivity Analysis 内最常被忽略——这种有层次的分析最容易拿 Distinction。

---

## T3. Leverage: Effects on Return, Risk and Cash Flow 🟡 Merit加分

### Model Answer (English)

**Effect on Return:**

yE = (yP − LTV × yD) / (1 − LTV)

yP > yD → positive leverage → equity return (yE) > property return (yP).
yP < yD → negative leverage → yE < yP; leverage destroys value.
Break-Even Interest Rate (BEIR) = unlevered IRR: borrow below BEIR → yE rises; borrow above → yE falls.

**Effect on Risk:**

RPE = RPD + LR × (RPP − RPD),  where LR = 1/(1 − LTV)

Higher LTV → LR increases → equity risk premium scales up by the same multiple as equity return.
Extra levered return = proportionally higher equity risk; no free lunch.

**Effect on Cash Flow:**

Debt service paid each period → cash flow available to equity decreases.
IO: principal stays at full amount throughout → cash flow risk persists until exit.
CPM: outstanding balance falls each period → lender's exposure shrinks → investor's cash flow risk decreases over time.

---

### 中文详解

**三条主线（每条都有公式支撑）：**

1. **杠杆与收益（Leverage & Return）**：
   - 关键公式：`yE = (yP − LTV × yD) / (1 − LTV)`
   - 正杠杆条件：`yP > yD`（物业回报率 > 借贷利率）
   - 盈亏平衡利率（Break-Even Interest Rate, BEIR）= 无杠杆 IRR。超过 BEIR 借款就变成负杠杆，放大损失。

2. **杠杆与风险（Leverage & Risk）**：
   - 关键公式：`RPE = RPD + LR × (RPP − RPD)`，LR = 杠杆率 = V/E = 1/(1−LTV)
   - 债务无风险时简化为：`RPE = LR × RPP`
   - LTV=70% 时 LR ≈ 3.33，即股权风险溢价是物业整体的3.33倍

3. **杠杆与现金流（Leverage & Cash Flow）**：
   - IO贷款：早期不还本金，现金流相对宽裕，但期末需还全部本金（balloon payment）
   - CPM贷款：每期均匀还款，本金逐步减少，银行风险较小，故利率略低
   - **IRR分解**：看收益来自运营还是来自出售——过度依赖出售意味着现金流风险高

**税的影响（After-Tax IRR）**：
- 利息税盾（Interest Tax Shield）：`实际借贷成本 = 利率 × (1 − 税率)`
- 折旧税盾（Depreciation Tax Shield）：只有建筑可折旧，土地不可折旧
- 这两项使税后杠杆 IRR 高于税前

---

## T4. IO vs CPM Tradeoffs 🔴 及格必记

### Model Answer (English)

**IO:** monthly payment = interest only → principal balance unchanged throughout → lender's exposure stays at full original loan amount → lender charges higher rate.

**CPM:** monthly payment = fixed, principal component rises each period → outstanding balance falls → lender's exposure shrinks progressively → lender charges lower rate.

**Rate order:** CAM < CPM < IO. Faster principal repayment reduces the lender's credit exposure → lower rate justified.

**Borrower preference for IO:** lower early debt service → more cash retained when NOI is low (e.g., lease-up phase). Cost: higher rate and a balloon repayment at maturity.

**Lender preference for CPM:** outstanding balance falls each period → loss-given-default shrinks over time → lower risk.

The rate premium on IO compensates the lender for bearing full principal exposure throughout the entire term.

---

### 中文详解

**核心对比（考试必须给出"双方视角"）：**

| 贷款类型 | 借款人（Borrower）偏好理由 | 银行（Lender）视角 |
|---------|--------------------------|-----------------|
| IO（纯利息）| 早期还款少，现金流压力小 | 风险敞口始终是原始贷款额，风险较高 → 利率更高 |
| CPM（等额还款）| 前期还款较多，现金流较紧 | 余额逐渐减少，风险逐期收缩 → 利率较低 |

**老师原话的核心逻辑**：这是一个典型的 tradeoff 题。IO 对借款人友好（节约早期现金流），对银行是风险（敞口期长）。银行会通过收更高利率来补偿。如果你只列出了双方偏好而没说"为什么这种偏好会被定价进利率"，就没有答到 Distinction 层次。

**利率排序记忆**：`CAM 利率 < CPM 利率 < IO 利率`（银行收回资金越慢，利率越高）

---

## T4.5. Participation Loan 🟢 Distinction（及格可跳过）

### Model Answer (English)

A participation loan sets the base interest rate below market. In exchange, the lender receives a contractual share of either NOI above a threshold or resale proceeds at exit.

**For the borrower:** lower base rate → debt service decreases → early cash flow increases. Cost: a portion of any upside goes to the lender.

**For the lender:** fixed interest income decreases. In return: performance-linked participation replaces some fixed return. Risk: lender's return now depends on operating performance and market conditions at exit → lender's exposure to asset risk increases.

**Core trade-off:** borrower retains more cash early; lender gains a share of value creation in exchange for the rate reduction.

---

### 中文详解

**⚠️ 老师提醒：没怎么讲，但理论题可能出——要知道概念和逻辑。**

**参与贷款（Participation Loan）** = 贷款方除利息外，还参与分享物业收益。

**结构**：
- 基础利率低于市场水平（对借款人友好）
- 作为补偿，lender 获得：
  - 物业运营收入（NOI）超过一定门槛后的**一部分**，或
  - 出售时资本增值的**一部分**

**核心逻辑（考试答这两点即可）**：

| 视角 | 内容 |
|------|------|
| Borrower（借款人）| 较低的固定利率 → 早期现金流压力更小，类似IO的效果 |
| Lender（贷款方）| 放弃了部分固定利息 → 换取物业上行收益的参与权，但同时承担管理和市场风险 |

**与普通抵押贷款的关键区别**：普通贷款 lender 的回报是固定的（利率确定）；参与贷款 lender 的回报有浮动部分，与物业表现挂钩。这改变了 lender 和 borrower 之间的风险分配结构。

---

## T5. Private Equity: GP/LP and Waterfall 🟡 Merit加分

### Model Answer (English)

**GP/LP Structure:**
GP: contributes <5% of capital, makes all operating decisions, bears unlimited liability.
LP: contributes >95% of capital, no decision-making role, liability limited to capital contributed.

Principal-agent problem: GP controls the asset but bears little downside → the waterfall aligns GP compensation with LP returns.

**Waterfall — distribution sequence:**
1. Return of capital to LP (first call on all proceeds)
2. Preferred return to LP (e.g., 9% pa) — GP receives nothing until this hurdle is cleared
3. Catch-up to GP (GP receives 100% until GP's cumulative share = 20% of total profits distributed so far)
4. Carried interest: remaining proceeds split 80% LP / 20% GP

**Deal-by-deal:** GP gets promote per successful deal (US standard) — favours GP, faster cash out.

**Whole-fund:** GP gets promote only after entire fund clears hurdle (UK standard) — favours LP, GP waits.

Note: waterfall calculations are not required in the exam — theory only.

---

### 中文详解

**考试重点（老师明确说：只考理论，不考计算）**

**GP（General Partner，普通合伙人）vs LP（Limited Partner，有限合伙人）**：

| 角色 | 资金来源 | 管理职责 | 风险暴露 |
|------|---------|---------|---------|
| GP | 少量（1–5%） | 全部运营决策 | 无限责任 |
| LP | 大量（95–99%） | 被动投资者 | 有限责任（仅出资额） |

**瀑布（Waterfall）分配顺序**：
1. 返还本金（Return of Capital）
2. 优先回报（Preferred Return / Pref）：课件示例为年化 9%（具体数值由基金协议约定，每个基金不同）——LP 达到该收益率前 GP 不参与分配
3. 补偿条款（Catch-up）：GP 独享 100% 分配，直到 GP 的累计所得 = 已分配总利润的 20%（追平到最终 carry split 比例，与 pref rate 无关）
4. 超额分配（Carried Interest）：如 20% 归 GP，80% 归 LP

**Deal-by-Deal vs Whole Fund 对比**：
- Deal-by-deal：每笔交易单独结算，GP 可以在好的交易上提前拿 promote，对 LP 保护较弱
- Whole Fund（英国更常见）：汇总全部交易后才结算，LP 保护更强，GP 激励更长期

**激励机制的核心逻辑**：GP 拿 promote（绩效奖励）而不是固定管理费，目的是让 GP 的利益与 LP 对齐——只有 LP 赚了超额回报，GP 才能拿到大额报酬。

---

## T6. Development Finance 🟡 Merit加分

### Model Answer (English)

Real estate development uses two sequential loans:

- **Construction (interim) loan:** short-term, interest-only, higher rate — reflecting no income yet and elevated completion risk.
- **Permanent loan:** longer term, lower rate, replaces the interim loan once the project stabilises (reaches target occupancy).

The transition is the critical risk point: cost overrun, time overrun, or lease-up failure can prevent the developer from repaying the interim lender, triggering default.

Two valuation approaches apply:

- **Shortcut method** (e.g., "build at 10%, sell at 8%"): provides a quick feasibility screen but ignores cash flow timing and tends to overstate value when construction delays occur.
- **Full DCF:** models each period's costs and revenues with a risk-adjusted discount rate — required for actual investment decisions.

The shortcut serves as initial screening; full DCF is the standard for final investment commitment.

**3. How Developers Manage Risk:**

Three primary risks: (1) cost overrun — construction costs exceed budget; (2) time overrun — delays increase interim loan costs; (3) contractor default — builder becomes insolvent mid-project.

Contract choice determines who bears each risk: 🟢 Distinction

| Contract | Developer bears | Investor/Funder bears |
|---------|----------------|----------------------|
| **Turnkey** | Low — contractor takes fixed price and delivery risk | Minimal — pays premium for certainty |
| **Forward Fund** | Completion risk | Market/value risk; funds project from start |
| **Forward Commitment** | All construction, time and lease-up risk | Only market value risk post-completion |

Forward Commitment: developer gets a committed buyer → easier to secure construction finance. Investor avoids tying up capital during construction.

---

### 中文详解

**1. 两阶段融资（老师最高频强调——"the interplay between construction loan and permanent loan"）**：

| 贷款类型 | 时机 | 特征 |
|---------|------|------|
| 过渡贷款（Interim Loan） | 建设阶段 | 短期、纯利息（IO）、利率高、按进度分批提款（drawdown） |
| 永久贷款（Permanent Loan） | 竣工 + 稳定出租后 | 长期、利率低、类似普通商业抵押贷款 |

关键风险：成本超支或招租失败 → 无法偿还过渡贷款 → 过渡贷款方风险敞口增加 → 潜在违约。
工期延误会**加剧**这一风险：未付利息累加到贷款余额（负摊销）→ 欠债越拖越多。

**2. 快捷估值 vs 完整DCF（老师原话："shortcut as opposed to a fully fledged valuation"）**：

- **快捷法（Shortcut）**：以 10% 收益率倒算建造成本上限，以 8% 出售 → 快速可行性筛选。缺陷：忽略现金流时序和工期不确定性 → 工期延误时高估 NPV。
- **完整DCF**：逐季度建模成本和收入，用风险调整折现率 → 更准确；实际投资决策必须用。

快捷法是初步筛选工具；项目通过筛选后才做完整 DCF。

**3. 开发商如何管理风险（老师原话："how a developer manages risk"）**🟢 Distinction：

三大开发风险：① 成本超支（cost overrun）② 工期超支（time overrun）③ 承包商违约（contractor default）。

合同选择决定谁来承担这些风险：

| 合同类型 | 开发商主要风险 | 投资者/融资方主要风险 |
|---------|--------------|-------------------|
| Turnkey（交钥匙）| 低——成本+工期风险转给承包商 | 极低——支付溢价换取确定性 |
| Forward Fund（预先融资）| 须完工 | 市场价值风险；从建设阶段开始提供资金 |
| Forward Commitment（预先承购）| 承担全部建设、工期和出租风险 | 仅竣工后的市场价值风险 |

Forward Commitment：开发商提前锁定买家 → 更易获得建设融资；投资者不在建设期占用资金。

**关键术语：** Interim Loan 过渡贷款 / Permanent Loan 永久贷款 / Drawdown 分批提款 / Shortcut Valuation 快捷估值 / Turnkey 交钥匙合同 / Forward Fund 预先融资 / Forward Commitment 预先承购 / Cost Overrun 成本超支 / Negative Amortisation 负摊销

---

## T7. Mortgage-Backed Securities 🔴 及格必记（纯理论，背下来就有分）

### Model Answer (English)

**Without Secondary Market:**
Originator holds loans on balance sheet → capital tied up → new lending capacity decreases → mortgage market grows slowly.

**With Secondary Market:**
Originator sells loans to GSE or private conduit → capital recycled → new lending capacity increases → prepayment risk transferred to MBS investors (GSEs absorb default/credit risk through their guarantee).

GSEs and conduits use two mechanisms: **Cash programme** — GSE pays cash for the loans, then issues MBS itself. **Swap programme** — GSE exchanges MBS directly for the bank's mortgages, letting the bank sell or hold the MBS. Both recycle capital and scale up the secondary market.

To create predictable cash flows, loans are pooled into **homogeneous** groups — similar in financial terms (rate, maturity, LTV) and structural terms (loan type, property type). Homogeneity reduces variation in prepayment behaviour, making the pool's cash flows predictable enough to price and sell to investors.

**Prepayment risk** is the key concept: when rates fall, borrowers prepay early → investors receive principal back at the worst time (when reinvestment rates are low) → interest income decreases. The three MBS types differ only in who bears this risk:

| Security | Over-collateralised? | Who bears prepayment risk? |
|---------|---------------------|---------------------------|
| **MBB** | Yes | Issuer → investor gets fixed coupon regardless of prepayments |
| **Pass-Through** | No | Investor → receives actual cash flows pro-rata |
| **CMO** | Tranched | Split: senior tranche bears least → lower yield; junior tranche bears most → higher yield |

CMO allows investors with different risk preferences to self-select: senior investors sacrifice yield for prepayment protection; junior investors accept prepayment risk in exchange for higher yield.

No calculation questions will be set on MBS.

---

### 中文详解

**考试明确说"不考计算，只考理论"**

**证券化动机（Securitisation）**：银行持有抵押贷款会占用大量资本，通过证券化把贷款卖出去，可以回笼资金再放新贷款，扩大信贷规模。转移的核心风险是**提前还款风险（prepayment risk）**，而非信用风险——GSE 通过担保自行吸收了违约/信用风险。

**Homogeneous Pooling（同质化打包）**——老师原话点名的缓解机制：
贷款打包前须保证同质性，包括：
- 金融同质（Financial）：利率类型相近、期限相近、LTV 相近
- 结构同质（Structural）：贷款类型相近、物业类型相近、地理分布类似

同质 → 还款行为相似 → 提前还款模式可预测 → 投资者能对证券定价。若 pool 里混入不同类型贷款，提前还款行为分散，现金流无法预测，证券就卖不出去。

**Cash Programme vs Swap Programme**：
- Cash（现金方案）：银行把贷款直接卖给 GSE，获得现金；GSE 再自行发行 MBS
- Swap（互换方案）：GSE 直接把 MBS 换给银行（银行拿 MBS 再自行出售）

**三类证券的核心区别（必须能背下来）**：

| 证券类型 | 超额抵押？ | 提前还款风险归谁？ |
|---------|---------|---------------|
| 抵押债券（MBB）| 是（过度抵押）| **发行方（银行）**承担 |
| 过手证券（Pass-Through）| 否 | **投资者**按比例承担 |
| CMO（分层债券）| 视 tranche 而定 | **按批次（tranche）分配**：高级层最安全，次级层最危险 |

**提前还款风险（Prepayment Risk）**是核心概念：当市场利率下降时，借款人会提前还清贷款（去重新借更便宜的）。投资者收回本金时，只能以更低利率再投资——这对投资者不利。谁承担这个风险，决定了三类证券的本质区别。

---

## T8. ESG 🟡 Merit加分

### Model Answer (English)

**Impact on Asset Risk:**
ESG non-compliance → vacancy increases, insurance costs increase, capex for refurbishment increases → NOI decreases → asset value decreases.
Regulatory tightening → stranded asset risk increases → asset may become unlettable or uninsurable.

ESG compliance → tenant demand increases, green premium on rent increases → NOI increases → asset value increases.
(JLL data: green premium up to 11.6% in London offices.)

**Impact on Cost of Borrowing:**
Higher ESG score → lender perceives lower default risk → loan margin decreases → cost of debt decreases → levered IRR increases.

**Double Materiality:**
Outside-in: environmental and regulatory risks flow back into NOI, vacancy, insurance costs, and valuations.
Inside-out: the asset's own emissions and energy consumption create future compliance cost exposure.

Treating ESG as only an ethical issue misses the direct financial channel: ESG performance determines yields, financing terms, and ultimately asset valuations.

---

### 中文详解

**今年课件（Lec10，外部讲师 S. Burak Kaplanoglu）的核心框架：**

**ESG 影响四个维度**（课件结论幻灯片）：Risks（±）、Yields（±）、Finance（±）、Valuation（±）——答题时可用这个结构组织思路。

**两条主线（必须都答到）：**

1. **ESG 影响资产风险（Asset Risk）**：
   - 不达标 ESG 的资产面临"搁浅资产风险（Stranded Asset Risk）"——法规趋严后空置期延长（longer void periods）、可能变成不可保资产（uninsurable assets）、运维问题（如传统锅炉无法使用）
   - 达标 ESG 的资产有"绿色溢价（Green Premium）"——课件引用 JLL 数据：伦敦办公楼绿色溢价高达 11.6%，北美 7.1%，亚洲 9.9%
   - 应纳入折现率和压力测试的考量中

2. **ESG 影响借款成本（Cost of Borrowing）**：
   - 课件数据：73% 的贷款方已有 ESG 贷款策略；81% 认为 ESG 表现将日益影响其贷款意愿；93% 认为监管机构可能要求将可持续性纳入资本配置模型（影响贷款可用性和成本）
   - 更低的借贷成本 → 提升有杠杆 IRR（Levered IRR）
   - 课件核心观点：ESG = 非财务绩效，但它直接影响财务绩效（双重实质性，Double Materiality）

**双重实质性（Double Materiality）**：课件提出的核心概念——Inside out（企业对环境/社会的影响）+ Outside in（环境/社会风险对企业财务的反向影响）。两个方向都要考虑。

---

## T9. DCF Valuation: Pro Forma & Discount Rate Unbundling 🟡 Merit加分（2025年Q1e，15分）

### Model Answer (English)

**Pro Forma Cash Flow Structure:**

**Pro Forma — operating cash flow waterfall:**

```
  PGI    Potential Gross Income  (full-occupancy rent roll)
− V      Vacancy Allowance       (never assume 100% occupancy)
+ OI     Other Income            (parking, signage, misc.)
────────────────────────────────────────────────────────
= EGI    Effective Gross Income
− OE     Operating Expenses      (fixed: taxes, insurance;
                                   variable: maintenance, utilities)
────────────────────────────────────────────────────────
= NOI    Net Operating Income
− CI     Capital Improvement Expenditures  (TIs, leasing commissions,
                                             major repairs)
────────────────────────────────────────────────────────
= PBTCF  Property Before-Tax Cash Flow
```

**Terminal value (reversion):**

Reversion = NOI_{n+1} / Going-Out Cap Rate

⚠️ Use Year n+1 NOI (the buyer's first year), not Year n.
Going-out cap rate > going-in cap rate: property ages, exit-market uncertainty increases.

**Risk-Adjusted Discount Rates — Unbundling:**

| Cash flow type | Risk | Discount rate |
|---------------|------|---------------|
| Intra-lease (contracted rent within active lease) | Tenant default only | Lower |
| Inter-lease / terminal value (re-letting, resale) | Full market uncertainty — future rents and exit cap rates unknown | Higher |

Single blended rate underprices terminal value risk → valuation overstated.
Unbundling applies different rates to each type → risk concentration is made explicit.

Terminal value = majority of total return → investment is more sensitive to exit cap rate than to annual NOI → partitioning IRR into income vs reversion components quantifies this.

---

### 中文详解

**考试背景：** 2025年Q1e考了15分，题目是"DCF 如何量化房地产投资的风险和机会"——这是标准理论题。

**Pro Forma 结构（必须会写这条线）：**

```
PGI（满租收入）
− 空置损失（Vacancy Allowance）：不能假设100%出租率！
+ 其他收入（Other Income）
= EGI（有效总收入）
− 运营费用（Operating Expenses）：包含物业税、保险等固定+可变费用，不含折旧和贷款
= NOI（净营业收入）
− 资本改善支出（Capital Improvement Expenditures）：TIs（租户装修贡献）+ 中介佣金
= PBTCF（税前物业现金流）
```

**终值计算：NOI_{n+1} / Going-Out Cap Rate**
- ⚠️ 用第 n+1 年 NOI（买方视角：他买入后第一年能收到的）
- Going-Out Cap Rate ≥ Going-In Cap Rate（物业老化+不确定性增加）

**折现率拆分（Unbundling）——这是最容易拿 Distinction 的要点：**

| 现金流类型 | 风险来源 | 折现率 |
|-----------|---------|-------|
| 租约内（Intra-Lease）| 仅租户违约风险 | **低**（现金流已由合同锁定）|
| 租约间/终值（Inter-Lease/Reversion）| 市场风险（重新出租价格、退出资本化率）| **高**（完全暴露于市场不确定性）|

单一折现率会系统性低估这种差异。两段式折现率才能真实定价合同收入与非合同收入之间的风险不对称。

**关键术语：** PGI（Potential Gross Income）潜在总收入 / NOI（Net Operating Income）净营业收入 / PBTCF（Property Before-Tax Cash Flow）税前物业现金流 / Going-Out Cap Rate 退出资本化率 / Intra-Lease 租约内 / Inter-Lease 租约间 / Unbundling 现金流拆解 / Partitioning 分解

---

## T10. Inflation Tilt Problem: GPM & ARM as Solutions 🟡 Merit加分

### Model Answer (English)

**The Tilt Problem:**

Fisher equation: (1 + r_nominal) = (1 + r_real) × (1 + π)

π↑ → nominal rate rises → CPM monthly payment rises sharply (e.g., doubles at π = 6%, r_real = 4%).
Payment fixed in nominal terms → real value falls each year.
Real burden front-loaded: highest in Year 1, lowest at maturity.
→ Borrower fails Day-1 qualification test (payment-to-income too high), even if affordable over the full term.

**GPM — Solution:**

Early payment < interest due → unpaid interest capitalised → balance grows (negative amortisation).
Payment rises each year (e.g., 7.5% pa for 5 years) → tracks nominal income growth.
→ Day-1 payment lower → qualification test passed.
Cost: balance grows early → LTV rises → lender's security decreases.

**ARM — Solution:**

Rate = market index + margin, resets periodically (e.g., annually).
At origination: teaser rate < equivalent fixed rate → initial payment lower.
Inflation rises → rate rises → payment rises. Inflation falls → rate falls → payment falls (no refinancing needed).
→ Lender avoids embedding worst-case inflation premium upfront → initial rate lower.
Cost: borrower bears interest rate risk.

GPM smooths the payment profile; ARM avoids locking in a high nominal rate at the outset.

---

### 中文详解

**考试背景：** 复习清单明确标为 🟡："通货膨胀如何推动 GPM 和 ARM 的使用"。

**倾斜问题（Tilt Problem）核心逻辑（Lec07）：**

```
高通胀（π↑）
→ Fisher方程：名义利率↑ （1+r_nom）=（1+r_real）×（1+π）
→ CPM 名义月供大幅上升（从 £286 到 £537！）
→ 实际月供在早期非常沉重，后期随通胀侵蚀而减轻
→ 借款人"倾斜"——实际负担集中在最前期
→ 收入/月供比达不到银行资格标准 → 有效借款需求下降
```

**GPM（渐进还款贷款）的解决方案：**
- 早期月供低于应付利息 → 产生负摊销（余额短暂增加）
- 月供每年以固定比例（如7.5%）递增，匹配借款人名义收入增长
- 优点：解决早期资格问题
- 缺点：总利息更高；银行早期安全边际缩小（Lec07: balance can exceed property value）

**ARM（可调利率贷款）的解决方案：**
- 利率随市场基准（Index + Margin）定期重置
- 不在贷款起点就锁定"高通胀溢价" → 初始利率（Teaser Rate）低
- 借款人分担利率风险换取更低起步利率
- 优点：若通胀后来下降，借款人自动受益
- 缺点：利率上升时月供可能大幅增加（不可预测性）

**Fisher 方程（必须能写出）：**

(1 + r_nominal) = (1 + r_real) × (1 + inflation)

简化近似：r_nominal ≈ r_real + inflation rate

**关键术语：** Tilt Problem 倾斜问题 / Fisher Equation 费雪方程 / GPM（Graduated Payment Mortgage）渐进还款贷款 / ARM（Adjustable Rate Mortgage）可调利率贷款 / Negative Amortisation 负摊销 / Teaser Rate 诱惑初始利率 / Interest Rate Risk 利率风险

---

# 计算题 Calculation Questions

---

## C1. Negative Amortization & Partial Amortizing Loans 🔴 及格必记（老师强调三遍）

### Model Answer — Methodology (English)

**Negative Amortization Loan:**
In a negatively amortizing loan, scheduled payments are deliberately set below the interest due in early periods. The unpaid interest is added to the outstanding balance, causing the balance to *grow* over time rather than shrink.

Calculator approach:
- N = total number of periods
- I/Y = periodic interest rate
- PV = original loan amount (negative sign convention: cash received = positive PV; or set as negative)
- PMT = the deliberately low payment (smaller than interest due)
- **FV = outstanding balance at maturity → this will be LARGER than original PV** (principal has grown)
- Solve for the unknown

**Partial Amortizing Loan (Balloon Payment):**
The loan amortises on a long schedule (e.g., 30 years) but becomes due after a shorter holding period (e.g., 10 years). The remaining balance at year 10 is the balloon payment.

Calculator approach:
- Set N = total amortisation schedule (e.g., 360 months for 30 years)
- Solve for PMT using I/Y and PV
- Then: to find the balloon, either:
  - Set N = actual holding period (e.g., 120 months) and solve for FV; or
  - Use AMORT function: P1 = 1, P2 = 120, read BAL

**Critical Rule:** FV ≠ 0 in both cases. This is the single most common error.

---

### 中文详解

**老师在课上反复强调这是最容易出错的考点！**

**负摊销贷款（Negative Amortization Loan）**：
- 每期还款额 < 当期利息 → 差额加到贷款余额上 → 余额越来越大
- 计算器设置：**FV > PV**（期末余额大于初始贷款额），FV 不能留 0！
- 物理意义：银行借给你 100 万，到期你不仅要还 100 万，还要还积累的未付利息

**部分摊销贷款（Partial Amortizing Loan）**：
- 按照 30 年摊销表计算 PMT，但实际持有 10 年后提前到期
- 第10年末有一笔气球还款（Balloon Payment）= 第10年末的剩余余额
- 计算器设置：先解出 PMT（N=360），再求 FV（N=120 时的余额）

**常见错误（老师原话）**：
1. 把 FV 留成 0 → 计算出来是标准 CPM，不是这两种贷款
2. 把负摊销和IO+CPM混用 → 认为"先IO期，再CPM期"——这是错的，整个期间是一个连贯的摊销逻辑
3. 计算器内存残留 → 每次计算前必须清除内存（CLR → Memory）

---

## C2. Effective Cost of Borrowing with Discount Points 🔴 及格必记

### Model Answer — Methodology (English)

Discount points are upfront fees paid by the borrower at origination to "buy down" the stated interest rate. They increase the effective cost of borrowing because the borrower receives less net cash than the face value of the loan.

**Step-by-Step Calculation:**

1. Calculate the scheduled monthly PMT using the full loan amount, stated rate, and total term.
2. Adjust the cash flow at time 0: the borrower receives `Loan Amount − Discount Points (£)`. For example, if discount points = 2% on a £750,000 loan, the borrower receives £750,000 − £15,000 = £735,000.
3. Set up the IRR calculation:
   - CF0 = −£735,000 (negative: cash out from lender's perspective, or cash received by borrower)
   - CF1 to CFN = PMT each period (positive: payments from borrower to lender)
   - For full term: CFN also includes any remaining balance (FV)
4. Solve for IRR (periodic rate) → annualise by multiplying by 12 (monthly) or 4 (quarterly).

**Key Intuition:** Effective cost > stated rate whenever discount points are present. The shorter the holding period, the higher the effective cost (points are amortised over fewer periods).

**Sanity check:** If effective cost < stated rate, something is wrong — recheck the calculation immediately. Write a note: "I recognise this is counterintuitive; logically ECB should exceed the stated rate with discount points."

---

### 中文详解

**有效借款成本（Effective Cost of Borrowing, ECB）的核心逻辑：**

折扣点（Discount Points）是预付的一次性费用，借款人实际到手金额 < 贷款面值。实际借的钱少了，但每月还款和最终还款不变，所以真实的利率成本比名义利率更高。

**计算步骤**（以月付CPM为例）：

```
Step 1：按名义利率计算月供 PMT
  N = 总月数
  I/Y = 月利率
  PV = 贷款面值（例：750,000）
  FV = 0（标准CPM）
  → 解 PMT

Step 2：构建实际现金流
  CF0 = -(750,000 - 折扣点金额)   ← 实际到手金额（取负）
  CF1至CFN = PMT（每月还款）
  （若提前还款：CFN 还需加上剩余余额）

Step 3：求 IRR
  → 月利率 × 12 = 年有效成本（ECB）
```

**两个必须记住的逻辑规则**：
1. **ECB > 名义利率**：有折扣点时必须成立。如果算出来 ECB < 名义利率，立即说"I recognise there is an error; ECB must exceed the stated rate"
2. **持有期越短，ECB越高**：折扣点摊薄在更少的期数上，每期分摊更多

**老师原话**：曾有学生算出 ECB < 名义利率，然后说"这是合理的因为是摊销贷款"——这是错误的，而且没有意识到矛盾的学生会失去理解分。

---

## C3. ARM: Effective Cost & Prepayment 🟡 Merit加分

### Model Answer — Methodology (English)

An Adjustable Rate Mortgage (ARM) has an interest rate that resets at specified intervals (typically annually) based on a benchmark index plus a spread.

**Calculating Effective Cost of an ARM:**

The challenge is that the interest rate changes over time, so the cash flows are not uniform. The approach is:

1. For each rate period, calculate the remaining balance at the start of that period (using the balance from the prior period as PV).
2. Calculate the payment for that period based on the new rate and remaining term.
3. Compile the full sequence of actual payments as an irregular cash flow stream.
4. Apply IRR to the full series (CF0 = net proceeds after discount points; CF1…CFN = actual payments each period).

**Prepayment and the ARM Counter-Intuition:**

Normally, prepayment with discount points increases effective cost (fewer periods to amortise the points). However, with an ARM where rates increase steeply in later periods, prepaying before those periods are reached avoids high-cost future cash flows — which can actually *reduce* the effective cost below full-term ECB. Always calculate both scenarios before concluding which is cheaper.

**Key Point — Rate Conversion:** When given a nominal annual rate with monthly compounding, simply divide by 12 (no effective rate conversion needed — the calculator uses simple division internally).

---

### 中文详解

**ARM（可调利率贷款 Adjustable Rate Mortgage）的计算逻辑：**

ARM 的利率不固定，每隔一段时间根据市场基准利率重置，所以现金流是**不规则**的（每段利率期对应的月供不同）。

**有效借款成本计算步骤**：
1. 逐段计算：每个利率期开始时，用当期利率和剩余期数重新计算 PMT
2. 拼接出完整的不规则现金流序列
3. CF0 = 实际到手金额（贷款面值 − 折扣点）
4. 对整个现金流序列求 IRR

**ARM 提前还款的反常情况（反直觉）**：

通常：提前还款 → ECB 更高（折扣点摊薄期短）

但对于 ARM：如果后期利率大幅上升，提前还款相当于**逃避了后期高利率**，节省的利息可能超过折扣点损失 → ECB 反而更低

老师明确说：见到 ARM 提前还款题，**不要假设结论，必须计算后再判断**。

**利率换算**：名义年利率 ÷ 12 = 月利率（不需要有效年利率公式，计算器内在逻辑是直接除法）

---

## C4. Leveraged vs Unlevered IRR 🔴 及格命脉（老师说这就是Q2的核心结构）

### Model Answer — Methodology (English)

**Unlevered IRR (Property-Level IRR):**
Calculated from the perspective of an all-equity investor. Cash flows are the property's NOI each period plus the resale proceeds at exit.

```
CF0 = −Purchase Price
CF1…CFN-1 = NOI (each period)
CFN = NOI_N + Resale Price (= Year N+1 NOI / Going-out Cap Rate)
IRR = unlevered property IRR
```

**Levered IRR (Equity IRR):**
Accounts for the debt taken on and its repayment schedule:

```
CF0 = −(Purchase Price − Loan Amount)    [equity invested]
CF1…CFN-1 = NOI − Debt Service
CFN = NOI_N + Resale Price − Debt Service − Outstanding Loan Balance
IRR = levered equity IRR
```

For an IO loan: outstanding balance at exit = original loan amount.
For a CPM loan: outstanding balance at exit < original loan (must calculate using AMORT or FV function).

**Quarterly Cash Flows:**
If given quarterly figures, work entirely in quarterly periods:
- N = number of quarters
- I/Y = quarterly rate (annual rate ÷ 4)
- Annualise quarterly IRR by × 4 (not compounding — as confirmed by the professor)

**Sanity Check:** Levered IRR > Unlevered IRR when positive leverage holds (cost of debt < property IRR). If levered IRR < unlevered IRR, check whether the loan rate exceeds property return (negative leverage).

---

### 中文详解

**无杠杆 IRR vs 有杠杆 IRR 的核心逻辑：**

无杠杆（Unlevered IRR）= 把物业当纯股权投资，看物业本身的回报率。

有杠杆（Levered IRR）= 只看股权部分的现金流，借来的钱不算在自己投资里，但债务还款要从现金流中扣除。

**关键计算差异**：

| 项目 | 无杠杆 IRR | 有杠杆 IRR |
|------|-----------|-----------|
| CF0 | −全部购买价格 | −自有资金（购买价 − 贷款额）|
| 中间期 CF | NOI | NOI − 债务还款（PMT 或利息）|
| 最终期 CF | NOI + 售价 | NOI + 售价 − 最终还款 − 剩余余额 |

**IO vs CPM 的区别**（期末）：
- IO：剩余余额 = 原始贷款额（一分未还）
- CPM：剩余余额 < 原始贷款额（需用 AMORT 或 FV 功能计算）

**季度现金流处理**（老师确认）：
- 年利率 ÷ 4 = 季利率（不需要复利换算）
- 季度 IRR × 4 = 年化 IRR
- 直接用季度做，不要折算成年度（折算会引入误差，且偏离题目要求）

**正负杠杆检验**：
- 有杠杆 IRR > 无杠杆 IRR → 正杠杆（借贷利率 < 物业回报率）✓
- 有杠杆 IRR < 无杠杆 IRR → 负杠杆，检查假设是否正确

---

*参考来源：GY462 Real Estate Finance, LSE，Olmo Silva 教授，2026年春季学期讲义及考前复习录音*
*Last Updated: 2026-05-07 | Distinction-level model answers*
