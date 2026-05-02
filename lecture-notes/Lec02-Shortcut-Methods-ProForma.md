# Lecture 2 — 快捷估值法与Pro Forma Shortcut Valuation & Pro Forma

## 核心主题 Key Topics
资本化率、Gordon 模型、等收益率法、Pro Forma 现金流预测、NPV/IRR 投资法则

---

## 1. 快捷估值法概览 Shortcut Methods Overview

**为什么需要快捷法？** DCF 方法准确但繁琐——需要预测 10 年现金流、选折现率、做敏感性分析。实践中，投资者常用"快捷法"进行**初步筛选**，快速判断一个物业值不值得深入研究。

| 方法 | 英文 | 核心公式 | 适用场景 |
|------|------|---------|--------|
| 直接资本化法 | Direct Capitalisation (Cap Rate) | V = NOI / Cap Rate | 稳定物业，快速估值 |
| 毛收入乘数法 | Gross Income Multiplier (GIM) | V = GIM × Gross Income | 住宅类物业 |
| 等收益率法 | Equivalent Yield | 英国常用，见下 | 英国商业地产 |

---

## 2. 资本化率 Cap Rate（直接资本化法）⭐

### 什么是 Cap Rate？

**Cap Rate（资本化率）**，全称 Capitalization Rate，是衡量物业收益水平的核心指标，定义如下：

```
Cap Rate = NOI / V

即：Cap Rate = 净营业收入 / 物业价值
```

这里：
- **NOI（Net Operating Income，净营业收入）**：年租金收入扣除物业运营费用后的净额（不含贷款利息、税收）
- **V（Value）**：物业市场价值（或购入价）

反过来，用来估值：

```
V = NOI / Cap Rate
```

> **类比**：Cap Rate 就像债券的"收益率"（Yield）。一只债券价格越高，收益率越低。同理，物业价值越高，Cap Rate 越低。

### Cap Rate 与风险的反向关系

| Cap Rate | 物业特征 |
|----------|---------|
| **低 Cap Rate**（如 4–6%）| 高价值物业，地段优越，租户信用好，升值预期强；投资者愿意用低收益换低风险 |
| **高 Cap Rate**（如 9–12%）| 风险较高，地段差，空置率高，或市场不确定性大；投资者要求更高收益补偿 |

**举例理解：** 自然灾害后（如新奥尔良卡特里娜飓风），当地 Cap Rate 飙升——因为物业价值崩溃（V 下跌），即使 NOI 不变，Cap Rate = NOI/V 也大幅升高。

### 关键术语 Key Terminology

```
Going-in Cap Rate（进入资本化率）= Year-1 NOI / 购入价
→ 投资初期的收益率水平

Going-out（Terminal）Cap Rate（退出资本化率）= Year-11 NOI / 出售价
→ 投资结束时（卖楼时）的预期收益率

Stabilised Cap Rate（稳定资本化率）= 稳定运营时 NOI / 价值
→ 物业达到正常出租水平时的资本化率
```

> **重要规律**：通常 Going-out Cap Rate ≥ Going-in Cap Rate。
> **为什么？** 楼宇老化（物理折旧）、未来不确定性更大，投资者要求更高回报，因此卖出时价值相对 NOI 更低（即 Cap Rate 更高）。
> **如何仍能赚钱？** 如果持有期间 NOI 增长幅度足够大，即使 Cap Rate 上升，出售价格仍可高于买入价。

### Cap Rate 计算例题

**例：** 某单一租户办公楼市场的 Going-in Cap Rate 为 7.5%，该楼第一年 NOI = £1M

```
V = NOI / Cap Rate = 1 / 0.075 = £13.333M
```

### 美国典型 Cap Rate 参考（Linneman 2013，2010年4月数据）

| 物业类型 | Cap Rate | 原因说明 |
|---------|---------|--------|
| 核心 CBD 办公（A 级） | 7–8% | 优质地段，大租户，流动性好 |
| 郊区办公 | 7.5–9% | 流动性稍差，租户较小 |
| 二线城市办公 | 8.5–12% | 市场薄，租约到期集中 |
| A 级公寓（Garden Apartments） | 7–8% | 好地段，现代设计 |
| B 级公寓 | 8–9.5% | |
| C 级公寓 | 9–12% | |
| A 级购物中心（有超市锚定） | 7.5–8.5% | 客流稳定，入驻率高 |
| B 级购物中心 | 8.5–11% | |
| C 级购物中心（空置多） | 10–14% | |
| 优质仓储（靠近高速） | 8–9.5% | |
| 差位置仓储 | 9–12% | |
| 酒店 | N/A | 极难估值，Cap Rate 差异极大 |

