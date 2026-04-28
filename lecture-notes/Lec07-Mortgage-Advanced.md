# Lecture 7 — 抵押贷款进阶 Mortgage: Advanced Topics

## 核心主题 Key Topics
提前还款罚金、通胀与还款、渐进还款抵押贷款（GPM）、可调利率抵押贷款（ARM）

---

## 1. 提前还款罚金 Prepayment Penalties

提前还款会使贷款方收入减少，因此设定罚金。

### 计算实际成本（含罚金）
```
CF0 = -(贷款额 - 折扣点)
C01~C(n-1) = 月供 PMT
C(n) = PMT + 剩余余额 BAL + 罚金
IRR CPT → 月 YTM
```

### 收益率维持条款 Yield Maintenance
- 贷款方要求借款人补偿提前还款导致的利息损失
- 补偿金额 = PV(剩余应付利息差额，用国债利率折现)

---

## 2. 通胀对抵押贷款的影响 Inflation & Mortgage Payments ⭐

### 实际利率 Fisher 方程
```
(1 + 名义利率) = (1 + 实际利率) × (1 + 通胀率)
名义利率 ≈ 实际利率 + 通胀率
```

**例：** 实际利率 4%，通胀 6%
```
名义利率 = (1.04 × 1.06) - 1 = 10.24%
无通胀月供 PMT = £286.45
有通胀月供 PMT = £537.21（高 87.5%）
```

### "倾斜问题" Tilt Problem
```
高通胀 → 高名义月供 → 早期实际还款负担重
         → 越来越多借款人无法资格达标（qualify）
随时间推移：通胀侵蚀名义月供实际价值 → 后期实际负担轻
```

| 时间 | 名义月供 | 实际月供（通胀调整） |
|------|---------|-----------------|
| 初期 | 高 | **非常高** |
| 后期 | 不变 | **逐渐降低** |

---

## 3. 渐进还款抵押贷款 GPM (Graduated Payment Mortgage)

### 解决问题
缓解早期还款压力过重（Tilt Problem）

### 运作机制
```
早期月供 < 标准 CPM 月供（甚至可能 < 当期利息）
→ 负摊销 Negative Amortization（余额短期增加）
后期月供 > 标准月供
```

### 权衡 Trade-off
- 优点：早期还款少，改善可及性（affordability）
- 缺点：总利息支出增加；初期余额可能增大

### 计算器计算步骤
```
第1-n年：低月供 PMT₁
第n+1年起：高月供 PMT₂
分两段用 CF Worksheet 计算 IRR / PV
```

---

## 4. 可调利率抵押贷款 ARM (Adjustable Rate Mortgage)

### 解决问题
降低利率风险（对贷款方而言），提供初期低利率（对借款方吸引力）

### 关键特征
```
初始利率（Teaser Rate）：通常低于固定利率
调整频率：每年、每3年、每5年（5/1 ARM = 前5年固定，之后每年调整）
基准利率 Index：LIBOR、SOFR、1年期国债利率
加成 Margin：Index + Margin = 当期利率
```

### 利率上限 Rate Caps
```
Period Cap：每次调整最大变动（如 ±2%）
Life Cap：整个贷款期利率最大变动（如 ±6%）
```

### 实际成本计算（ARM）
```
分段计算：
每个调整期用各自利率和对应月供
用 CF Worksheet 计算整体 IRR
```

---

## 5. 固定利率 vs 可调利率选择 FRM vs ARM Decision

| | 固定利率 FRM | 可调利率 ARM |
|--|------------|------------|
| 利率风险 | 借款人承担 | 贷款方承担 |
| 初期月供 | 较高 | 较低 |
| 适合场景 | 长期持有、利率上行预期 | 短期持有、利率下行预期 |
| 可预测性 | 高 | 低 |

---

## 6. 有效抵押贷款成本汇总 Effective Cost Summary

影响实际借款成本的因素：
```
实际成本 (YTM) > 合同利率，因为：
1. 折扣点 Discount Points（降低净到手金额）
2. 其他手续费 Origination Fees
3. 提前还款罚金 Prepayment Penalties
4. 持有期越短 → 实际成本越高
```

---

## 考试高频考点 Exam Focus Points
1. 通胀对名义/实际月供的影响（Fisher 方程）
2. Tilt Problem 的含义和 GPM 的解决方案
3. ARM 的关键特征：Index、Margin、Cap
4. 提前还款罚金对 YTM 的影响计算
5. FRM vs ARM 的风险归属对比
