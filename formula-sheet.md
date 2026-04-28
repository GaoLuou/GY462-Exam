# GY462 Real Estate Finance — 公式速查表 Formula Sheet

---

## 货币时间价值 Time Value of Money

### 现值 Present Value
```
PV = FV / (1 + r)^n
```

### 终值 Future Value
```
FV = PV × (1 + r)^n
```

### 年金现值 Annuity (PV of stream of payments)
```
PV = C × [1 - 1/(1+r)^n] / r
```

### 永续年金 Perpetuity
```
PV = C / r
```

### 增长型永续年金 Growing Perpetuity
```
PV = C / (r - g)       条件 g < r
```

---

## 折现现金流估值 DCF Valuation

### 净现值 NPV
```
NPV = Σ [CF_t / (1 + r)^t] - 初始投资
NPV(买方) = 市场价值 - 成交价
NPV(卖方) = 成交价 - 市场价值
```

### 内部收益率 IRR (Internal Rate of Return)
```
令 NPV = 0 时的折现率即为 IRR
规则: IRR > 必要回报率 hurdle rate → 投资
```

### 折现率 Discount Rate
```
r = r_f + RP
r_f = 无风险利率 risk-free rate
RP  = 风险溢价 risk premium
```

---

## 估值捷径 Valuation Shortcuts

### 资本化率 Cap Rate
```
Cap Rate = NOI / V
V = NOI / Cap Rate
```

### 戈登模型 Gordon Model
```
V = CF₁ / (r - g)
Cap Rate = r - g
```

### 等收益率法 Equivalent Yield (UK)
```
V = I/y + (R - I) / [y × (1 + y)^n]
I = 当前租金 passing rent
R = 市场估计租金 ERV
y = 等收益率 equivalent yield
```

---

## Pro Forma 现金流 Cash Flow

### 经营现金流 Operating CF
```
PGI  潜在总收入 Potential Gross Income
- V  空置损失 Vacancy (= Vacancy Rate × PGI)
+ OI 其他收入 Other Income
- OE 运营费用 Operating Expenses
= NOI 净营业收入 Net Operating Income
- CI 资本改善支出 Capital Improvements
= PBTCF 税前现金流
```

### 退出现金流 Reversion CF
```
转售价 = Year(n+1) NOI / Going-out Cap Rate
PBTCF(R) = 转售价 - 销售费用
```

---

## 财务杠杆 Financial Leverage

### 基本关系 Basic Relations
```
V = D + E
LTV = D / V    贷款价值比
LR  = V / E = 1 / (1 - LTV)    杠杆率
```

### WACC（税前）Before-Tax
```
rP = LTV × rD + (1 - LTV) × rE
⟹ rE = rP + (rP - rD) × (D/E)
```

### WACC（税后）After-Tax
```
rE = rP + (rP - rD×(1-t)) × (D/E)
```

### 收益率分解 Yield Decomposition
```
r = y + g
yE = (yP - LTV × yD) / (1 - LTV)    现金回报率 Cash-on-Cash Yield
gE = (gP - LTV × gD) / (1 - LTV)    股权增值率
```

### 杠杆与风险 Leverage & Risk
```
RPE = RPD + LR × (RPP - RPD)
若 RPD = 0: RPE = LR × RPP   (股权风险与杠杆成正比)
```

### 盈亏平衡利率 BEIR
```
BEIR = ATIRRP / (1 - t)
借款利率 > BEIR → 杠杆不利
```

---

## 抵押贷款 Mortgage

### CPM 月供 Constant Payment Mortgage
```
PMT = BAL₀ × i / [1 - (1 + i)^(-N)]
i = 月利率 = 年利率 / 12
N = 总期数
```

### 剩余余额 Remaining Balance
```
BALₜ = PMT × [1 - (1 + i)^(-(N-t))] / i
```

### 有效年利率 EAY
```
EAY = (1 + i/12)^12 - 1
```

### 实际借款成本 Effective Cost of Borrowing
```
CF0 = -(贷款额 - 折扣点 - 其他费用)
C01~CN = 月供 PMT
IRR CPT → 月 YTM → 年化
YTM > 合同利率
```

### Fisher 方程 通胀调整
```
(1 + 名义利率) = (1 + 实际利率) × (1 + 通胀率)
```

---

## 私募股权 Private Equity

### 瀑布分配 Waterfall
```
第1层: LP 获得 Pref
第2层: 超额利润 (1-Promote%) → LP，Promote% → GP
```

### IRR 偏好 IRR Preference
```
先确保 LP 达到目标 IRR，剩余按约定比例分
```

---

## 风险评估 Risk Assessment

### 敏感性分析 Sensitivity Analysis
```
E(IRR) = Σ Prᵢ × IRRᵢ
Var    = Σ Prᵢ × (IRRᵢ - E(IRR))²
SD     = √Var
CoV    = SD / E(IRR)
```

---

## 开发项目 Development

### 10/8 法则 Build-at-10, Sell-at-8
```
Going-in yield = 稳定 NOI / 总开发成本 ≥ 10%
Going-out CR   = 稳定 NOI / 出售价格 ≈ 8%
利润 ≈ NOI × (1/8% - 1/10%) = NOI × 2.5 (约 25% 利润率)
```

### 替代租金 Replacement Rent
```
替代租金 = (目标 NOI + 运营成本) / (1-Loss Factor) / (1-空置率)
```

---

## 关键结论 Key Takeaways

| 关系 Relationship | 公式 Formula |
|-------------------|-------------|
| Cap Rate ↑ → 价值↓ | V = NOI / Cap Rate |
| 正杠杆条件 | rP > rD（税后：rP > rD×(1-t)） |
| Going-out ≥ Going-in | 物业老化，不确定性增加 |
| 杠杆放大风险 | RPE = LR × RPP |
| 增长越快 → Cap Rate 越低 | Cap Rate = r - g |
