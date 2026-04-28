# Lecture 9 — 债务证券化与MBS Debt Securitisation & MBS

## 核心主题 Key Topics
二级抵押贷款市场起源、RMBS 运作机制、GSE 角色、MBS 风险类型、CMO/优先劣后结构

---

## ⚠️ 考试特别提示
> Lecture 9 讲义第3页明确：**考试 2 道题，一道偏理论，一道偏计算**
> **必须用金融计算器（TI BA II Plus），不允许 Excel**

---

## 1. 二级市场起源 Why Did Secondary Market Emerge?

### 背景：大萧条（1929-1939）
- 美国 1/3 银行倒闭
- 50% 抵押贷款违约率
- 私人贷款机构无法稳定供应信贷

### 传统贷款问题（大萧条前）
- 首付 40-50%
- 纯利息贷款（到期一次还本）
- 3-5 年期限，到期再融资风险高
- 美国租房率约 45%

### 二级市场的解决方案
1. **补充资金来源**：贷款机构出售贷款 → 获得新资金再放贷
2. **风险转移**：从贷款机构转移至证券投资者
3. **专业化分工**：贷款发放、服务、投资各自专业化

---

## 2. 美国 GSE 发展时间线

| 年份 | 事件 |
|------|------|
| 1938 | FNMA（联邦国家抵押贷款协会）成立 |
| 1968 | FNMA 拆分为 Fannie Mae（私有化）和 Ginnie Mae |
| 1970 | Freddie Mac 成立（提供竞争） |
| 2008 | Fannie 和 Freddie 被国有化（次贷危机救助） |

**GSE（政府支持企业）的隐性政府担保 → 可以低成本融资**

---

## 3. MBS 运作机制 How MBS Works ⭐

### 现金项目 Cash Programme
```
贷款机构发放贷款 → 出售给 GSE → GSE 池化成 MBS → 出售给投资者
GSE 收取担保费 (G-Fee) 承担信用风险
```

### 互换项目 Swap Programme
```
贷款机构 → 将贷款"互换"给 GSE → 
GSE 返回 MBS 证券（而不是现金）→ 
贷款机构自己出售 MBS 给投资者
GSE 收取担保费，承担信用风险
```

---

## 4. RMBS 的主要风险 Key Risks of RMBS ⭐

### 1) 提前还款风险 Prepayment Risk
```
原因：利率下降 → 借款人再融资（refinancing）
     搬家、卖房
影响：投资者收到本金 → 只能以更低利率再投资
     "再投资风险 Reinvestment Risk"
```

提前还款测量：
- **CPR (Conditional Prepayment Rate)**：年化提前还款率
- **PSA (Public Securities Association) Standard**：标准提前还款速度曲线
  ```
  PSA 假设：前30个月 CPR 从0线性增至6%/年，此后维持6%
  100% PSA = 标准速度
  200% PSA = 两倍提前还款速度
  ```

### 2) 违约风险 Default Risk
```
借款人无法还款 → 止赎 Foreclosure
GSE MBS：由 GSE 担保（信用风险转移给 GSE）
私有 MBS：无担保，投资者自担违约风险
```

### 3) 利率风险 Interest Rate Risk
```
利率上升 → MBS 价格下跌（如普通债券）
利率下降 → 提前还款增加（负凸性 Negative Convexity）
```

---

## 5. MBS 类型 Types of MBS

### 过手证券 Pass-Through Securities
```
投资者"穿透"持有底层抵押贷款池的比例权益
所有本金和利息按比例分配给投资者
所有人平等承担提前还款风险
```

### 抵押贷款担保证券/CMO Collateralized Mortgage Obligations ⭐
```
将 MBS 池再结构化 → 创设多个"分层" Tranches
不同分层风险/回报不同
```

#### CMO 典型分层结构
| 分层 Tranche | 特点 | 风险 |
|-------------|------|------|
| Senior（A 级） | 最先收到还款；优先保护 | 最低 |
| Mezzanine（中间层） | 中等优先级 | 中等 |
| Junior/Equity（次级） | 最后收到还款；首先承担损失 | 最高 |

**提前还款分配规则（PAC Bonds）：**
```
PAC（计划摊销类）：提前还款速度在一定范围内，PAC 受保护
Support Bonds：吸收超出范围的提前还款波动（更高风险）
```

---

## 6. 2008 次贷危机教训 Lessons from 2008

- 次级贷款（Subprime）→ 评级虚高 → MBS 崩盘
- 模型假设全美房价不会同时下跌 → 现实打脸
- 风险层层转移但最终无处可逃
- GSE 被国有化，纳税人承担最终损失

---

## 考试高频考点 Exam Focus Points

> **历年真题分析 Based on Past Exams 2013–2025**

> ⚠️ **考试趋势**：MBS/证券化 2013–2016 年为核心必考内容；2017–2021 年偶尔出现于理论题；2022 年后几乎不再考，ESG 和开发融资取而代之

1. **MBS/证券化机制（早期必考）** ★★★★ — 2013, 2014, 2016
   - Cash Programme vs Swap Programme 区别（GSE 如何分配信用风险）
   - 风险如何在：贷款机构 → GSE → MBS 投资者 之间传递

2. **CMO vs Pass-Through Securities** ★★★ — 2013, 2014, 2016, 2018（resit）
   - Pass-Through：所有投资者平等承担提前还款风险
   - CMO 分层（Senior/Mezzanine/Junior）：高级层最先收到还款，最后承担损失
   - 考题常要求讨论"tranching 如何改变风险分配"

3. **次级贷款与 2008 危机** ★★★ — 2013, 2014, 2018（resit）
   - 次级贷款（Subprime）特征：通常为 ARM，与房价上涨强依存
   - 为何 Subprime MBS 难定价：overcollateralization 不稳定，delinquency triggers 复杂
   - 评级机构失误：假设全国房价不会同时下跌 → 评级虚高 → 危机

4. **REITs 间接投资（2016–2022 高频）** ★★★★★ — 2013, 2014, 2015, 2016, 2017, 2018, 2019, 2020, 2022, 2023
   - 绕过直接投资三大风险：流动性差、不可分割性、信息不对称
   - 主要约束：强制分红（90%+ 应税利润）、限制再投资
   - 价值创造策略：管理改进、收购优质资产、资本结构优化
   - UK REIT 历史（2007 年启动以来）：用杠杆和 NAV 分析（2014–2017 反复考）

5. **ESG / 绿色投资（近年新重点）** ★★★ — 2022, 2023, 2024
   - 气候变化如何影响 NOI（能效、碳税、绿色溢价/棕色折扣）
   - 绿色建筑在 Pro Forma 中的体现：更低运营成本、更高租金、更低 Cap Rate

6. **投资组合构建 Portfolio Construction** ★★★ — 2019, 2020, 2021, 2023
   - 关键考量：流动性、资产特征（物业类型/地域）、物业数量（分散化）
   - 直接 vs 间接组合的差异；私有市场数据限制（Return smoothing 问题）
