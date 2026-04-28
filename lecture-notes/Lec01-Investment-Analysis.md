# Lecture 1 — 投资分析基础 Investment Analysis

## 核心主题 Key Topics
房地产金融导论、收益性物业类型、DCF 估值方法、折现率选取、租约内/租约间折现率

---

## 1. 房地产特性 Characteristics of Real Estate

与其他金融资产的区别 Differences from other financial assets：
- **不可分割性 Indivisibility**：大宗交易，难以分拆
- **异质性 Heterogeneity**：每套物业独一无二
- **流动性差 Illiquidity**：交易慢、成本高，私下交易为主
- **高交易成本 High transaction costs**

---

## 2. 收益性物业类型 Income-Producing Property Types

| 类型 Type | 特点 Notes |
|-----------|-----------|
| 办公 Office | 核心 CBD vs 郊区；大租户 vs 多租户 |
| 零售 Retail | 购物中心 vs 商业街；锚定租户重要性 |
| 住宅 Residential/Multifamily | 高层公寓、小户型 |
| 工业/仓储 Industrial/Warehouse | 近高速出入口为佳 |
| 酒店 Hotel | 极难估值，Cap Rate 差异巨大 |

**三大影响维度：Location（位置）、Structure（结构）、Tenants（租户）**

---

## 3. DCF 估值法 Discounted Cash Flow Valuation

**步骤 Steps：**
1. 预测未来现金流 Forecast future cash flows
2. 确定折现率 Ascertain required rate of return
3. 折现至现值 Discount to PV

```
PV = Σ [CF_t / (1 + r)^t]
```

**考试核心例题：Single Tenant Office Building**
```
CF: Year 1-3 = 1.0,  Year 4-6 = 1.5,  Year 6 + Sale = 15
r = 10%
PV = 13.757
```

---

## 4. 折现率 Discount Rate

```
r = r_f + RP
```
- **r_f**：无风险利率 Risk-free rate（国债收益率 Treasury bill yield）
- **RP**：风险溢价 Risk premium（非绝对风险，而是对投资组合的边际贡献）

折现率应反映：
- 项目风险特征 Risk characteristics
- 资本机会成本 Opportunity cost of capital
- 同类投资的替代回报 Alternative comparable investments

---

## 5. 租约内 vs 租约间折现率 Intra vs Inter-Lease Discount Rate ⭐

| | 租约内 Intra-Lease | 租约间 Inter-Lease |
|--|-------------------|-------------------|
| 含义 | 现有合同期内 | 合同到期后/重新出租 |
| 风险 | 租户违约风险 Tenant default risk | 市场风险 + 未来出租不确定性 |
| 折现率 | **低** (如 8%) | **高** (如 15%) |

**核心公式（五步法）：**
```
Step 1: PV(第一段租约)  用 intra-lease rate 折现
Step 2: PV(第二段租约) 在第二段开始时  用 intra-lease rate
Step 3: 将 Step 2 结果折回现在  用 inter-lease rate
Step 4: PV(售价) 用 inter-lease rate
Step 5: 总价值 = Step1 + Step3 + Step4
```

**例题结果：** 简单法 13.058 vs 精确法 13.454（差额 £396,000）

> **考试要点**：会考五步法计算，也会考简单法 vs 精确法的区别和原因

---

## 6. 其他估值方法 Alternative Valuation Methods

| 方法 Method | 逻辑 Logic |
|------------|-----------|
| 销售比较法 Sales Comparison | 参考近期类似物业成交价，调整差异 |
| 建设成本法 Construction Cost | 重建成本（含折旧）作为上限 |

---

## 考试高频考点 Exam Focus Points

> **历年真题分析 Based on Past Exams 2013–2025**

1. **RE 主要风险 Main Risks** ★★★★★ — 出现于**每年** Theory Q1（2013–2025）
   - 空置、流动性差、经营成本、租赁违约、自然灾害、信息不对称
   - 必须区分"房地产特有风险"vs"其他金融资产共有风险"

2. **RE 主要机会 Opportunities** ★★★★ — 2013, 2014, 2015, 2018, 2022, 2023, 2025
   - 租金增值、资产升值、运营管理协同效应（租金价值 > 售价重要）

3. **流动性差/不可分割性 Illiquidity / Indivisibility** ★★★★ — 2019, 2020, 2023, 2025
   - 三大特征：Indivisibility（大宗交易）、Illiquidity（难变现）、Large-lot size
   - 这些特征使杠杆成为不可避免的选择，进一步放大风险

4. **DCF 方法如何体现风险与机会** ★★★★ — 2013, 2014, 2019, 2021, 2025
   - 分子（NOI）= 机会；分母（折现率）= 风险
   - 同一资产不同租约段用不同折现率（Intra vs Inter-Lease）

5. **Intra/Inter-Lease 折现率五步法** ★★ — 明确计算出现于 2016
   - Intra-lease（签约期内）：低折现率（租户违约风险低）
   - Inter-lease（租约间/未来重新出租）：高折现率（市场风险高）

6. **物业类型特征 Property Types（Office/Retail/Industrial）** ★★ — 2013, 2014, 2015
   - 位置、结构、租户特征对 Cap Rate 和风险的影响
