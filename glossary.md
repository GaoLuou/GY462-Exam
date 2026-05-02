# GY462 缩写与术语速查表
# GY462 Abbreviations & Glossary

> 按主题分类。每个缩写附中文全称、英文全称、简要解释。

---

## 一、通用金融计算 General Finance

| 缩写 | 英文全称 | 中文 | 解释 |
|------|---------|------|------|
| **PV** | Present Value | 现值 | 未来现金流折现到今天的价值 |
| **FV** | Future Value | 终值 | 今天的钱在未来某时点的价值 |
| **NPV** | Net Present Value | 净现值 | 所有现金流折现后的净值；NPV > 0 → 值得投资 |
| **IRR** | Internal Rate of Return | 内部收益率 | 使 NPV = 0 的折现率；越高越好 |
| **DCF** | Discounted Cash Flow | 折现现金流 | 把未来每期现金流按折现率折回今天的方法 |
| **CF** | Cash Flow | 现金流 | 每期收到或支出的资金 |
| **CF0** | Initial Cash Flow | 初始现金流 | 第 0 期（今天）的现金流，通常是负数（投资额） |
| **PMT** | Payment | 每期还款额 | CPM/CAM 中每期支付的固定金额 |
| **BAL** | Balance | 余额 | 当前未偿还的贷款本金 |
| **BAL₀** | Initial Balance | 初始贷款额 | 贷款最初的本金总额 |
| **BAL_t** | Balance at time t | 第 t 期余额 | 还了 t 期后剩余的未偿本金 |
| **AMORT** | Amortization | 摊销 / 本金归还 | 每期还款中归还本金的那部分 |
| **YTM** | Yield to Maturity | 到期收益率 | 持有到期的实际年化回报率；含折扣点时 YTM > 合同利率 |
| **EAY** | Effective Annual Yield | 有效年利率 | 考虑复利效应后的真实年利率；EAY = (1 + i/12)^12 - 1 |
| **i** | Interest rate per period | 每期利率 | 月利率 = 年利率 / 12 |
| **N** | Number of periods | 总期数 | 30年贷款 = 360期（月度）|
| **t** | Time period | 时间期数 | 具体指第几期 |
| **r** | Required return / discount rate | 要求回报率 / 折现率 | 投资者要求的最低回报，用于折现 |
| **g** | Growth rate | 增长率 | NOI 或价值的年增长率 |

---

## 二、抵押贷款 Mortgage

| 缩写 | 英文全称 | 中文 | 解释 |
|------|---------|------|------|
| **CPM** | Constant Payment Mortgage | 等额还款贷款 | 每期还同样金额（PMT）；最常见 |
| **CAM** | Constant Amortization Mortgage | 固定摊销贷款 | 每期还同样本金，利息递减；总还款额前高后低 |
| **IO** | Interest Only | 纯利息贷款 | 每期只还利息，到期一次性还全部本金（balloon）|
| **ARM** | Adjustable Rate Mortgage | 可调利率贷款 | 利率定期随市场指数调整 |
| **FRM** | Fixed Rate Mortgage | 固定利率贷款 | 整个贷款期利率不变 |
| **GPM** | Graduated Payment Mortgage | 渐进还款贷款 | 早期月供低，后期月供高；解决通胀倾斜问题 |
| **LTV** | Loan-to-Value ratio | 贷款价值比 | LTV = 贷款额 / 物业价值；越高风险越高 |
| **LR** | Leverage Ratio | 杠杆率 | LR = V/E = 1/(1-LTV)；注意区别于 LTV |
| **DCR** | Debt Coverage Ratio | 债务覆盖率 | DCR = NOI / 年债务还款；银行审贷标准（通常要求 ≥ 1.2）|
| **BEIR** | Break-Even Interest Rate | 盈亏平衡利率 | 使杠杆恰好无效的借贷利率；= 无杠杆 IRR（rP）|
| **Balloon** | Balloon Payment | 气球还款 | 到期一次性偿还的大额本金（IO 贷款的期末还款）|
| **Teaser Rate** | — | 优惠初始利率 | ARM 初始低利率（吸引借款人），重置后通常大幅上涨 |

---

## 三、房地产投资 Real Estate Investment