---

## 3. Cap Rate 的局限性与 Gordon 模型修正 ⭐

### 局限性："近视"问题（Myopia Problem）

Cap Rate 只用**第一年** NOI 来估值，忽略了未来 NOI 的增长。这会导致对不同增长前景的物业错误定价。

**数字例子：** 两栋风险相同的楼，A 和 B，折现率均为 12%

| 年份 | 楼 A (NOI, 无增长) | 楼 B (NOI, 每年增长 2%) |
|------|-------------------|----------------------|
| 1 | 1.000 | 1.000 |
| 2 | 1.000 | 1.020 |
| 3 | 1.000 | 1.040 |
| ... | ... | ... |

若直接套用相同 Cap Rate，两楼估值相同。但用 DCF 正确计算：

```
V_A = 1 / 0.12 = 8.33（用永续年金公式，g=0）
V_B = 1 / (0.12 - 0.02) = 1 / 0.10 = 10.00（增长型永续年金）
```

结论：**楼 B 应该贵 20%！** 如果用同一 Cap Rate，会系统性低估高增长物业，这就是 Cap Rate 的"近视"缺陷。

### Gordon 模型（增长型永续年金）修正

当 NOI 以固定比率 g 增长时：

```
V = CF₁ / (r - g)

对应的 Cap Rate = r - g

其中：
  r = 必要回报率（折现率）
  g = NOI 年增长率
  CF₁ = 第一年 NOI
```

**验证：** 楼 B 的正确 Cap Rate = 12% - 2% = 10%（而非 12%），对应价值 = 1/10% = 10 ✓

**结论：** Cap Rate = r - g，所以：
- 高增长物业 → 低 Cap Rate（因为 g 大，分母 r-g 小）
- 低增长物业 → 高 Cap Rate

### Gordon 模型的前提条件

```
1. NOI 增长率较为稳定（Stabilised growth）
2. g < r（增长率低于折现率，否则价值无穷大）
3. NOI 增长相对于折现率较小（才能用简单近似）
```

> **如果物业不满足稳定增长假设，必须做完整的多年 DCF 分析！**

---

## 4. 等收益率法 Equivalent Yield（英国常用）

**英国商业地产**最常用的估值方法（而不是美国式 Cap Rate 方法）。

**为什么英国不同？** 英国商业租约（尤其 1980–2000 年代）多为长期"向上调整"租约（upward-only rent reviews），每隔 5 年有一次租金审查（rent review）。等收益率法考虑了"当前合同租金"与"市场租金"之间的差距。

### 公式
```
V = I/y + (R - I) / [y × (1 + y)^n]

其中：
  I = 当前合同租金（Passing Rent / Income）
  R = 市场估计租金（Estimated Rental Value, ERV）
  y = 等收益率（Equivalent Yield）
  n = 下次租金审查距今的年数
```

**直观理解：**
- 第一项 I/y：以当前合同租金为基础的"资本价值"
- 第二项 (R-I)/[y×(1+y)^n]：下次审查时租金会从 I 调整到 R 的"额外价值"折现

---

## 5. Pro Forma 现金流预测 Pro Forma Cash Flow

**什么是 Pro Forma？** 是一份多年期现金流预测表（Multi-year Cash Flow Forecast），向贷款人和外部投资者展示物业未来的财务表现。

Pro Forma 分两种现金流：
1. **经营现金流 Operating Cash Flow**：物业日常运营产生的现金流（每年都有）
2. **退出现金流 Reversion Cash Flow**：物业出售时一次性产生的现金流

---

### 5.1 经营现金流（Pro Forma 各行项目）

