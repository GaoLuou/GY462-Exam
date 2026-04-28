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
1. 二级市场存在的原因（理论题必考）
2. Cash Programme vs Swap Programme 区别
3. 提前还款风险（CPR/PSA 概念）
4. Pass-Through vs CMO 结构差异
5. MBS 的三种主要风险及相互关系
6. GSE 的角色和隐性政府担保的含义
