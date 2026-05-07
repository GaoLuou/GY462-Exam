# GY462 Real Estate Finance — Key Topic Model Answers
# 老师划重点标准答案（英文答案 + 中文详解）

> **说明**：内容来自 GY462 课件（Olmo Silva 教授讲义）。按 Distinction 70分难度撰写：突出 2–3 个核心论点，考试时间内可写完。

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

**计算题 Calculation Questions**
- [C1. Negative Amortization & Partial Amortizing Loans](#c1-negative-amortization--partial-amortizing-loans)
- [C2. Effective Cost of Borrowing with Discount Points](#c2-effective-cost-of-borrowing-with-discount-points)
- [C3. ARM: Effective Cost of Borrowing & Prepayment](#c3-arm-effective-cost--prepayment)
- [C4. Leveraged vs Unlevered IRR (Simple Cash Flow)](#c4-leveraged-vs-unlevered-irr)

---

# 理论题 Theory Questions

---

## T1. Risks & Opportunities of Direct Real Estate Investment

### Model Answer (English)

Direct real estate investment offers a distinctive risk-return profile compared to financial assets such as government bonds.

**Key Risks:**

The most important risks are vacancy and leasing risk. If a tenant vacates, the investor faces a period with no rental income while still bearing operating costs. Beyond that, real estate is highly illiquid: its large lot size and indivisibility mean it cannot be sold quickly or partially — this makes it vulnerable to forced selling at distressed prices. Finally, as a physical asset concentrated at a fixed location, it is exposed to natural disaster risk (fire, flood) in a way diversified financial portfolios are not.

**Key Opportunities:**

The primary opportunity is rental income growth. Since a property's value is anchored to its Net Operating Income (NOI), maximising rent and controlling operating costs is the most reliable path to value creation — more so than depending on favourable real estate cycles. Terminal value (resale proceeds) provides a secondary upside, but is highly uncertain because it depends on exit cap rates at the time of sale.

**Priority:** Among these opportunities, efficient operations and rental maximisation should take precedence. The terminal value is large but the least controllable; investors who focus on NOI generation first will outperform those who bet on market timing.

**Growth-Adjusted Cap Rate:** The cap rate can be adjusted for expected NOI growth: Adjusted Cap Rate = Raw Cap Rate − Growth Rate. When expected growth is negative, subtracting a negative number makes the adjusted cap rate *larger* — reflecting higher risk and lower value. This is why a high cap rate signals both high risk and low growth expectations simultaneously.

---

### 中文详解

**核心论点（考试必答的3个）：**

1. **空置/租赁风险（Vacancy & Leasing Risk）**：这是老师明确排到第一位的风险。空置意味着完全失去租金收入，而运营成本还在继续。考试时不要只列名称，要说明为什么它比其他风险更重要——它直接冲击 NOI（净营业收入 Net Operating Income），而资产价值由 NOI 决定。

2. **流动性风险（Liquidity Risk）**：大额、不可分割（large lot size & indivisibility）是直接投资区别于股票、债券的本质特征。老师在讲座中专门说"流动性是第二问的重点，别在第一问把话说完"——所以要根据子问题结构合理分配。

3. **机会的优先级（Priority of Opportunities）**：列出租金、终值（Terminal Value）、运营管理还不够，**必须给出排序**：首先专注最大化租金和高效运营，这是可控的；而市场周期带来的终值（Terminal Value，即出售所得）是不可控的，不应作为主要投资逻辑。老师明确说"没排序就丢分"。课件中三大机会是：Operating cost（运营成本优化）、Terminal value（终值）、Rental growth（租金增长）。

**⚠️ Growth-adjusted Cap Rate 的反直觉逻辑（必须能解释）：**

Growth-adjusted Cap Rate = Raw Cap Rate − Growth Rate

- 若 Growth > 0（预期租金增长）：adjusted cap rate 变小 → 资产价值更高，风险更低
- 若 Growth < 0（预期租金下降）：减去负数等于加上一个正数 → adjusted cap rate **变大** → 资产价值更低，风险更高
- 考试陷阱：不少人认为"负增长时 cap rate 减去负数，cap rate 会变小"——这是错误的！Cap Rate 变大才是正确方向。
- 这就是为什么说 **Cap Rate 大 = 风险高 + 机会少**——它同时反映了高折现率和低（甚至负）增长预期。

**不应该写的：** 不要在这道题用大量篇幅讲流动性，如果子问题明确把流动性单列出来的话。先通读所有子题再分配内容。

---

## T2. Risk Assessment Methods

### Model Answer (English)

The course identifies three main approaches to assessing risk in a real estate investment:

**1. Due Diligence:** The foundation of risk assessment before committing capital. This involves verifying financial projections, reviewing legal title, assessing market conditions, and checking physical condition of the asset. Due diligence establishes whether the investment assumptions are credible in the first place — without it, quantitative analysis rests on unverified inputs.

**2. Partitioning of IRR/NPV:** Decomposing the total IRR or NPV into its sources — income return (operating cash flows) versus capital return (terminal value from resale) — reveals whether the investment is overly dependent on resale proceeds. If most of the IRR comes from terminal value rather than operating income, the investment is riskier than the headline number suggests, since resale value is highly uncertain and depends on future cap rates at exit.

**3. Sensitivity Analysis:** Testing how the investment's IRR or NPV changes as key input variables are altered — rental growth, vacancy rates, exit cap rates, construction timeline. This identifies which variables drive the most risk. It takes three forms of increasing sophistication:

- *Stress Testing*: fix the central projection; move one variable at a time to its worst plausible value.
- *Scenario Analysis*: construct a small number of complete macro states (e.g., base / optimistic / pessimistic) where all correlated variables shift simultaneously.
- *Simulation / Monte Carlo*: assign probability distributions to each key input and run thousands of random draws simultaneously, producing a full probability distribution of IRR or NPV outcomes. This is the most rigorous form and was explicitly highlighted by the professor as rarely appearing in student answers despite being examinable.

**Key Insight:** Partitioning is the most commonly overlooked method. An investment with a strong headline IRR but most returns concentrated in terminal value is qualitatively riskier than one generating stable operating income throughout. Monte Carlo is the most commonly overlooked within Sensitivity Analysis.

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

## T3. Leverage: Effects on Return, Risk and Cash Flow

### Model Answer (English)

Leverage amplifies both returns and risks in a predictable, quantifiable way.

**Effect on Return:**
Using the yield decomposition framework, the equity yield is:

yE = (yP − LTV × yD) / (1 − LTV)

As long as the property return yP exceeds the cost of debt yD (positive leverage), equity yield rises with LTV. The Break-Even Interest Rate (BEIR) equals the unlevered IRR — borrowing below BEIR enhances equity returns; borrowing above destroys them.

**Effect on Risk:**
The equity risk premium is amplified by the leverage ratio (LR = 1/(1−LTV)):

RPE = RPD + LR × (RPP − RPD)

With risk-free debt (RPD = 0): RPE = LR × RPP. A 70% LTV loan doubles the equity risk premium relative to unlevered investment. Leverage does not create risk-free return; every unit of additional return comes with proportionally higher risk.

**Effect on Cash Flow:**
Early-period cash flows are squeezed most under debt service. Under an interest-only (IO) loan, the entire principal remains outstanding, so the investor must ensure sufficient NOI to cover debt service throughout — creating cash flow risk if vacancy rises. Partitioning the levered IRR into income and capital components helps identify whether cash flow is genuinely sufficient or the investment relies excessively on terminal value.

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

## T4. IO vs CPM Tradeoffs

### Model Answer (English)

The choice between Interest-Only (IO) and Constant Payment Mortgage (CPM) reflects a fundamental tradeoff between the interests of borrowers and lenders.

**From the Borrower's Perspective:**
IO loans are preferred by commercial investors because early-stage cash flows are often constrained — particularly during lease-up or development. IO loans minimise debt service in the critical early years, preserving cash flow when operating income may be lower. The full principal is repaid only at maturity, allowing the investor to deploy capital more efficiently in the interim.

**From the Lender's Perspective:**
IO loans are riskier. The bank's outstanding balance never decreases, so if the borrower defaults, the lender is exposed to the full original loan amount throughout the entire term. Under CPM, the outstanding balance decreases steadily with each payment, so the lender's exposure is progressively reduced. This is why banks charge a higher interest rate on IO loans: they require compensation for bearing greater duration risk.

**The Tradeoff:**
IO is good for the borrower but costly from the bank's viewpoint — and this misalignment is priced into the interest rate premium. CPM sacrifices early cash flow in exchange for a cheaper loan. In practice, institutional real estate investors often prefer IO precisely because NOI stability becomes more assured once the asset is stabilised, making the balloon repayment manageable.

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

## T4.5. Participation Loan

### Model Answer (English)

A participation loan (also called an equity kicker or equity participation mortgage) is a mortgage in which the lender receives, in addition to regular interest payments, a contractual share of the property's operating income or capital appreciation upon sale.

**Structure:**
The lender provides debt at a below-market base interest rate. In return, the lender receives a participation right — for example, a share of NOI above a specified threshold, or a percentage of the resale proceeds. This converts part of the lender's return from fixed interest into a variable, performance-linked component.

**Why it Exists — Risk and Return Logic:**
From the borrower's perspective, the lower base rate reduces the immediate debt service burden, improving early cash flow — similar in effect to an IO structure. From the lender's perspective, giving up fixed interest income in exchange for a participation right exposes them to both the upside and the operating performance of the asset. The lender's return becomes partially dependent on the borrower's management quality and market conditions.

**Key Exam Point:** The course notes that participation loans were not covered in depth but may appear as a theory question. The core concept to convey is the tradeoff: lower fixed rate for the borrower in exchange for sharing value creation with the lender.

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

## T5. Private Equity: GP/LP and Waterfall

### Model Answer (English)

In a private equity real estate fund, risk and return are deliberately split between two types of investor to align incentives.

**GP/LP Structure:**
The General Partner (GP) manages the fund — sourcing deals, overseeing asset management, and handling disposals. The Limited Partners (LPs) provide the bulk of the capital but are passive investors with limited liability. Because the GP has superior information and control, compensation is structured to align their incentives with LP interests.

**The Waterfall:**
Returns are distributed in a sequence designed to protect LPs first:
1. Return of capital to LPs
2. Preferred return (Pref) to LPs — a minimum annual return agreed at fund inception (the course example uses a 9% pref rate); the GP receives nothing until LPs have earned this hurdle
3. Catch-up to GP (to compensate for the promoted interest deferral)
4. Carried interest split above the hurdle (e.g., 80/20 LP/GP)

**Deal-by-Deal vs Whole Fund:**
Under deal-by-deal structures, the GP can crystallise promote on successful early disposals without waiting for underperforming assets to be resolved — this favours the GP. Whole-fund structures aggregate all returns before distributing promote, giving LPs stronger protection but reducing GP incentive to move quickly. In the UK market, whole-fund structures are more common.

**Note:** Waterfall calculations are theory-only in the exam. No numerical waterfall structuring will be required.

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
3. 补偿条款（Catch-up）：GP 追上之前被延迟的 promote
4. 超额分配（Carried Interest）：如 20% 归 GP，80% 归 LP

**Deal-by-Deal vs Whole Fund 对比**：
- Deal-by-deal：每笔交易单独结算，GP 可以在好的交易上提前拿 promote，对 LP 保护较弱
- Whole Fund（英国更常见）：汇总全部交易后才结算，LP 保护更强，GP 激励更长期

**激励机制的核心逻辑**：GP 拿 promote（绩效奖励）而不是固定管理费，目的是让 GP 的利益与 LP 对齐——只有 LP 赚了超额回报，GP 才能拿到大额报酬。

---

## T6. Development Finance

### Model Answer (English)

Development financing involves two distinct lending phases and a fundamental choice between simplified and full valuation methods.

**Interim vs Permanent Financing:**
During construction, the developer draws on an interim (or construction) loan provided by a bridging lender. This loan is typically short-term, interest-only, and carries a higher rate — reflecting the elevated uncertainty during the build phase. Once the property is completed and income-generating, the interim loan is refinanced with a permanent loan (a longer-term mortgage at a lower rate). The key risk in development finance is that construction cost overruns or lease-up failures may prevent the borrower from servicing the permanent loan, leaving the interim lender exposed.

**Shortcut Valuation ("Build at 10, Sell at 8") vs Full DCF:**
The shortcut — producing income at a 10% yield and selling at an 8% yield — gives a quick feasibility screen. Its advantage is speed and simplicity; its weakness is that it ignores timing of cash flows, construction duration uncertainty, and the cost of capital across phases. A full DCF, by contrast, explicitly models each quarter's costs and revenues, applies a risk-appropriate discount rate, and can incorporate stress tests (e.g., extending the construction period). The shortcut is a useful first filter; the full DCF is required for investment decisions.

---

### 中文详解

**两个核心知识点：**

**1. 过渡贷款（Interim/Construction Loan）vs 永久贷款（Permanent Loan）**：

| 贷款类型 | 时机 | 特征 |
|---------|------|------|
| 过渡贷款（Interim Loan） | 建设阶段 | 短期、利率高、按需提款（drawdown） |
| 永久贷款（Permanent Loan） | 竣工后、稳定经营后 | 长期、利率低、类似普通商业抵押贷款 |

关键风险：建设超支或招租失败 → 无法偿还过渡贷款或无法转换为永久贷款 → 开发商违约。

**2. 快捷估值（Shortcut: "Build at 10, Sell at 8"）vs 完整DCF（Full Evaluation）**：

- 快捷法：NOI / 建造成本 = 10%（建造端）；NOI / 售价 = 8%（出售端）→ 利润 ≈ 25%
  - 优点：快速筛选，不需要复杂建模
  - 缺点：忽略现金流时序、建设工期不确定性、资本成本的分阶段性

- 完整DCF：逐季度建模成本和收入，显式折现，可做压力测试（延长工期会怎样？）
  - 优点：更准确，能量化"如果工期延长2个季度，IRR 下降多少"
  - 缺点：需要更多假设和数据

**老师的考试提示**：可能被要求"比较快捷法和完整DCF的优缺点"，或"在什么情况下你会用快捷法而不是完整DCF"——这是典型的 Distinction 层次问题。

---

## T7. Mortgage-Backed Securities

### Model Answer (English)

Securitisation transforms illiquid mortgage loans into tradeable financial securities, broadening the funding base for mortgage markets.

**Life of a Mortgage Without Secondary Market:**
Originators hold loans on their own balance sheet until maturity, tying up capital and concentrating risk. The primary constraint is the lender's own capital and risk appetite.

**Life of a Mortgage With Secondary Market:**
Originators sell loans to a Government-Sponsored Enterprise (GSE) or conduit (Cash Programme), or exchange them for mortgage-backed securities (Swap Programme). This allows originators to recycle capital, originate more loans, and transfer credit risk. The GSE pools the loans and issues securities to investors.

**Three Types of MBS:**

| Security | Risk Allocation | Key Feature |
|---------|-----------------|-------------|
| **Mortgage-Backed Bond (MBB)** | Prepayment risk stays with **issuer** (over-collateralised) | Investor receives fixed coupon regardless of prepayments |
| **Mortgage Pass-Through** | Prepayment risk transferred to **investor** | Investor receives pro-rata share of all principal and interest payments |
| **CMO (Collateralised Mortgage Obligation)** | Risk **split across tranches** — senior tranche bears least, junior tranche bears most | Different investor risk preferences are matched through tranching |

**Key Exam Point:** Prepayment risk is the central concept — when interest rates fall, borrowers prepay early, and investors receive principal back when reinvestment rates are low. Who bears this risk is the fundamental differentiator between MBS types. No calculation questions will be set on MBS.

---

### 中文详解

**考试明确说"不考计算，只考理论"**

**证券化动机（Securitisation）**：银行持有抵押贷款会占用大量资本，通过证券化把贷款卖出去，可以收回资金再放新贷款，扩大信贷规模。

**Cash Programme vs Swap Programme**：
- Cash（现金方案）：银行把贷款直接卖给 GSE，获得现金
- Swap（互换方案）：银行把贷款"换"成 MBS 证券，自己再拿去卖给投资者

**三类证券的核心区别（必须能背下来）**：

| 证券类型 | 超额抵押？ | 提前还款风险归谁？ |
|---------|---------|---------------|
| 抵押债券（MBB）| 是（过度抵押）| **发行方（银行）**承担 |
| 过手证券（Pass-Through）| 否 | **投资者**按比例承担 |
| CMO（分层债券）| 视 tranche 而定 | **按批次（tranche）分配**：高级层最安全，次级层最危险 |

**提前还款风险（Prepayment Risk）**是核心概念：当市场利率下降时，借款人会提前还清贷款（去重新借更便宜的）。投资者收回本金时，只能以更低利率再投资——这对投资者不利。谁承担这个风险，决定了三类证券的本质区别。

---

## T8. ESG

### Model Answer (English)

ESG (Environmental, Social, Governance) considerations have increasingly direct implications for both investment returns and the cost of capital in real estate.

**Impact on Asset Risk:**
Buildings that fail to meet evolving environmental standards face obsolescence risk — future refurbishment costs, difficulty attracting high-quality tenants, and declining rents. Conversely, ESG-compliant assets attract a "green premium": stronger tenant demand, lower vacancy, and more resilient NOI. From an investor's perspective, ESG is not simply an ethical constraint but a forward-looking risk factor that should be incorporated into the discount rate and stress tests.

**Impact on Cost of Borrowing:**
Lenders are increasingly incorporating ESG scores into pricing. Assets assessed as more future-proof (better energy ratings, lower stranded asset risk) attract lower loan margins. This creates a direct link between ESG performance and financing cost — reducing the cost of debt, thereby improving levered IRR.

**Double Materiality:**
The course frames ESG through the lens of double materiality: inside-out (the asset's impact on the environment) and outside-in (how environmental and social risks flow back to affect the asset's financial performance — portfolio risk, insurance costs, asset valuations, rental yields, void periods). Investors who focus only on the ethical dimension miss the financial materiality channel. How a real estate business responds to ESG will determine yields, risks, financing terms, and ultimately valuations.

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

# 计算题 Calculation Questions

---

## C1. Negative Amortization & Partial Amortizing Loans

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

## C2. Effective Cost of Borrowing with Discount Points

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

## C3. ARM: Effective Cost & Prepayment

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

## C4. Leveraged vs Unlevered IRR

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
