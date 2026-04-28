# Lecture 2 — 快捷估值法与Pro Forma Shortcut Valuation & Pro Forma

## 核心主题 Key Topics
资本化率、Gordon 模型、等收益率法、Pro Forma 现金流预测、NPV/IRR 投资法则

---

## 1. 快捷估值法概览 Shortcut Methods Overview

| 方法 | 英文 | 核心公式 |
|------|------|---------|
| 直接资本化法 | Direct Capitalisation (Cap Rate) | V = NOI / Cap Rate |
| 毛收入乘数法 | Gross Income Multiplier (GIM) | V = GIM × Gross Income |
| 等收益率法 | Equivalent Yield | 英国常用，见下 |

---

## 2. 资本化率 Cap Rate ⭐

```
Cap Rate = NOI / V

V = NOI / Cap Rate
```

### 关键术语 Key Terminology
- **Going-in Cap Rate**：投资初始资本化率 = Year-1 NOI / Purchase Price
- **Going-out (Terminal) Cap Rate**：退出资本化率 = Year-11 NOI / Exit Price
- **Stabilised Cap Rate**：稳定运营时的资本化率

> **规律**：Cap Rate ↑ → 物业价值 ↓（反比关系）
> Going-out cap ≥ Going-in cap（物业老化、不确定性增加）

### Cap Rate 与风险
- 低 Cap Rate：高价值物业，增值潜力强，优质地段
- 高 Cap Rate：风险大，不确定性高，流动性差

### 美国典型 Cap Rate 参考（Linneman 2013）
| 物业类型 | Cap Rate |
|---------|---------|
| 核心 CBD 办公（A 级） | 7–8% |
| 郊区办公 | 7.5–9% |
| A 级购物中心 | 7.5–8.5% |
| A 级公寓 | 7–8% |
| 优质仓储 | 8–9.5% |
| 酒店 | 极难估值，差异巨大 |

---

## 3. Gordon 模型（增长型永续年金）Gordon Model ⭐

适用于现金流稳定或以固定比率增长的物业：

```
V = CF₁ / (r - g)

Cap Rate = r - g
```
- **r**：必要回报率 Required return
- **g**：NOI 增长率 Growth rate of NOI

**例：** Building B，r = 12%，g = 2%，NOI₁ = 1  
→ Cap Rate = 10%，V = 1/0.10 = 10

> **关键前提**：g < r；NOI 增长稳定；否则需做完整 DCF

---

## 4. 等收益率法 Equivalent Yield（英国常用）

```
V = I/y + (R - I) / [y × (1 + y)^n]
```
- **I**：当前租金 Passing rent
- **R**：市场估计租金 Estimated Rental Value (ERV)
- **y**：等收益率 Equivalent yield
- **n**：下次租约审查期限

---

## 5. Pro Forma 现金流预测 Pro Forma Cash Flow

### 经营现金流 Operating CF
```
潜在总收入 PGI  (Potential Gross Income = Rent × SF)
- 空置损失 V    (Vacancy = Vacancy Rate × PGI)
+ 其他收入 OI   (Other Income)
- 运营费用 OE   (Operating Expenses)
= 净营业收入 NOI (Net Operating Income)
- 资本改善支出 CI (Capital Improvement Expenditures)
= 税前现金流 PBTCF (Property Before-Tax Cash Flow)
```

### 退出现金流 Reversion CF
```
售价 Property Value at Sale
- 销售费用 SE (Selling Expenses)
= 税前现金流 PBTCF
```

### 运营费用 Operating Expenses 包含：
- **固定 Fixed**：物业税、保险、安保、物业管理（即使自管也要算）
- **可变 Variable**：维修、租户未付的水电

### 资本改善支出 Capital Improvements 包含：
- 租户改善支出 Tenant Improvements (TIs)
- 中介佣金 Leasing Commissions
- 重大维修/设备更换

### 转售价值估算 Resale Value
```
转售价 = Year(n+1) NOI / Going-out Cap Rate
```
Going-out ≥ Going-in cap（一般原则）

---

## 6. 投资决策法则 Investment Decision Rules

### NPV 法则
```
NPV (Buyer) = Market Value - Price
NPV (Seller) = Price - Market Value
```
- NPV > 0 → 投资
- 正常市场中 NPV ≈ 0（买卖双方均衡）

### IRR 法则
```
IRR = 使 NPV = 0 的折现率
规则: IRR > Hurdle Rate → 投资
```
**计算器输入法（TI BA II Plus）：**
```
CF0 = -初始投资
C01, F01 = 第1段现金流及期数
C02, F02 = 第2段现金流及期数
...最后一期 = 最后现金流 + 售价
IRR CPT → 得出IRR
```

### 识别"好得离谱"的交易 Red Flags
- 历史成本计算土地（低估）
- 租金增长率 > 费用增长率（不合理）
- 空置率假设过低
- 退出 Cap Rate 过低
- 低估销售费用

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
