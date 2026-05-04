# GY462 Real Estate Finance — 2021 Exam Model Answers
# 2021年考试标准答案（英文答案 + 中文详解）

> Source: GY462 2026 lecture notes (Lec 1–3, Lec 9) + official exam solution hints
> Standard: UK 70 marks (Distinction pass line) — focus on 2–3 core points per question.

---

# QUESTION 1 — DCF Methods, Risk Assessment, Portfolio & Green Buildings

---

## Q1a — How does DCF combine risks and opportunities? Most important risks and opportunities in direct real estate? [5 pts]

*(Lecture 1)*

### Standard Answer

**How DCF combines risks and opportunities:**

The DCF framework captures risks and opportunities through two channels:

1. **The discount rate** (risk side) — the required rate of return (r = risk-free rate + risk premium) reflects the riskiness of the investment. Higher uncertainty about future cash flows demands a higher risk premium, compressing present value. Risks such as vacancy, tenant default, and illiquidity all inflate the discount rate.

2. **The projected cash flows** (opportunity side) — rental income, rental growth, and the terminal sale value are the sources of upside. A higher NOI or a rising exit cap rate environment directly increases the NPV. The investor seeks assets where expected cash flows exceed what the discount rate implies the market already prices in.

**Most important risks:** vacancy (unlet space generates zero income while costs persist) and liquidity risk (inability to exit at a fair price quickly).

**Most important opportunity:** terminal value — the exit sale proceeds, typically the dominant component of total return, especially over medium hold periods (3–7 years).

---

### 中文详解

**DCF 双通道理解：**
- **分母（折现率）= 风险**：风险越高 → r 越大 → PV 越小
- **分子（现金流）= 机会**：租金 + 租金增长 + 终值越高 → PV 越大

**最重要的风险**：空置（Vacancy Risk）和流动性风险（Liquidity Risk）
**最重要的机会**：终值/资本增值（Terminal Value），持有期越短、退出越重要

**关键词**：Risk Premium 风险溢价 / Discount Rate 折现率 / Terminal Value 终值 / NOI 净营业收入

---

## Q1b — Other methods used to value real estate assets [5 pts]

*(Lecture 1, 2 + Tristan Capital external speaker)*

### Standard Answer

Beyond DCF, three alternative valuation approaches are used in practice:

**1. Sales Comparison Approach (Comparables / "Comps")**
The subject property is valued by reference to recent arm's-length transactions of comparable properties in similar locations, of similar size, quality and tenancy. Adjustments are made for differences (floor, specification, lease length). This is the most reliable method when there are sufficient recent comparable transactions.

**2. Replacement Cost Approach (Construction Cost Method)**
The property's value is estimated as the cost of reproducing an equivalent building from scratch: land value + construction cost − physical depreciation. This method is most appropriate for special-purpose properties (schools, factories, car parks) where market comparables are scarce, but it tends to over-value older buildings and ignores market demand dynamics.

**3. Income Capitalisation (Cap Rate / Equivalent Yield)**
As discussed by the Tristan Capital external speakers, practitioners often use a direct capitalisation short-cut: Value = NOI / Cap Rate (or in the UK, the equivalent yield method). This provides a rapid market-based check on a full DCF model, particularly useful for stabilised income-producing assets. The limitation is its "myopia" — it captures only the current year's income and ignores future rental growth, which a full DCF correctly models.

---

### 中文详解

**三种替代估值法（记住各自的适用场景和局限）：**

| 方法 | 适用场景 | 局限 |
|-----|---------|-----|
| 可比销售法 Sales Comp | 市场活跃、可比交易多 | 需要足够的近期成交案例 |
| 重置成本法 Replacement Cost | 特殊用途物业（工厂/学校） | 忽视市场需求，会高估老建筑 |
| 直接资本化法 Cap Rate | 稳定收益物业，快速估值 | "近视"：忽略未来 NOI 增长 |

Tristan Capital 外部演讲者强调：Cap Rate 法是实务中的快速筛选工具，但仍需全 DCF 验证。

**关键词**：Comparable Transactions 可比交易 / Replacement Cost 重置成本 / Direct Capitalisation 直接资本化 / Equivalent Yield 等收益率（英国常用）

---

## Q1c — How can pro-forma analysis help assess revenues and costs in DCF? [5 pts]

*(Lecture 2)*

### Standard Answer

A pro-forma is a multi-year cash flow projection that systematically structures all revenue and cost items into a standardised format, enabling the analyst to build a credible DCF model:

**Revenue side (PGI → EGI → NOI):**
- **Potential Gross Income (PGI)** — the full rental income assuming 100% occupancy, calculated from the rent roll (tenant-by-tenant lease schedule).
- Less **Vacancy Allowance** — an explicit deduction for expected empty periods, forcing the analyst to make a specific assumption rather than assuming full occupancy.
- Plus **Other Income** (parking, signage).
- = **Effective Gross Income (EGI)** — realistic income the asset can generate.

**Cost side (OE and CapEx):**
- **Operating Expenses (OE)** — management fees, insurance, property taxes, maintenance. By itemising these, the analyst ensures no cost is overlooked.
- **Capital Improvement Expenditures** — tenant improvements (TIs), leasing commissions, and major repairs that are one-time but recur at lease renewal — a pro-forma forces these to be modelled explicitly rather than ignored.

The pro-forma thus imposes discipline: every assumption is explicit, transparent, and challengeable by lenders, partners, or the analyst themselves.

---

### 中文详解

**Pro Forma 的核心价值：** 把所有收入和成本**逐行列出**，不让任何假设隐藏。

**收入结构：**
- PGI（满租收入）→ 减空置 → 加其他收入 → = EGI → 减运营费用 → = NOI

**成本必须包括（常被遗漏的）：**
- 租户改善支出（TI）：新租约时装修支持 → 是真实的一次性资本支出
- 招租佣金（Leasing Commission）：每次出租付给中介
- 管理费（即使自管也要计入）

**关键词**：Rent Roll 租金清单 / PGI/EGI/NOI / Vacancy Allowance 空置扣除 / Tenant Improvements 租户改善支出 / Capital Expenditure 资本支出

