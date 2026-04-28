# GY462 Real Estate Finance — Formula Sheet

## Time Value of Money

### Present Value
```
PV = FV / (1 + r)^n
```

### Future Value
```
FV = PV × (1 + r)^n
```

### Annuity (PV of stream of payments)
```
PV = C × [1 - 1/(1+r)^n] / r
```

### Perpetuity
```
PV = C / r
```

### Growing Perpetuity
```
PV = C / (r - g)        where g < r
```

### Constant Multiple Perpetuity
```
PV = C × M / r          where M = growth multiple per period
```

---

## Valuation

### Direct Capitalisation
```
Value = NOI / Cap Rate
```

### Discounted Cash Flow (DCF)
```
Value = Σ [NOI_t / (1+r)^t] + [Terminal Value / (1+r)^n]
Terminal Value = NOI_(n+1) / (Exit Cap Rate)
```

### Net Operating Income (NOI)
```
NOI = Gross Rental Income
    - Vacancy & Credit Loss
    - Operating Expenses
    (before debt service and tax)
```

---

## Leverage & Capital Structure

### WACC (Weighted Average Cost of Capital)
```
WACC = (E/V) × r_e + (D/V) × r_d × (1 - T)

Where:
  E = equity value
  D = debt value
  V = E + D (total firm value)
  r_e = cost of equity
  r_e = cost of debt
  T = tax rate
```

### Modigliani-Miller (with taxes)
```
V_L = V_U + T × D
(Levered firm value = Unlevered + Tax shield)
```

### Loan-to-Value (LTV)
```
LTV = Loan Amount / Property Value
```

### Debt Service Coverage Ratio (DSCR)
```
DSCR = NOI / Annual Debt Service
(Lenders typically require DSCR ≥ 1.25)
```

### Interest Coverage Ratio
```
ICR = NOI / Interest Expense
```

---

## Returns

### Total Return
```
Total Return = Income Return + Capital Return
Income Return = NOI / Beginning Value
Capital Return = (End Value - Begin Value) / Begin Value
```

### Internal Rate of Return (IRR)
- Rate r such that NPV = 0:
```
0 = Σ [CF_t / (1+r)^t]
```

### Equity Multiple
```
Equity Multiple = Total Equity Distributions / Total Equity Invested
```

---

## Real Estate Specific

### Gross Rent Multiplier (GRM)
```
GRM = Property Price / Gross Annual Rent
```

### Cap Rate
```
Cap Rate = NOI / Property Value
```

### Reversionary Yield
```
Reversionary Yield = ERV / Capital Value
(ERV = Estimated Rental Value at market rent)
```

### Running Yield / Initial Yield
```
Initial Yield = Passing Rent / Capital Value
```

---

## Risk & Beta

### Levered Beta (Hamada Equation)
```
β_L = β_U × [1 + (1-T) × (D/E)]
```

### Unlevered Beta
```
β_U = β_L / [1 + (1-T) × (D/E)]
```

### CAPM
```
r_e = r_f + β × (r_m - r_f)
```

---

## Key Relationships to Remember

1. **Higher cap rate → lower property value** (inverse relationship)
2. **Leverage amplifies both gains and losses**
3. **DSCR < 1** → property cash flow cannot cover debt → default risk
4. **Growing perpetuity requires g < r** otherwise PV → ∞
5. **IRR > hurdle rate → accept investment**