```
潜在总收入 PGI  (Potential Gross Income)
    = 满租情况下的总租金收入 = 租金/平方英尺 × 总面积
  
- 空置损失 V    (Vacancy Allowance)
    = 空置率 × PGI
    = 预估多少比例的面积会空置，对应的收入损失
  
+ 其他收入 OI   (Other Income)
    = 停车费、广告位、杂项收入
  
= 有效总收入 EGI (Effective Gross Income)
    = 实际预期能收到的总收入
  
- 运营费用 OE   (Operating Expenses)
    = 维持物业正常运营的费用
  
= 净营业收入 NOI (Net Operating Income)
    = 物业运营层面的净收益（不含贷款偿还）
  
- 资本改善支出 CI (Capital Improvement Expenditures)
    = 一次性大额支出，如装修、更换设备
  
= 税前现金流 PBTCF (Property Before-Tax Cash Flow)
    = 物业实际产生的、税前的净现金流
```

### 5.2 各行项目详解

**PGI（潜在总收入）— "租金清单"（Rent Roll）**
- 逐个租户列出：租约到期日、租金、面积
- 需考虑：租免期（Rent-Free Period，新租户入驻时给的"装修期"）、超额租金（Overage，营业额超标时额外付租）、停车费等其他收入

**空置损失（Vacancy Allowance）**
- 不要假设 100% 出租率！现实中总有部分空置
- 计算：空置率 = 空置月数 / （空置月数 + 出租月数）
- 参考：市场平均空置率 或 该物业历史空置率

**运营费用（Operating Expenses）分两类：**

| 类别 | 内容 |
|------|------|
| **固定 Fixed** | 物业税（Property Taxes）、保险（Hazard Insurance）、物业安保（Security）、物业管理费（即使自己管也要算！） |
| **可变 Variable** | 维修保养（Maintenance & Repairs）、租户没付的水电费（Utilities not paid by tenants） |

> **重要提示**：OE **不包括** 所得税（Income Tax）和折旧（Depreciation）。折旧是会计概念，不是真实现金流出。

**资本改善支出（Capital Improvement Expenditures）**：
- **租户改善支出 TIs（Tenant Improvements）**：为吸引/留住租户，按租户要求进行的定制装修（属于一次性支出）
- **中介佣金 Leasing Commissions**：付给招租中介的费用
- **重大维修 Major Repairs**：更换电梯、重装屋顶等

> **思考题**：这些支出算"费用（Expense）"还是"投资（Investment）"？答案是"投资"——它们带来未来收益（新租约、更高租金），因此单独列示，不计入运营费用。

---

### 5.3 退出现金流（Reversion CF）

```
物业出售价值（Property Value at Time of Sale）
  - 销售费用 SE（Selling Expenses）= 中介费、法律费、印花税等
  = 税前现金流 PBTCF（Reversion）
```

**如何估算转售价格（Resale Value）？** 最常用方法：

```
转售价格 = Year(n+1) NOI / Going-out Cap Rate

例：10 年持有期末出售，用第 11 年 NOI 除以 Going-out Cap Rate
```

> **为什么是第 11 年 NOI，而不是第 10 年？** 因为出售时，买家会根据他**接下来能收到**的 NOI（即第 11 年的）来定价。第 10 年的 NOI 对买家来说是"过去式"。

**重要规律：Going-out Cap Rate ≥ Going-in Cap Rate（通常情况下）**
原因：
1. 物业老化，维修需求增加
2. 租约到期后再出租的不确定性
3. 时间越长，预测越不精准，风险溢价越高

---

## 6. 投资决策法则 Investment Decision Rules

### 6.1 NPV 法则（Net Present Value）

```
NPV（买方）= 市场价值 - 支付价格
NPV（卖方）= 支付价格 - 市场价值
```

**决策规则：**
- NPV > 0 → 买入（你认为物业比标价更值钱）
- NPV < 0 → 不买
- NPV = 0 → 正常市场均衡（买卖双方对物业价值估计一致）

> **关键洞见**：在一个**有效市场**中，NPV 通常 = 0——因为如果 NPV > 0，很多人竞争买，价格被推高直到 NPV = 0。赚钱的机会往往来自信息优势（你比市场更准确地估计了 NOI 或风险）。

### 6.2 IRR 法则（Internal Rate of Return，内部回报率）