---

## Q1d — Rent roll and operating costs: main considerations for forecasting [15 pts]

*(Lecture 2 + Case Studies: Croydon & Leeds)*

### Standard Answer

**Rent Roll Forecasting — key considerations:**

**1. Headline rent vs. effective rent**
The rent roll records the contractual (headline) rent per lease, but the effective rent received by the landlord is often lower due to:
- **Rent-free periods** — landlords typically grant new tenants several months of free occupancy to incentivise signing (especially in a weak market). The effective rent per year of the lease term is therefore lower than the headline. For example, a 5-year lease at £100,000/year with 6 months rent-free has an effective rent of £100,000 × (4.5/5) = £90,000/year.
- **Rental concessions** — fit-out contributions, stepped-rent arrangements, or capped service charges that reduce the landlord's net income.
- **Overage clauses** — in retail, some leases include turnover rent (overage): base rent plus a percentage of tenant's sales above a threshold. This adds revenue uncertainty but also upside.

**2. Square footage measurement**
In the UK, offices are typically measured on a Net Internal Area (NIA) basis. However, service charge recovery may be based on Gross Internal Area (GIA), which includes communal areas, plant rooms, and circulation space. Analysts must be clear which measure underlies the rent-per-square-foot calculation — using NIA for rent but GIA for charge recovery leads to errors.

**3. Lease structure and expiry profile**
The rent roll must flag when each lease expires (WAULT — Weighted Average Unexpired Lease Term). A building with leases all expiring in Year 3 faces a concentrated re-letting risk; a building with staggered expiry dates has diversified income risk.

**4. Estimating rental growth for un-let space**
For space expected to be vacant and then re-let, the analyst must forecast market rents at the time of re-letting, drawing on local market data (vacancy rates, rental trend indices). The Croydon case study illustrated that suburban office markets with structurally high vacancy require conservative assumptions — headline market rents may be achievable only at the cost of generous incentive packages.

**Operating Cost Forecasting:**

**5. Fixed vs. variable expenses**
Fixed costs (property taxes, insurance, management fees, security) accrue regardless of occupancy. Variable costs (utilities not recovered from tenants, maintenance) scale with occupancy. Both must be estimated separately and their growth rates assumed (typically CPI or a specific cost index).

**6. Service charge recoverability**
Under a Full Repairing and Insuring (FRI) lease, the tenant bears most operating costs — the landlord's net income is close to the headline rent. Under a gross lease (common in multi-let offices), the landlord absorbs operating costs, reducing NOI significantly. The Leeds case study highlighted a mixed lease structure where service charge recovery was partial, requiring careful modelling of irrecoverable costs.

**7. Capital expenditure reserves**
The pro-forma must include provisions for planned capex (refurbishment cycles, plant replacement) and unplanned maintenance. Omitting capex is one of the most common sources of IRR overstatement in pro-forma models.

---

### 中文详解

**两大模块分别展开：**

**租金清单（Rent Roll）关键问题：**

| 问题 | 具体内容 | 案例联系 |
|-----|---------|---------|
| 名义租金 vs 有效租金 | 减去免租期（Rent-Free）、租金优惠 | Croydon：弱市下免租期长达12个月 |
| 租赁面积计量 | NIA（净内部面积）vs GIA（总内部面积） | 服务费基础可能用 GIA，须区分 |
| 租约到期集中度 | WAULT 低 → 再出租风险集中 | Leeds：多租户错开到期 → 分散风险 |
| 超额租金（Overage） | 零售额超门槛后的额外收入 | 增加上行空间但增加不确定性 |

**运营成本（Operating Costs）关键问题：**
- FRI 租约 → 成本转嫁租户 → 净收入接近合同租金
- Gross 租约 → 房东承担运营成本 → NOI 被压缩，须单独建模
- 资本支出（CapEx）必须列入：遗漏是最常见的 IRR 高估来源

**关键词**：Effective Rent 有效租金 / Rent-Free Period 免租期 / NIA/GIA / WAULT 加权平均剩余租期 / FRI Lease 全修全保租约 / Service Charge 服务费

---

## Q1e — Estimating resale value; how to ensure sold at a premium [10 pts]

*(Lecture 2, 3)*

### Standard Answer

**Most common approach — terminal cap rate method:**

The standard way to estimate a building's resale value at the end of the holding period is the **direct capitalisation of the following year's NOI** using an assumed **going-out (exit) cap rate**:

$$\text{Resale Value} = \frac{\text{Year} (n+1) \text{ NOI}}{\text{Going-out Cap Rate}}$$

The year (n+1) NOI — the first year of cash flow the new buyer will receive — is used because the buyer prices the asset based on what it will earn going forward, not what it earned in the seller's final year.

**Why the going-out cap rate typically exceeds the going-in cap rate:**
- The building is older and requires more capital expenditure
- The remaining lease terms are shorter, increasing void risk
- Time horizon uncertainty increases risk premiums

**How to ensure the building is sold at a premium:**

1. **Maximise NOI growth** — the numerator in the cap rate formula. Aggressive but achievable rental growth, via proactive lease management (rent reviews, lease regears, re-letting at higher market rents) increases what the buyer will pay.

2. **Maintain lease covenant quality** — a building with long leases to strong-covenant tenants commands a lower exit cap rate (more like a bond), compressing the denominator. Active management of tenant mix — replacing weak tenants with creditworthy ones — protects and enhances exit pricing.

3. **Cap rate timing** — sell when market cap rates are compressing (during periods of falling interest rates or rising investor appetite). A 25bp compression in exit cap rate, at a £2M NOI, adds £1M to sale price at a 5% cap rate.

4. **Physical asset quality** — reinvesting in refurbishment during the holding period preserves leasability and signals quality to buyers, supporting a tighter exit cap rate.

---

### 中文详解

**退出价值公式（必须记住）：**

$$\text{退出价值} = \frac{\text{第}(n+1)\text{年 NOI}}{\text{退出 Cap Rate}}$$

为什么是 n+1 年？因为买家定价的是**他未来能收到的**现金流，不是卖家最后一年的过去收入。