| 缩写 | 英文全称 | 中文 | 解释 |
|------|---------|------|------|
| **NOI** | Net Operating Income | 净营业收入 | 租金收入 − 运营费用（不含融资成本和税）|
| **PGI** | Potential Gross Income | 潜在毛收入 | 假设 100% 出租时的总租金收入 |
| **EGI** | Effective Gross Income | 有效毛收入 | EGI = PGI × (1 - 空置率) |
| **OE** | Operating Expenses | 运营费用 | 物业管理、维修、保险、物业税等（不含贷款还款）|
| **Cap Rate** | Capitalization Rate | 资本化率 | Cap Rate = NOI / 价值；用于快速估值 |
| **Going-in Cap Rate** | — | 进入资本化率 | 购买时的 Cap Rate = NOI₁ / 购买价 |
| **Going-out Cap Rate** | — | 退出资本化率 | 出售时的 Cap Rate = NOI_{n+1} / 售价；通常 ≥ Going-in |
| **ERV** | Estimated Rental Value | 估计租金价值 | 物业在当前市场条件下应收的市场租金 |
| **I** | Passing / Income | 当前合同租金 | 租约中实际约定的租金（可能 ≠ ERV）|
| **R** | Reversion / ERV | 市场租金 | 下次租约审查后预期收取的市场租金 |
| **y** | Equivalent Yield / Income yield | 等收益率 / 收益率 | 整体折现率（等收益率法）或当期收入/价格 |
| **n** | Periods to next rent review | 下次租约审查期数 | 等收益率法公式中的时间参数 |
| **GDV** | Gross Development Value | 总开发价值 | 开发完成后物业的预计市场价值 |
| **LTC** | Loan-to-Cost | 开发成本贷款比 | 建设贷款 / 总开发成本；开发融资常用指标 |
| **Pro Forma** | — | 财务预测表 | 列出未来各年 NOI、现金流、IRR 等的预测表格 |

---

## 四、风险与杠杆 Risk & Leverage

| 缩写 | 英文全称 | 中文 | 解释 |
|------|---------|------|------|
| **WACC** | Weighted Average Cost of Capital | 加权平均资本成本 | WACC = LTV × rD + (1-LTV) × rE；物业整体要求回报率 |
| **rP** | Property return | 物业无杠杆回报率 | 不用贷款时物业本身的 IRR |
| **rD** | Debt return / interest rate | 债务利率 | 贷款的实际利率 |
| **rE** | Equity return | 股权回报率 | 股权投资者实际获得的 IRR（含杠杆效应）|
| **D** | Debt | 债务 | 贷款金额 |
| **E** | Equity | 股权 | 自有资金（= 物业价值 - 贷款额）|
| **V** | Value | 价值 | 物业总价值（V = D + E）|
| **RP** | Risk Premium | 风险溢价 | 超过无风险利率的额外回报要求 |
| **RPP** | Risk Premium on Property | 物业风险溢价 | 持有物业要求的风险溢价 |
| **RPD** | Risk Premium on Debt | 债务风险溢价 | 贷款方要求的风险溢价（无风险债务时 = 0）|
| **RPE** | Risk Premium on Equity | 股权风险溢价 | 股权方要求的风险溢价；RPE = RPD + LR × (RPP - RPD) |
| **rf** | Risk-free rate | 无风险利率 | 通常用国债利率（如英国国债）|
| **yP / yD / yE** | Property / Debt / Equity yield | 物业/债务/股权收益率 | 各方的当期现金回报率 |
| **gP / gD / gE** | Property / Debt / Equity growth | 物业/债务/股权增值率 | 各方资本增值的速率 |
| **SD** | Standard Deviation | 标准差 | 回报率的波动程度（风险绝对量）|
| **CoV** | Coefficient of Variation | 变异系数 | CoV = SD / E(IRR)；每单位期望回报承担多少风险 |
| **E(IRR)** | Expected IRR | 期望 IRR | 加权平均回报：Σ Pᵢ × IRRᵢ |

---

## 五、私募股权 Private Equity

| 缩写 | 英文全称 | 中文 | 解释 |
|------|---------|------|------|
| **PE** | Private Equity | 私募股权 | 非公开市场的股权投资 |
| **LP** | Limited Partner | 有限合伙人 | 出资方，不参与日常管理，风险有限 |
| **GP** | General Partner | 普通合伙人 | 基金管理方，承担无限责任，赚取管理费 + Promote |
| **Pref** | Preferred Return | 优先回报 | LP 优先收到的最低回报率（如 8%），达到后才给 GP Promote |
| **Promote** | — | 超额收益分成 | GP 在超过 Pref 后获得的额外分成（激励费）|
| **Hurdle Rate** | — | 门槛收益率 | 同 Pref；GP 赚 Promote 的最低前提条件 |
| **Waterfall** | — | 瀑布分配 | 资金分配顺序：LP Pref → GP Pref → 剩余按比例分 |
| **MOIC** | Multiple on Invested Capital | 投资倍数 | 总回收 / 总投入；MOIC = 2× 表示翻倍 |
| **AUM** | Assets Under Management | 管理资产规模 | GP 管理的总资产金额 |
| **Lookback** | — | 回溯条款 | 确保 LP 达到目标 IRR（如 10%）后，剩余全归 GP |
| **Clawback** | — | 追回条款 | 若基金整体表现差，GP 须退还之前多领的 Promote |

---

## 六、证券化与 MBS Securitisation & MBS

