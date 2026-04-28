# Lecture 3 — 风险评估与杠杆 Risk Assessment & Financial Leverage

## 核心主题 Key Topics
风险评估三法、财务杠杆原理、WACC、正杠杆条件、杠杆与收益率分解

---

## 1. 风险评估方法 Risk Assessment Methods

### 方法一：尽职调查 Due Diligence
- 系统性评估流程，判断投资是否符合目标
- 考察：物业状况、租赁情况、市场供需、法律合规、环境风险
- 对代他人投资的机构尤为重要（问责 accountability）

### 方法二：IRR/PV 分解 Partitioning the IRR/PV
- 分析经营现金流 vs 售价现金流各自贡献比例
- 例：办公楼 PV 中，经营 CF 占 30%，售价 CF 占 70%（不确定性更高）
- 越依赖售价 → 风险越大

### 方法三：敏感性分析 Sensitivity Analysis ⭐
```
E(IRR) = Pr₁×IRR₁ + Pr₂×IRR₂ + Pr₃×IRR₃

Variance = Σ Prᵢ × (IRRᵢ - E(IRR))²
SD = √Variance
CoV (变异系数) = SD / E(IRR)
```
三种情景：悲观 Pessimistic、最可能 Most Likely、乐观 Optimistic

---

## 2. 财务杠杆基础 Financial Leverage Basics

### 为什么使用债务 Why Use Debt？
1. 自有资本不足 Lack of equity
2. 利息税盾 Tax deductibility of interest
3. 正杠杆效应 Positive leverage（借款成本 < 投资回报率）
4. 改变项目风险特征 Change risk profile

### 核心术语 Key Terms
```
资产价值 V = 债务 D + 股权 E
贷款价值比 LTV = D / V
杠杆率 LR = V / E = 1 / (1 - LTV)
```

---

## 3. WACC 加权平均资本成本 ⭐

```
rₚ = LTV × rD + (1 - LTV) × rE

变形得到股权回报率：
rE = rP + (rP - rD) × (D/E)
```

- **rₚ**：物业总回报率
- **rD**：债务成本（利率）
- **rE**：股权回报率

> 只要 rP > rD → 杠杆可以放大股权回报（正杠杆）

### 税后分析 After-Tax WACC
```
税后债务成本 = rD × (1 - Tax Rate)
rE = rP + (rP - rD×(1-t)) × (D/E)
```

**例：** rP = 8.76%，rD = 10%，t = 28%，D/E = 80/20  
→ 税后债务成本 = 7.2% < 8.76%  
→ rE = 8.76 + (8.76 - 7.2) × 4 ≈ 15%

---

## 4. 盈亏平衡利率 Break-Even Interest Rate (BEIR)

```
BEIR = ATIRRP / (1 - t)
```
当借款利率 > BEIR → 杠杆不利

---

## 5. 增量借贷成本 Incremental Cost of Debt

```
增量成本 = (新利息总额 - 旧利息总额) / 额外借款额
```
**例：** 80% loan at 10% vs 85% loan at 10.25%  
→ 额外成本 = (85×10.25% - 80×10%) / 5 = 14.25%

---

## 6. 杠杆与收益率分解 Leverage, Yield & Growth

总回报分解：
```
r = y (收益率/income yield) + g (增值/growth)
r = rf + RP
```

WACC 公式同样适用于各分量：
```
yP = LTV × yD + (1 - LTV) × yE
→ yE = (yP - LTV × yD) / (1 - LTV)   [Cash-on-Cash Yield 现金回报率]

gP = LTV × gD + (1 - LTV) × gE
→ gE = (gP - LTV × gD) / (1 - LTV)   [股权增值收益率]
```

---

## 7. 杠杆与风险 Leverage & Risk ⭐

```
RPE = RPD + LR × (RPP - RPD)

若债务无风险 (RPD = 0):
RPE = LR × RPP
```
→ **股权风险与杠杆率成正比**

### 数值案例对比
| | 无杠杆 Unlevered | 杠杆 90% Levered |
|--|-----------------|-----------------|
| E(BTIRR) | 13.06% | 25.46% |
| Standard Deviation | 3.29% | 18.48% |
| 悲观情景 IRR | 7.93% | **-6.03%** |

**结论**：杠杆 = 放大收益 + 放大风险，没有免费午餐 No free lunch

---

## 日本房地产案例 Japanese Property Case
- LTV = 85%，利率 4%，NOI 增长 -2%/年
- 现金回报率 24%（吸引人），但资产价值下降
- 股权年均资本利得 **-16.6%**（灾难性）
- 教训：高杠杆 + 下跌市场 = 极度放大损失

---

## 考试高频考点 Exam Focus Points

> **历年真题分析 Based on Past Exams 2013–2025**

1. **WACC 公式 + 杠杆放大效应** ★★★★★ — 2013, 2014, 2015, 2017, 2018, 2019, 2020, 2021, 2022, 2025
   - `rE = rP + (rP - rD) × D/E`
   - 注意：WACC 是**近似值**（假设 D/E 不变），全 DCF 才是精确解

2. **杠杆 IRR 计算（全 DCF 方法）** ★★★★★ — **几乎每年**（2013–2025）
   - IO 贷款：CF 中减去利息，期末减去贷款本金（balloon）
   - CPM 贷款：每期减去 PMT，期末减去剩余余额（更复杂）

3. **正/负杠杆条件 Positive/Negative Leverage** ★★★★ — 2013, 2015, 2017, 2018, 2025
   - rP > rD → 正杠杆（杠杆放大收益）
   - rP < rD → 负杠杆（杠杆放大损失，如 2013 年租金下降情景 IRR = -18.6%）

4. **情景分析 E(IRR)、Var、SD** ★★★★ — 2013, 2014, 2015, 2016, 2018
   - 两情景：E(IRR) = 50%×IRR₁ + 50%×IRR₂；SD 计算后比较有/无杠杆下的风险放大

5. **Cash-on-Cash Yield + Growth Yield** ★★★ — 2014, 2015, 2018
   - `yE = (yP - LTV×yD) / (1-LTV)`；增值收益率用初/末股权价值年化
   - 2015 考了 95% LTV 下资产价值低于贷款额（负股权）的极端情景

6. **税后 IRR After-Tax Analysis** ★★★ — 2013, 2014, 2016, 2018, 2019
   - 建筑折旧（直线法）抵税；利息税盾；资本利得税
   - 2019 有完整税后 IRR 推导题，含折旧、利息扣除、含资本利得

7. **BEIR 盈亏平衡利率** ★★ — 明确出现于 2013
   - BEIR = 无杠杆 IRR；在 BEIR 借款则杠杆无效；低于 BEIR 才有利