```
IRR = 使 NPV = 0 的折现率
即：求 r，使得 PV(所有未来现金流) = 初始投资额
```

**直白理解：** IRR 是"这笔投资实际能给你赚多少年化回报率"。

**决策规则：**
1. IRR > 必要回报率（hurdle rate）→ 投资
2. 在多个投资机会中，**选 IRR - hurdle rate 差距最大**的
3. IRR < hurdle rate → 不投

> **类比**：你要求最低回报 10%（hurdle rate）。投资 A 的 IRR = 15%，超额 5%；投资 B 的 IRR = 13%，超额 3%。选 A。

### 6.3 用计算器计算 IRR（TI BA II Plus）

以之前的 10 年期例子为例（购入价 13.453，现金流如表）：

```
CF Worksheet 操作步骤：
1. 按 CF 键，进入现金流工作表
2. CF0 = -13.45（负号！因为是投资支出）按 ENTER
3. C01 = 1（第1–3年每年1.0）按 ENTER
4. F01 = 3（持续3期）按 ENTER
5. C02 = 1.50（第4–6年）按 ENTER；F02 = 3
6. C03 = 2（第7–9年）按 ENTER；F03 = 3
7. C04 = 22（第10年现金流2.0 + 售价20.0）按 ENTER；F04 = 1
8. 按 IRR，然后 CPT
9. 结果：IRR = 13.13%
```

---

## 7. 识别"好得离谱"的交易 Red Flags — 过于乐观的假设

实践中，有人故意（或无意）在 Pro Forma 中做出过于乐观的假设，使 IRR 虚高。常见陷阱：

| 问题 | 为什么会虚高 IRR |
|------|----------------|
| 土地用历史成本（历史价格）计入 | 低估了当前土地成本，压低了总投资额 |
| 租金增长率 > 费用增长率 | 现实中两者趋同，人为拉大了未来 NOI |
| 遗漏运营费用 | NOI 被高估 |
| 未考虑租金优惠（Rent Concessions） | 实际有效租金低于合同租金（租免期等） |
| 空置率假设过低 | 实际总有空置期 |
| 退出 Cap Rate 设得过低 | 导致终值（售价）被高估 |
| 低估销售费用 | 净退出现金流被高估 |

---

## 考试高频考点 Exam Focus Points

> **历年真题分析 Based on Past Exams 2013–2025**

1. **Pro Forma 构建 + NOI 计算** ★★★★★ — **每年**计算 Q 都有（2013–2025）
   - 典型元素：多租户建筑、租免期（rent-free）、超额租金（overage）、停车费
   - 退出价值：`Year (n+1) NOI / Going-out Cap Rate`（需多算一年）
   - 2020 考了购物中心（3租户）；2013考了办公楼（3租户+overage）

2. **IRR 计算（CF Worksheet）** ★★★★★ — **每年**计算题（2013–2025）
   - 给定购价求 IRR；给定目标 IRR 反算最高购价（用 NPV=0）
   - 注意：计算器使用 CF0, C01/F01, C02/F02... → IRR CPT

3. **Cap Rate 应用与近视性局限** ★★★★ — 2013, 2014, 2015, 2016, 2017, 2019, 2020
   - `V = NOI / Cap Rate`；近视性（不考虑 NOI 增长）
   - Going-in vs Going-out：去出 Cap Rate 一般 ≥ 进入 Cap Rate

4. **Gordon 模型 Cap Rate 修正** ★★★★ — 2013, 2014, 2015, 2020
   - `Adjusted Cap Rate = r - g`；DCF 和 Gordon 法结果一致（增长型永续年金）
   - 2020 明确要求比较"未修正 Cap Rate"和"DCF"对同一物业的估值差异

5. **情景/敏感性分析 Scenario Analysis** ★★★★ — 2013, 2014, 2015, 2016, 2017, 2018, 2020, 2023
   - 变动 Cap Rate（±2%）对 IRR 的影响；E(IRR)、Var、SD、CoV 计算公式
   - 2020 具体要求：三种情景各 1/3 概率，求期望 IRR 和标准差

6. **等收益率法 Equivalent Yield** ★★ — 2013, 2014, 2016（英国早期考题）
   - 区分 term-and-reversion、layer-and-hard core、equivalent/net initial/reversionary yield