| 缩写 | 英文全称 | 中文 | 解释 |
|------|---------|------|------|
| **MBS** | Mortgage-Backed Securities | 抵押贷款支持证券 | 以抵押贷款池为担保发行的债券 |
| **RMBS** | Residential MBS | 住宅抵押贷款支持证券 | 底层资产为住宅贷款的 MBS |
| **CMO** | Collateralized Mortgage Obligation | 担保抵押贷款债券 | 将 MBS 进一步分层（Tranche）的结构化产品 |
| **GSE** | Government-Sponsored Enterprise | 政府支持企业 | 如 Fannie Mae、Freddie Mac；有隐性政府担保 |
| **G-Fee** | Guarantee Fee | 担保费 | GSE 收取的信用风险承担费用 |
| **CPR** | Conditional Prepayment Rate | 条件提前还款率 | 年化的提前还款速度 |
| **PSA** | Public Securities Association | 公共证券协会 | PSA 标准：前30个月 CPR 线性升至 6%，之后维持 |
| **PAC** | Planned Amortization Class | 计划摊销类 | CMO 中受保护的分层，在一定 PSA 范围内还款稳定 |
| **Tranche** | — | 分层 | CMO 中按风险/优先级划分的不同投资层 |
| **Senior** | — | 优先层 | 最先收到还款，最后承担损失；风险最低 |
| **Junior / Equity** | — | 次级层 | 最后收到还款，最先承担损失；风险最高 |

---

## 七、REITs 与间接投资

| 缩写 | 英文全称 | 中文 | 解释 |
|------|---------|------|------|
| **REIT** | Real Estate Investment Trust | 房地产投资信托 | 上市交易的房地产基金，解决流动性/不可分割性/信息不对称 |
| **NAV** | Net Asset Value | 净资产价值 | NAV = 资产总价值 - 负债；REIT 定价常与 NAV 比较 |
| **FFO** | Funds from Operations | 营运资金 | FFO = 净利润 + 折旧（剔除折旧影响的真实运营现金流）|
| **Discount to NAV** | — | NAV 折价 | REIT 股价低于每股 NAV；常见于市场悲观时 |
| **Premium to NAV** | — | NAV 溢价 | REIT 股价高于每股 NAV；常见于市场乐观时 |

---

## 八、税务 Taxation

| 缩写 | 英文全称 | 中文 | 解释 |
|------|---------|------|------|
| **CGT** | Capital Gains Tax | 资本利得税 | 出售资产时对增值部分征收的税 |
| **t** | Tax rate | 税率 | 应税收入或资本利得适用的税率 |
| **Depreciation** | — | 折旧 | 建筑价值按年分摊的税前扣除项（直线法 = 等额摊销）|
| **Tax Shield** | — | 税盾 | 折旧或利息支出可扣税，减少实际税负 |

---

## 九、计算器专用术语 Calculator Terms (Casio fx-83GT CW)

| 符号/键 | 含义 | 用途 |
|--------|------|------|
| **EXE** | Execute | 确认计算 |
| **AC** | All Clear | 清除全部 |
| **ANS** | Answer | 引用上一步计算结果 |
| **SHIFT** | — | 调出第二功能 |
| **ALPHA** | — | 输入字母变量名 |
| **x^y** | Power | 幂运算（如 1.005^360）|
| **√** | Square root | 开方 |
| **A, B, C, D, X, Y** | Variable memory | 存储中间计算结果 |

---

## 十、快速对照：常见混淆对

| 容易混淆 | 区别 |
|---------|------|
| **LTV vs LR** | LTV = D/V（贷款/价值）；LR = V/E = 1/(1-LTV)（杠杆倍数）|
| **Cap Rate vs IRR** | Cap Rate 只看 Year 1 NOI；IRR 考虑全部持有期现金流 |
| **rP vs rE** | rP = 无杠杆物业回报；rE = 有杠杆股权回报（更高或更低）|
| **Going-in vs Going-out** | Going-in = 买入时；Going-out = 卖出时（通常更高）|
| **I vs R（等收益率法）** | I = 当前合同租金 Passing Rent；R = 市场租金 ERV |
| **PMT vs AMORT** | PMT = 总还款额；AMORT = PMT 中的本金部分（PMT = 利息 + AMORT）|
| **LP vs GP** | LP = 出钱的投资者；GP = 管理基金的人 |
| **Pref vs Promote** | Pref = LP 优先分到的；Promote = GP 超额后才拿的 |
| **NOI vs CF** | NOI = 运营层面（不含融资）；CF = 实际到手现金（NOI - 贷款还款）|
| **BEIR vs WACC** | BEIR = rP（无杠杆 IRR）；WACC 是要求回报率（考虑融资成本）|

---

*持续更新 | GY462 Real Estate Finance | Last Updated: 2026年5月*