**如何确保溢价出售（Premium Sale）？**
- 提高分子（NOI）：主动签约、续约、提升租金水平
- 压低分母（退出 Cap Rate）：长期强信用租约 → 类债券 → 要求更低 Cap Rate
- 时机选择：在利率下行、投资者食欲旺盛时出售（Cap Rate 压缩阶段）
- 资产维护：翻新投入 → 保持物业吸引力 → 支撑更低 Cap Rate

**关键词**：Going-out Cap Rate 退出资本化率 / Cap Rate Compression Cap Rate 压缩 / Lease Covenant 租约信用 / Asset Quality 资产质量

---

## Q1f — Risk assessment methods for direct real estate investment; what is stress-tested? [10 pts]

*(Lecture 3)*

### Standard Answer

Three complementary risk assessment methods are used alongside DCF analysis:

**1. Due Diligence**
A systematic pre-acquisition investigation covering: physical condition (structural survey, mechanical and electrical systems), legal title (clear ownership, no encumbrances), planning permissions, environmental contamination, and financial review (audit of historical NOI, lease documentation). Due diligence reduces the risk of discovering material problems post-acquisition. It is particularly important for institutional investors who must demonstrate accountability to beneficiaries.

**2. IRR / PV Decomposition (Partitioning)**
The total present value is split into the PV of operating cash flows and the PV of the terminal sale proceeds. If 70–80% of the total PV comes from the exit value, the investment's performance is highly sensitive to assumptions about the future market (exit cap rate, market conditions in Year 5 or 10). Decomposition reveals where value is concentrated and therefore where the key risks lie.

**3. Sensitivity Analysis ("Flexing" the Model)**
The three key variables most commonly stress-tested are:
- **Exit yield / going-out cap rate** (±50–100 bps) — the most impactful variable, since small changes in cap rate dramatically affect terminal value
- **Vacancy rate** (5%, 10%, 15%) — directly affects EGI and NOI
- **Rental growth rate** (pessimistic / base / optimistic scenarios)

For each scenario, the analyst recalculates the IRR and NPV, then computes the expected IRR, standard deviation (SD), and coefficient of variation (CoV = SD / E(IRR)). A lower CoV signals a more efficient risk-return trade-off. This enables comparison between two investments with similar expected IRRs but very different risk profiles.

---

### 中文详解

**三种风险评估法（考试三选二即可，敏感性分析最重要）：**

| 方法 | 核心功能 | 关键词 |
|-----|---------|-------|
| 尽职调查 Due Diligence | 收购前识别实质风险（物理/法律/财务） | 问责制（Accountability） |
| IRR分解 Partitioning | 看清价值集中在经营CF还是终值 | 终值占比越高 → 风险越大 |
| 敏感性分析 Sensitivity | 三情景IRR → 期望值、标准差、变异系数 | E(IRR), SD, CoV |

**最常被压力测试的变量：**
1. 退出 Cap Rate（±50bps，影响最大）
2. 空置率（5%/10%/15%）
3. 租金增长率（悲观/基准/乐观）

**公式**：E(IRR) = ΣPᵢ × IRRᵢ；SD = √Σ[Pᵢ × (IRRᵢ − E(IRR))²]；CoV = SD / E(IRR)

---

## Q1g — Data limitations for real estate portfolio assessment; methods to overcome them [20 pts]

*(Week 9 External Lecture — Dr. Niko Szumilo)*

### Standard Answer

**Principal data limitations in direct real estate portfolio analysis:**

**1. Appraisal-based (smoothed) returns**
Unlike equities, commercial real estate properties are not traded daily. Portfolio returns are typically based on periodic professional appraisals (usually quarterly or annually). Appraisers are known to **smooth** values over time — anchoring to previous valuations and adjusting gradually — rather than marking to market instantly. This creates three problems:
- Measured volatility is artificially low (understated risk)
- Serial correlation in returns is artificially high (returns appear more predictable than they are)
- Correlations with other asset classes (equities, bonds) are understated, making real estate appear to offer more diversification benefit than it actually does

**2. Illiquidity and infrequent transactions**
Because properties trade infrequently, many periods have no transaction price for a given asset. Any index of real estate returns based on actual transactions will have large gaps, leading to thin and potentially unrepresentative samples — especially in downturns when transaction volume collapses.

**3. Heterogeneity — no two properties are alike**
Unlike equities (where a share is identical to every other share), each property is unique in location, physical attributes, and lease structure. This makes it extremely difficult to construct meaningful indices or compare risk-adjusted returns across properties and portfolios.

**4. Private market opacity**
Direct real estate is traded privately (no exchange), so information on prices, yields, and transaction volumes is often proprietary or delayed. This contrasts sharply with listed markets where prices are public and continuous.

**Methods to overcome these limitations:**

**1. Return "unsmoothing"**
Mathematical techniques (e.g. Geltner's unsmoothing model) attempt to reverse the appraisal smoothing effect by extracting an estimated "true" returns series from the smoothed appraisal-based index. This produces a series with higher volatility and lower autocorrelation — more consistent with what a market-clearing price would show.

**2. Transaction-based indices**
Rather than relying on appraisals, transaction-based indices (e.g. IPF/MSCI transaction-based indices, US NCREIF TBI) use actual sale prices to construct returns. These are more volatile and represent true market pricing, but suffer from thin samples and selection bias (distressed sellers may transact at unusual prices).

**3. REIT-based proxies**
Listed Real Estate Investment Trusts (REITs) are publicly traded and provide continuous daily pricing. Their returns can be used as a proxy for direct real estate, though REITs introduce additional noise (equity market sentiment, management fees, leverage) and lead the direct market by 12–18 months. Researchers often use lagged REIT returns to approximate what the direct market will do.

**4. Hedonic regression**
Hedonic models control for property-specific characteristics (size, age, location quality, lease type) to construct "like-for-like" price indices, enabling comparison across heterogeneous properties. This helps decompose price changes into market-wide versus property-specific factors.

---

### 中文详解

**核心问题：直接房地产数据为什么特别难用？**

| 数据局限 | 根本原因 | 影响 |
|---------|---------|-----|
| 估值平滑 Appraisal Smoothing | 评估师锚定历史值，渐进调整 | 波动率被低估、相关性失真 |
| 交易稀少 Illiquidity | 非公开市场、每年成交极少 | 指数缺口多、代表性差 |
| 异质性 Heterogeneity | 每栋楼独一无二 | 难以构建可比指数 |
| 信息不透明 Opacity | 私下交易、价格不公开 | 市场价格发现能力差 |

**解决方法：**
- **Unsmoothing（去平滑）**：数学还原"真实"波动率（Geltner模型）
- **成交价指数（TBI）**：基于实际成交价，比估值指数更真实，但样本小
- **REIT代理**：用上市REIT日收益率代理直接房地产，领先直接市场约12-18个月
- **特征价格模型（Hedonic Regression）**：控制物业特征，提取纯市场价格变化

**关键词**：Appraisal Smoothing 估值平滑 / Transaction-Based Index 成交价指数 / REIT 房地产投资信托 / Unsmoothing 去平滑 / Hedonic Regression 特征价格回归

---

## Q1h — Most important considerations for structuring a real estate portfolio [10 pts]

*(Week 9 External Lecture — Dr. Niko Szumilo)*

### Standard Answer

When selecting assets for a direct real estate portfolio, three considerations dominate:

**1. Liquidity**
Liquidity varies significantly across real estate sub-sectors and geographies. Central London offices and prime logistics are among the most liquid UK assets (hundreds of comparable transactions per year); regional retail or secondary offices may see only a handful of transactions annually. A portfolio investor must match the liquidity profile of assets to the investment vehicle's redemption structure. An open-ended fund that allows quarterly redemptions cannot hold predominantly illiquid assets without creating a mismatch that triggers a "gating" crisis (as seen in UK open-ended property funds after Brexit and COVID). A closed-ended fund with a fixed life can tolerate greater illiquidity in exchange for higher returns.

**2. Asset characteristics — diversification by property type and geography**
Concentration risk is the enemy of portfolio resilience. A portfolio entirely in London offices is exposed to the economic fortunes of a single city and a single occupier type (financial services). Diversification across:
- **Property types** (office, logistics, residential, retail) — different economic drivers and lease structures
- **Geographies** (London, regional UK, European cities) — non-synchronised economic cycles
- **Lease lengths and covenant quality** — a mix of long-income core assets and shorter-lease value-add assets balances stability with growth

Modern Portfolio Theory (MPT) can be applied: the efficient frontier of real estate portfolios (maximum return for a given standard deviation) is achieved through correlation-minimising diversification across sub-sectors. However, as noted in Q1g, measured correlations in real estate data are unreliable due to appraisal smoothing — the true diversification benefit is typically lower than raw data suggests.

**3. Number of properties**
A meaningful reduction in idiosyncratic (property-specific) risk requires a minimum portfolio size. Research suggests that most idiosyncratic risk is diversified away with approximately 30–50 direct real estate assets across different property types and locations. Below this threshold, individual property events (a single large tenant default, a building-specific capex surprise) have an outsized impact on total portfolio returns. However, each additional property increases transaction costs, management complexity, and monitoring overhead — so scale must be balanced against operational capacity.

---

### 中文详解

**三大选资产原则：**

**1. 流动性匹配（Liquidity）**
- 开放式基金（允许随时赎回）→ 必须持有高流动性资产（核心伦敦/物流）
- 封闭式基金（固定存续期）→ 可持有低流动性资产换取更高回报
- 2016年英国脱欧后：多个开放式地产基金因流动性不足被迫"门控（Gating）"

**2. 资产特征多元化（Asset Characteristics）**
- 跨物业类型：办公/物流/零售/住宅 → 不同经济驱动因素
- 跨地理位置：伦敦/英国地区/欧洲 → 非同步经济周期
- 现代组合理论（MPT）的有效前沿可用，但须注意评估平滑导致相关性被低估

**3. 资产数量（Number of Properties）**
- 至少需要30-50个物业才能有效分散个体风险
- 低于此门槛：单个租户违约/单栋楼资本支出意外 → 对整体组合回报影响过大
- 更多资产 → 管理成本和复杂性上升 → 需平衡规模与运营能力

**关键词**：Open-ended vs Closed-ended Fund 开放式/封闭式基金 / Gating 门控 / MPT / Idiosyncratic Risk 特异性风险 / Diversification 多元化

---

## Q1i — Green buildings: value for investors and lenders; direct investor and lender perspectives [20 pts]

*(Lecture 9 — Dr. Liao, ESG Panel)*

### Standard Answer

**From the perspective of a direct investor (building owner):**

**1. Green premium on rents and values**
Buildings with strong sustainability credentials (BREEAM 'Excellent' or above, LEED Platinum, EPC A or B) command a rental premium of 10–20% over comparable non-certified buildings in major UK and European markets. This reflects corporate occupiers' own ESG commitments — many FTSE 100 and Fortune 500 companies now require their leased premises to meet minimum sustainability standards to satisfy their own net-zero pledges. For the landlord, this translates into both higher NOI and, through the cap rate formula (Value = NOI / Cap Rate), materially higher capital values.

**2. Mitigation of stranded asset risk**
Non-compliant buildings face a tightening regulatory environment. UK minimum EPC requirements are being raised progressively (already E for new leases; proposals to require B by 2030). A building that falls below the minimum EPC threshold cannot be lawfully let — making it a "stranded asset" with zero income and impaired value. Investing in energy efficiency upgrades (insulation, LED systems, heat pumps, photovoltaic panels) is therefore not just a value-enhancer but a risk mitigation measure that preserves lettability and avoids value cliff-edges.

**3. Lower operating costs**
High-performance, energy-efficient buildings consume significantly less energy. With rising energy prices, reducing operational energy consumption lowers irrecoverable service charges (where applicable), improving the building's competitiveness relative to less efficient alternatives and supporting occupier retention.

**4. Green lease provisions**
Green leases incorporate data-sharing obligations (energy, water, waste), minimum performance standards, and joint commitments to reduce emissions. From the investor's perspective, green leases reduce uncertainty about operating performance, facilitate access to green financing, and document the building's sustainability credentials for future sale.

**From the perspective of a lender (lending against a green building):**

**1. Lower credit risk / better loan performance**
Green buildings exhibit lower vacancy rates and stronger covenant quality (they attract larger, creditworthy corporate tenants). Lower vacancy reduces the probability that debt service is impaired. Empirically, green-certified buildings show lower rates of loan default compared to equivalent non-green assets.

**2. Access to green finance and regulatory compliance**
Banks and insurance companies face growing regulatory pressure (Bank of England climate stress tests, EU taxonomy) to reduce the carbon footprint of their loan portfolios. Lending against green-certified assets counts positively toward their own ESG reporting. Green buildings qualify for green bond financing, allowing banks to issue green bonds backed by a portfolio of certified assets.

**3. Sustainability-linked loan terms**
Lenders increasingly offer sustainability-linked loans (SLLs) where the interest rate is tied to the borrower's ESG KPIs (e.g. achieving an EPC A rating, reducing energy intensity by 20%). If the borrower meets the targets, the margin steps down, reducing the cost of debt. This creates alignment between borrower and lender incentives to maintain and improve the building's sustainability performance.

**4. Residual value protection**
From the lender's perspective, the building serves as collateral. A building that becomes unlettable due to EPC non-compliance loses value rapidly — impacting the bank's recovery in a default scenario. Green buildings provide more durable collateral values because they are better protected against regulatory and market obsolescence.

---

### 中文详解

**两个视角分别答（各约一半篇幅）：**

**直接投资者视角（Building Owner）：**

| 利益点 | 具体内容 |
|-------|---------|
| 绿色溢价 Green Premium | 租金溢价10-20%，NOI提升→资产价值提升 |
| 规避搁浅资产风险 | EPC达标 → 保持可出租性；不达标 → 无法出租 → 价值崩塌 |
| 降低运营成本 | 节能 → 服务费更低 → 竞争力更强 → 租户续约率高 |
| 绿色租约 Green Lease | 数据共享、最低能效标准 → 降低不确定性，便于融资 |

**贷款方视角（Lender）：**

| 利益点 | 具体内容 |
|-------|---------|
| 较低信用风险 | 绿色楼空置率低→债务偿付风险低 |
| 监管合规 | 银行ESG压力测试→绿色资产有利于银行自身报告 |
| ESG挂钩贷款（SLL） | 借款人达标→利率下调（双方利益对齐） |
| 抵押物价值保护 | 绿色楼不易"搁浅"→抵押物更耐久，银行违约损失更低 |

**关键词**：BREEAM / LEED / EPC / Stranded Asset 搁浅资产 / Green Premium 绿色溢价 / Sustainability-Linked Loan（SLL）ESG挂钩贷款 / Green Lease 绿色租约 / Climate Stress Test 气候压力测试

---

# QUESTION 2 — Mortgage Finance and Leveraged Returns

> Loan: £20,000,000 on a building worth £40,000,000; 5-year hold; quarterly compounding; 5% annual interest

---

## Q2a — IO loan: quarterly payments and balloon payment [5 pts]

*(Lecture 6)*

### Standard Answer

**Interest Only (IO) loan:**
- Loan: £20,000,000
- Annual interest rate: 5%
- Quarterly interest rate: 5% / 4 = **1.25%**

**Quarterly payment:**
$$\text{Quarterly payment} = 1.25\% \times £20{,}000{,}000 = \boxed{£250{,}000}$$

**Balloon payment at end of Year 5 (Quarter 20):**
Since no principal is repaid during the term, the full amount is due at maturity:
$$\text{Balloon payment} = \boxed{£20{,}000{,}000}$$

Total final quarter outflow = £250,000 + £20,000,000 = **£20,250,000**

---

### 中文详解

IO 贷款每期只还利息，本金（Balloon）在最后一期归还。

- 季利率 = 5% / 4 = 1.25%
- 季还款 = 1.25% × 20,000,000 = **£250,000**
- 第20期末（Year 5末）：还利息 £250,000 + 归还本金 £20,000,000

---

## Q2b — CPM: quarterly payments and outstanding balance at Year 5 [5 pts]

*(Lecture 6)*

### Standard Answer

**Constant Payment Mortgage (CPM):**
- Loan: £20,000,000
- Amortisation period: 30 years = **120 quarterly periods**
- Quarterly rate: 5% / 4 = 1.25%

**Step 1: Monthly payment:**

$$N = 120, \quad I/Y = 1.25\%, \quad PV = 20{,}000{,}000, \quad FV = 0$$
$$\text{CPT PMT} = \boxed{£322{,}669.91}$$

**Step 2: Outstanding balance after Year 5 (20 quarters):**

Using the AMORT worksheet (periods 1 to 20), or equivalently solving for the PV of the remaining 100 payments:

$$\text{Outstanding balance at Year 5} = \boxed{£18{,}360{,}350.29}$$

---

### 中文详解

- TVM 计算器：N=120, I/Y=1.25, PV=20,000,000, FV=0 → PMT = **£322,669.91**
- Year 5末余额：AMORT工作表设置第20期，或等价地对剩余100期付款求PV → **£18,360,350.29**

注意：5年20期后仍有 18,360,350/20,000,000 ≈ 91.8% 的本金未还。30年摊还期，早期还款以利息为主。

---

## Q2c — Effective cost of IO and CPM with £200,000 origination charge; compare [10 pts]

*(Lecture 6–7)*

### Standard Answer

**Origination charge:** £200,000 (flat fee, not a percentage). Net proceeds received = £20,000,000 − £200,000 = **£19,800,000**. Payments, however, are still calculated on the full £20,000,000 loan.

**IO Loan — effective annual cost:**
- CF0 = −£19,800,000
- CF1–CF19 = £250,000 (quarterly interest payments, periods 1–19)
- CF20 = £20,000,000 + £250,000 = £20,250,000 (balloon + final interest)

Solve for quarterly IRR, multiply by 4:

$$\text{Annual Effective Cost (IO)} = \boxed{5.2286\%}$$

**CPM Loan — effective annual cost:**
- CF0 = −£19,800,000
- CF1–CF19 = £322,669.91
- CF20 = £18,360,350.29 + £322,669.91 = **£18,683,020.20**

$$\text{Annual Effective Cost (CPM)} = \boxed{5.2370\%}$$

**Comparison:**

Both exceed the nominal 5% because the origination charge is effectively additional interest paid upfront on the same loan amount. The CPM is marginally more expensive (5.237% vs 5.229%) because the CPM's early payments are larger (£322,670 vs £250,000). In present-value terms, larger near-term outflows weigh more heavily than later ones, making the origination cost — borne at the same point — slightly more burdensome relative to the CPM's total payment stream.

---

### 中文详解

**开设费（Origination Charge）的逻辑：** 借款人到手 £19,800,000，但按 £20,000,000 还款 → 有效融资成本 > 名义利率 5%

**IO 计算步骤：**
- CF0 = -19,800,000
- CF1-19 = 250,000（季利息）
- CF20 = 20,250,000（利息+本金）
- IRR × 4 = **5.2286%**

**CPM 计算步骤：**
- CF0 = -19,800,000
- CF1-19 = 322,669.91
- CF20 = 18,360,350.29 + 322,669.91 = 18,683,020.20
- IRR × 4 = **5.2370%**

**CPM 略贵的原因：** 早期还款更多（322,670 > 250,000），现值权重更大，开设费的拖拽效应在分母更重的情况下更显著。

---

## Q2d — Rationale for origination charges; banks prefer CPM; borrowers prefer IO [5 pts]

*(Lecture 6–7)*

### Standard Answer

**Rationale for origination charges:**
Banks incur fixed upfront costs — credit underwriting, legal due diligence, property valuation, and documentation — regardless of loan size. Origination charges (whether a flat fee or discount points) recover these costs immediately, providing certain income that is not subject to prepayment risk. They also partially compensate the bank for the option value the borrower holds (the right to repay early).

**What banks prefer in CPM vs IO:**
- **Amortisation reduces credit risk progressively** — as the borrower repays principal each quarter, the outstanding loan balance falls, reducing the bank's exposure. A borrower who defaults in Year 4 of a CPM owes far less than under an IO loan, giving the bank better recovery prospects.
- **Improving LTV** — regular principal repayment improves the loan-to-value ratio, widening the equity cushion that protects the bank's position.
- **Predictable, above-interest payments** — the fixed CPM payment exceeds the interest charge, providing higher early cash flows to the bank from a pure income perspective.

**Why borrowers prefer IO:**
- **Lower periodic cash outflows** — £250,000/quarter vs £322,670/quarter frees up capital for reinvestment or reserves.
- **Maximum leverage effect** — the outstanding principal remains at £20M throughout, so the full leverage benefit (positive spread between asset return and debt cost) persists until exit.
- **No premium de-leveraging** — in a CPM, early principal repayments reduce the loan balance, which reduces the D/E ratio and dilutes the leverage multiplier on equity returns.

---

### 中文详解

与2022年Q2d相同逻辑，简化记忆：

- **银行收开设费**：回收固定承贷成本，且不受提前还款影响（已锁定）
- **银行喜欢CPM**：摊还→余额下降→违约时损失小；LTV随时间改善
- **借款人喜欢IO**：季付款低（£250K vs £323K）；维持高杠杆直到退出；避免提前去杠杆

---

## Q2e — ARM loan: payments for three rate periods and final balance [20 pts]

*(Lecture 7)*

### Standard Answer

An Adjustable Rate Mortgage (ARM) is modelled as a sequence of CPM loans, each resetting to the new interest rate on the then-outstanding balance for the remaining original term.

**Period 1: Year 1–2 (Quarters 1–8) at 4% annual / 1% quarterly, original 30-year term**

$$N = 120, \quad I/Y = 1\%, \quad PV = 20{,}000{,}000, \quad FV = 0$$
$$\text{CPT PMT} = \boxed{£286{,}941.90}$$

Outstanding balance after 8 quarters (AMORT periods 1–8):
$$\text{Balance at end of Year 2} = \boxed{£19{,}279{,}628.09}$$

---

**Period 2: Year 3–4 (Quarters 9–16) at 6% annual / 1.5% quarterly, remaining 28-year term**

New principal = £19,279,628.09; remaining term = 28 years = 112 quarters

$$N = 112, \quad I/Y = 1.5\%, \quad PV = 19{,}279{,}628.09, \quad FV = 0$$
$$\text{CPT PMT} = \boxed{£356{,}464.05}$$

Outstanding balance after 8 quarters (AMORT periods 1–8 of this sub-loan):
$$\text{Balance at end of Year 4} = \boxed{£18{,}712{,}354.18}$$

---

**Period 3: Year 5 (Quarters 17–20) at 7% annual / 1.75% quarterly, remaining 26-year term**

New principal = £18,712,354.18; remaining term = 26 years = 104 quarters

$$N = 104, \quad I/Y = 1.75\%, \quad PV = 18{,}712{,}354.18, \quad FV = 0$$
$$\text{CPT PMT} = \boxed{£391{,}985.66}$$

Outstanding balance after 4 quarters (AMORT periods 1–4, end of Year 5 = end of holding period):
$$\text{Final balloon repayment} = \boxed{£18{,}447{,}422.42}$$

---

### 中文详解

**ARM（可调利率抵押贷款）的核心逻辑：每次利率重置时，用当前余额作为新本金，剩余原始年限重新计算月供。**

三段计算流程（必须记住顺序）：

| 阶段 | 利率 | 本金 | 剩余期 | 季供 | 期末余额 |
|-----|-----|-----|------|-----|---------|
| Year 1-2 (8Q) | 4% (1%/Q) | £20,000,000 | 30yr=120Q | £286,941.90 | £19,279,628.09 |
| Year 3-4 (8Q) | 6% (1.5%/Q) | £19,279,628.09 | 28yr=112Q | £356,464.05 | £18,712,354.18 |
| Year 5 (4Q) | 7% (1.75%/Q) | £18,712,354.18 | 26yr=104Q | £391,985.66 | **£18,447,422.42**（提前还款额）|

**关键词**：ARM 可调利率贷款 / Rate Reset 利率重置 / Amortisation Schedule 摊还计划

---

## Q2f — Effective cost of borrowing of the ARM with £200,000 origination charge [10 pts]

*(Lecture 7)*

### Standard Answer

**Cash flow structure for the bank's IRR calculation:**

- CF0 = −£19,800,000 (£20M loan minus £200K origination charge)
- CF1–CF8: £286,941.90 × 8 quarters (Year 1–2, 4% period)
- CF9–CF16: £356,464.05 × 8 quarters (Year 3–4, 6% period)
- CF17–CF19: £391,985.66 × 3 quarters (Q1–Q3 of Year 5)
- CF20: £391,985.66 + £18,447,422.42 = **£18,839,408.08** (final payment + balloon)

Solve for quarterly IRR, multiply by 4:

$$\text{Annual Effective Cost (ARM)} = \boxed{5.5256\%}$$

**Comparison with IO and CPM:**

| Loan | Effective Annual Cost |
|------|----------------------|
| IO | 5.2286% |
| CPM | 5.2370% |
| ARM | **5.5256%** |

The ARM is the most expensive loan, despite beginning with a 4% initial rate. The reason: the two rate resets in Years 3 and 5 push the effective cost well above the initial headline rate. The ARM's effective cost of 5.53% substantially exceeds the nominal 4% starting rate because the origination charge is applied to the full loan upfront while later periods carry much higher rates (6% and 7%).

---

### 中文详解

**ARM 有效成本计算（CF Worksheet）：**

- CF0 = -19,800,000
- C01 = 286,941.90, F01 = 8
- C02 = 356,464.05, F02 = 8
- C03 = 391,985.66, F03 = 3
- C04 = 391,985.66 + 18,447,422.42 = 18,839,408.08, F04 = 1
- IRR × 4 = **5.5256%**

**ARM 贵的原因：** 初始 4% 很便宜，但后期 6%→7% 的上升是重要的隐性成本。开设费在第0期已支付，而后期高利率期的还款更大——总有效成本远超初始名义利率。

**排名**：IO (5.23%) < CPM (5.24%) < ARM (5.53%)

---

## Q2g — Unleveraged annual IRR [10 pts]

*(Lecture 1–2)*

### Standard Answer

**Investment parameters:**
- Purchase price: £40,000,000
- NOI: £275,000/quarter for Years 1–2 (8 quarters), then £500,000/quarter for Years 3–5 (12 quarters)
- Sale price at end of Year 5 (Quarter 20): £45,500,000

**Cash flow structure (CF worksheet):**
- CF0 = −£40,000,000
- CF1–CF8: £275,000 (8 quarters, Year 1–2)
- CF9–CF19: £500,000 (11 quarters, Year 3 through Q3 of Year 5)
- CF20: £500,000 + £45,500,000 = **£46,000,000**

Solve for quarterly IRR, annualise:

$$\text{Annual Unleveraged IRR} = \boxed{6.3708\%}$$

**Interpretation:** The building's unlevered return is ~6.37% p.a., reflecting the modest NOI in Years 1–2 and the capital gain from £40M to £45.5M. Notably, the cost of debt (5.23% for IO or CPM) is below this return — so leverage should generate positive equity returns above 6.37%.

---

### 中文详解

**计算步骤：**
- CF0 = -40,000,000
- C01 = 275,000, F01 = 8
- C02 = 500,000, F02 = 11
- C03 = 46,000,000 (500,000 + 45,500,000), F03 = 1
- IRR × 4 = **6.3708%**

**关键观察**：6.37% > IO成本（5.23%）> CPM成本（5.24%）→ 两者均为正向杠杆 → 借款将放大股权回报（但ARM后期6-7%，有效成本5.53%，仍低于6.37%，也是正向杠杆）

---

## Q2h — Leveraged annual IRRs: IO, CPM, ARM; compare and discuss [25 pts]

*(Lecture 3)*

### Standard Answer

**Equity invested for all three loans:**
The equity outflow = purchase price − net loan proceeds:

$$\text{CF0} = -(£40{,}000{,}000 - £19{,}800{,}000) = \boxed{-£20{,}200{,}000}$$

(The bank charges £200,000 origination upfront, so the borrower receives only £19,800,000 but must still make up the full £40M purchase price.)

---

**IO Leveraged IRR:**

- CF0 = −£20,200,000
- CF1–CF8: £275,000 − £250,000 = **£25,000**
- CF9–CF19: £500,000 − £250,000 = **£250,000**
- CF20: (£500,000 − £250,000) + (£45,500,000 − £20,000,000) = **£25,750,000**

*(Note: the balloon repayment is the full £20,000,000, even though the bank only advanced £19,800,000 — the discount is implicit in CF0.)*

$$\text{Annual Leveraged IRR (IO)} = \boxed{7.3602\%}$$

---

**CPM Leveraged IRR:**

- CF0 = −£20,200,000
- CF1–CF8: £275,000 − £322,669.91 = **−£47,669.91** (negative — NOI less than debt service in Years 1–2)
- CF9–CF19: £500,000 − £322,669.91 = **£177,330.09**
- CF20: (£500,000 − £322,669.91) + (£45,500,000 − £18,360,350.29) = **£27,317,979.80**

$$\text{Annual Leveraged IRR (CPM)} = \boxed{7.2906\%}$$

---

**ARM Leveraged IRR:**

- CF0 = −£20,200,000
- CF1–CF8: £275,000 − £286,941.90 = **−£11,941.90** (slight negative in Years 1–2)
- CF9–CF16: £500,000 − £356,464.05 = **£143,535.95**
- CF17–CF19: £500,000 − £391,985.66 = **£108,014.34**
- CF20: (£500,000 − £391,985.66) + (£45,500,000 − £18,447,422.42) = **£27,160,591.92**

$$\text{Annual Leveraged IRR (ARM)} = \boxed{7.0732\%}$$

---

**Comparison and discussion:**

| | Unleveraged | IO | CPM | ARM |
|--|------------|-----|-----|-----|
| Annual IRR | 6.37% | **7.36%** | **7.29%** | **7.07%** |
| Effective loan cost | — | 5.23% | 5.24% | 5.53% |

**All three loans generate positive leverage** (leveraged IRR > unleveraged IRR > loan cost). However, the magnitude of the leverage benefit differs:

**IO > CPM:** As in the 2022 exam, the CPM forces principal repayment early, creating negative net cash flows in Years 1–2 (£275,000 NOI < £322,670 debt service). These early losses are front-loaded and carry high present-value weight, dragging down the IRR. Although the CPM has a lower outstanding balance at exit (£18.36M vs £20M to repay), the time value effect favours the IO.

**IO > ARM:** The ARM starts cheaply (£286,942/quarter, only slightly above the IO's £250,000), producing near-neutral early cash flows. However, the rate resets to 6% and then 7% mean debt service jumps sharply in Years 3–5. The higher overall effective cost of the ARM (5.53%) eats into the equity return more than either the IO or CPM, despite the ARM's favourable start.

**Key insight:** The ranking of effective borrowing costs (IO < CPM < ARM) directly predicts the ranking of leveraged IRRs (IO > CPM > ARM). The timing of cash flows interacts with the leverage, amplifying the differences — early losses (CPM in Years 1–2, ARM in Years 1–2) reduce IRR disproportionately.

---

### 中文详解

**三种贷款杠杆 IRR 对比：**

| 贷款 | 早期净现金流 | 退出余额 | 杠杆 IRR |
|-----|-----------|---------|---------|
| IO | +£25,000/Q（正） | £20,000,000 | **7.36%** |
| CPM | −£47,670/Q（负！） | £18,360,350 | **7.29%** |
| ARM | −£11,942/Q（轻微负） → 后期快速上升 | £18,447,422 | **7.07%** |

**排名解释：**
- **IO最优**：早期现金流为正，完整保留杠杆，有效借款成本最低（5.23%）
- **CPM居中**：早期亏损（NOI < 季供）前加，IRR被拖低；但有效成本（5.24%）与IO接近
- **ARM最差**：尽管初始利率低（4%），后期跳至6%/7%，有效成本最高（5.53%），抵消了早期便宜的优势

**计算器操作提示（CF Worksheet）：**
- IO: C01=25,000/F01=8; C02=250,000/F02=11; C03=25,750,000/F03=1
- CPM: C01=-47,669.91/F01=8; C02=177,330.09/F02=11; C03=27,317,979.80/F03=1
- ARM: C01=-11,941.90/F01=8; C02=143,535.95/F02=8; C03=108,014.34/F03=3; C04=27,160,591.92/F04=1

---

## Q2i — WACC approximation: comparison with full DCF; what does WACC miss? [10 pts]

*(Lecture 3)*

### Standard Answer

**WACC estimates of leveraged equity return:**

$$r_E = r_P + (r_P - r_D) \times \frac{D}{E}$$

Where:
- $r_P$ = unleveraged IRR = 6.3708%
- D = £19,800,000 (net loan proceeds)
- E = £20,200,000 (equity invested)
- D/E = 19,800,000 / 20,200,000 = **0.9802**

Using the **effective** cost of borrowing for $r_D$:

| Loan | $r_D$ (effective) | WACC $r_E$ |
|------|------------------|------------|
| IO | 5.2286% | 6.3708% + (6.3708% − 5.2286%) × 0.9802 ≈ **7.49%** |
| CPM | 5.2370% | 6.3708% + (6.3708% − 5.2370%) × 0.9802 ≈ **7.48%** |
| ARM | 5.5256% | 6.3708% + (6.3708% − 5.5256%) × 0.9802 ≈ **7.20%** |

**Comparison with full DCF results:**

| Loan | WACC estimate | Full DCF | Difference |
|------|--------------|----------|------------|
| IO | 7.49% | 7.36% | WACC overstates by +0.13% |
| CPM | 7.48% | 7.29% | WACC overstates by +0.19% |
| ARM | 7.20% | 7.07% | WACC overstates by +0.13% |

**What WACC misses:**

WACC assumes a **constant D/E ratio** throughout the holding period, but this is incorrect:

1. **For the CPM**, the D/E ratio falls over time as principal is repaid — the loan balance drops from £20M to £18.36M by Year 5, increasing the equity proportion. WACC incorrectly applies the initial D/E ratio throughout, overstating the leverage effect and thus overstating the equity return.

2. **For the ARM**, D/E similarly changes, and additionally the cost of debt changes at each rate reset — something a single WACC figure cannot capture.

3. **WACC treats IO ≈ CPM** (7.49% vs 7.48%) when the full DCF shows a more meaningful gap (7.36% vs 7.29%), because WACC does not account for the timing of cash flows — the front-loaded losses under the CPM that disproportionately drag the IRR.

**The full DCF approach captures all of these effects precisely** by modelling each cash flow in each period. The WACC approximation is useful as a quick sanity check and for understanding the direction and rough magnitude of leverage effects, but it is an approximation that can mislead on relative rankings and precise values.

---

### 中文详解

**WACC 公式：**

$$r_E = r_P + (r_P - r_D) \times \frac{D}{E} = 6.3708\% + (6.3708\% - r_D) \times 0.9802$$

| 贷款 | WACC估算 | DCF精确值 | WACC高估 |
|-----|---------|---------|---------|
| IO | 7.49% | 7.36% | +0.13% |
| CPM | 7.48% | 7.29% | +0.19% |
| ARM | 7.20% | 7.07% | +0.13% |

**WACC 漏掉了什么？**
1. **D/E 随时间变化**：CPM摊还→贷款余额下降→D/E 下降；WACC 假设D/E固定 → 高估杠杆效应
2. **现金流时序**：WACC不能捕捉CPM早期亏损（-£47,670/Q）对IRR的前加拖拽效应
3. **ARM利率变动**：单一WACC无法代表三段不同利率，必须用多段现金流才能精确

**核心结论**：WACC排名方向正确（IO > CPM > ARM），但数值偏高，不能精确描述CPM vs IO的差距。全DCF方法是唯一精确的解法。

**关键词**：WACC 加权平均资本成本 / Constant D/E Assumption D/E固定假设 / Cash Flow Timing 现金流时序 / Approximation 近似值
