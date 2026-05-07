# GY462 考前复习清单 Revision Checklist

> 来源：2026年5月6日 + 5月7日老师划重点录音
> 考试：2026年5月11日 14:30 | 闭卷 | 2小时+10分钟阅读时间 | 两道题均必答

---

## 优先级说明 Priority Guide

| 标记 | 含义 | 目标 |
|------|------|------|
| 🔴 **及格必记** | 不会这个很难及格，先死磕这些 | 50分 |
| 🟡 **Merit加分** | 掌握后能稳定在60分区间 | 60分 |
| 🟢 **Distinction** | 已有时间再看，否则跳过 | 70分 |

> 只想及格：**只看 🔴 标记的内容**，Q2计算题做对，Q1写 IO vs CPM + MBS三类 + 风险排序，就够了。

---

## 考试结构 Exam Structure

| 项目 | 说明 |
|------|------|
| 题目数 | **2道，均必答**（Q1理论 + Q2计算，不可选） |
| 时间 | 2小时正式 + 10分钟阅读时间（用来规划答题策略） |
| 计算器 | Casio FX-83 / FX-85 系列（其他型号请提前确认） |
| 闭卷 | 是，不可带笔记 |

---

## 一、理论题 Theory Question 重点 ⭐

理论题考点**散布全部10周**，可能跨多讲组合。

### 1.1 房地产投资分析 Real Estate Investment Analysis（Lec 1–5）

- [ ] 🔴 **风险与机会 Risks & Opportunities of Real Estate**
  - 风险：自然灾害（物理资产集中在特定位置）、空置风险、租赁风险、运营风险、流动性风险（大额且不可分割）
  - 机会：租金增长 Rental Growth、终值 Terminal Value（出售所得）、运营成本优化 Operating Cost（课件原词，非"Capital Appreciation"）
  - **排序很重要**：优先最大化租金收入 → 高效运营 → 最后依赖地产周期
  - 不要把流动性/大额/不可分割全堆在第一个子问题，若Q1b专门问这些则省着说

- [ ] 🟡 **估值方法 Valuation Methods**
  - DCF（折现现金流）：结合风险与机会，可使用分阶段折现率
  - 上行/下行现金流的拆解（Unbundling cash flows）：整合收入 vs 过渡收入
  - Cap Rate：为什么好（简单）？为什么不好（不前瞻）？如何调整（减去增长率）？
  - **Growth-adjusted Cap Rate = Cap Rate − Growth Rate**
    - Growth > 0：减去正数 → adjusted cap rate 变小 → 资产价值更高（市场预期增长）
    - Growth < 0：减去负数（等于加上）→ adjusted cap rate 变大 → 资产价值更低、风险更高
    - ⚠️ 反直觉：负增长时不是"cap rate 减个负数"让价格变高，而是让 cap rate 变大反映更高风险
  - **Cap Rate大 = 风险高 + 机会少**
  - 资产价值由净营业收入NOI驱动，不要完全依赖地产周期

- [ ] 🟢 **风险评估方法 Risk Assessment Methods**（老师说很多人没答全）
  - **课件（Lec03）三种正式方法**：
    1. **尽职调查 Due Diligence**：⚠️ 几乎没人提！是定量分析的前提，验证所有输入假设
    2. **IRR分解/NPV分解 Partitioning**：⚠️ 几乎没人提——区分"运营收益"vs"出售收益"，判断是否过度依赖终值
    3. **敏感性分析 Sensitivity Analysis**：包含三个层次——
       - 压力测试 Stress Testing：固定中心预测，逐个测试单一变量
       - 情景分析 Scenario Analysis：多个宏观状态，所有关键变量同时变化
       - **模拟/蒙特卡洛 Simulation / Monte Carlo**：⚠️ Mock 里几乎没人提，是高分点——对所有关键变量的概率分布同时模拟，输出 IRR/NPV 的概率分布，比单点情景分析更全面
  - 结合案例（Copenhagen / Croydon 项目）讲述你做了哪些压力测试

- [ ] 🟡 **杠杆 Leverage**（Lec 4）
  - 税前/税后 IRR（Before/After Tax）
  - 盈亏平衡利率 Breakeven Interest Rate
  - 杠杆与收益的关系（Weil公式）
  - 杠杆与风险的放大（资本价值变化 + 融资风险分解）
  - 杠杆与现金流的关系（Growth field → IRR分解）

### 1.2 抵押贷款 Mortgages（Lec 6–7）

- [ ] 🟡 理解抵押贷款全周期（含/不含二级市场）
- [ ] 🔴 各类贷款对比：
  - IO（Interest Only）：对商业投资者友好（早期现金流压力小），对银行风险较大（敞口期长）→ 银行收更高利率
  - CPM（Constant Payment Mortgage）
  - GPM（Graduated Payment Mortgage）：通货膨胀背景下使用，早期还款少
  - ARM（Adjustable Rate Mortgage）：利率随市场调整
  - 🟡 **通货膨胀如何推动 GPM 和 ARM 的使用**
  - 🟢 **参与贷款 Participation Loan**：⚠️ 老师提到"没怎么讲，但理论题可能出"
    - 贷款方除收取利息外，还分享物业的部分运营收入或资本增值
    - 好处：借款人以"让利"换取更低的基础利率
    - 风险分配：lender 承担更多上行收益权，borrower 以此换取更低固定利率负担
- [ ] 🔴 IO vs CPM 的权衡（银行与借款人各自偏好分析）

### 1.3 私募股权基金 Private Equity Funds（Lec 5，外部讲师 Ignacio）

- [ ] 🟡 GP（General Partner）与 LP（Limited Partner）角色、风险分担、报酬
- [ ] 🟡 瀑布分配 Waterfall：Deal-by-deal vs All-fund 结构对比
- [ ] 🟢 激励机制（carried interest）与绩效计量
- [ ] ⚠️ **瀑布不会出计算题**，只考理论

### 1.4 开发融资 Development Finance（外部讲师 Paul + Rico）

- [ ] 🟡 永久贷款 Permanent Loan vs 过渡贷款 Interim Lender（桥接），如何衔接
- [ ] 🟡 **快捷估值（10法则 / Rule of 10 & 7a）vs 完整折现估值**对比：优缺点各是什么？
- [ ] 🟢 开发项目关键风险管理（Paul & Rico 提到的文化差异与承包商管理）

### 1.5 抵押贷款支持证券 Mortgage-Backed Securities（MBS）

- [ ] ⚠️ **只考理论，不考计算**
- [ ] 🟡 有/无二级抵押市场下，贷款的生命周期对比
- [ ] 🟡 证券化动机：现金型（Cash Program）vs 互换型（Swap Program）
- [ ] 🔴 三类证券对比（**谁承担预付风险是核心**）：
  - **抵押贷款债券 Mortgage-Backed Bonds（MBB）**：超额抵押（over-collateralised），预付风险归**发行方**
  - **抵押贷款直接过手证券 Mortgage Pass-Throughs**：预付风险归**投资者**
  - **抵押贷款担保债券 CMOs（Collateralised Mortgage Obligations）**：按**tranche分配**，高级层最安全

### 1.6 ESG（Lec 10，外部讲师 S. Burak Kaplanoglu）

- [ ] ESG 影响四个维度：Risks（±）/ Yields（±）/ Finance（±）/ Valuation（±）
- [ ] ESG如何影响资产风险：搁浅资产（Stranded Asset）、绿色溢价（Green Premium）、空置期延长
- [ ] ESG如何影响借款成本：73%贷款方有ESG策略；81%认为ESG将影响贷款意愿；93%认为监管将要求纳入资本配置
- [ ] **双重实质性 Double Materiality**：Inside-out（企业对环境的影响）+ Outside-in（环境风险对企业财务的反向冲击）
- [ ] 要将 ESG 与 investment analysis、cost of borrowing 串联，不要孤立讲
- [ ] ⚠️ Mock exam 的 ESG 题与今年课程偏差较大，今年重点更偏**投资者+贷款方**视角

---

## 二、计算题 Calculation Question 重点 ⭐

### 2.1 计算器操作

- [ ] 🔴 检查电池是否充足，确认是 Casio FX-83/85
- [ ] 🔴 **每次开始计算前清除内存**（按 CLR → Memory），避免残留数字污染
- [ ] Excel 和金融计算器软件**不允许使用**

### 2.2 CPM（Constant Payment Mortgage）🔴 及格命脉

- [ ] 🔴 5个键：N, I/Y, PV, PMT, FV——**先把这5个键玩熟，其他一切都建在这上面**
- [ ] 🔴 月付/季付/年付的 N 和 I/Y 调整（直接乘/除，不需要有效年利率转换）
- [ ] 🔴 负摊销贷款 **Negative Amortization**：FV > PV（初始本金），**FV键不能留零**
- [ ] 🔴 部分摊销贷款 **Partial Amortizing Loan**：FV = 气球还款额（Balloon Payment），不为零
- [ ] ⚠️ 常见错误：把IO + CPM混合，认为"前N期IO，第N+1期CPM一次性还完"——**这是错误的**，整个期间是一致的摊销逻辑

### 2.3 IO（Interest Only）🔴

- [ ] 🔴 每期只还利息，期末还本金（FV = 原始贷款额）
- [ ] 🔴 **Levered IRR 里最常用 IO**：中间期扣利息，最后期还本金 + 利息

### 2.4 GPM（Graduated Payment Mortgage）🟢 时间够再看

- [ ] 🟢 早期还款低，后期递增
- [ ] 🟢 需要分阶段计算，计算器操作繁琐
- [ ] 目标：做对大概方向，写清楚逻辑步骤（即使数字偏差，得逻辑分）

### 2.5 ARM（Adjustable Rate Mortgage）🟡

- [ ] 🟡 老师只做过年频率示例，考试可能出现月/季频率
- [ ] 🟡 有效借款成本（Effective Cost of Borrowing）的计算
- [ ] 🟡 ARM的预付情景：提前还款时 ECB 可能低于全期 ECB（规避了后期高利率）→ 反直觉，**不要假设结论，计算后再判断**

### 2.6 有效借款成本 Effective Cost of Borrowing（ECB）🔴

- [ ] 🔴 折扣点 Discount Points：增加 ECB，因为前期缴费减少了实际到手金额
- [ ] 🔴 ECB **必须高于名义利率**（当有折扣点时），若计算出来更低说明计算有误
- [ ] 🔴 若发现数字与逻辑矛盾，**明确写出"I believe there may be a calculation error; logically ECB should be higher"**，比假装没看到更有利

### 2.7 杠杆计算 🔴 及格命脉（与Q2直接挂钩）

- [ ] 🔴 无杠杆 IRR vs 有杠杆 IRR（简单现金流 + IO/CPM贷款）——**老师说这就是Q2的结构**
- [ ] 🟡 税前/税后 IRR（28% 税率，利息费用抵税）
- [ ] 🟢 折旧：土地 vs 建筑物折旧（理论为主，计算较少）

### 2.8 现金流与 IRR 🔴

- [ ] 🔴 季度现金流的处理：直接用季度频率计算（不要折算成年度）
- [ ] 🔴 写出清晰的中间步骤：N= ?, I/Y= ?, PV= ?, PMT= ?, FV= ?（**逻辑对数字错也给分**）
- [ ] 🔴 季度频率转年：直接乘4（不要用有效年利率公式复利换算）
- [ ] 🟡 数字精度：金额保留4位小数；利率/百分比尽量多保留几位

---

## 三、案例整合 Case Study Integration

老师**明确要求**考试中引用案例，不要只谈抽象概念。

| 案例 | 适用场景 |
|------|---------|
| **Copenhagen** | 开发项目（Development），现金流跨度长，季度时间轴，压力测试变量：建设周期、招租率 |
| **Croydon** | Buy-hold 持有型项目，NOI估算，杠杆IRR，IRR分解 |

- 若题目问"如何评估投资风险"，可说"在Copenhagen案例中我们做了X，若条件允许还应做Y"
- 可以比较两个案例（如开发 vs 持有型投资的风险差异）

---

## 四、答题策略 Exam Technique

- [ ] **10分钟阅读时间**：通读两道题，规划各子问题顺序和时间分配
- [ ] **看子问题分值**：分值高的子问题花更多时间；不要在5分题上写2.5页
- [ ] **跨子问题不重复**：若Q2b专门考流动性，Q2a就少提流动性，换其他角度
- [ ] **不要只列要点**：每个bullet point后加解释，说清楚它的含义和重要性排序
- [ ] 理论题：3–5个核心要点，带排序和解释，优于10个裸标题
- [ ] 计算题：写清每一步的N/I/Y/PV/PMT/FV值；即使答案有误也能拿逻辑分
- [ ] **不要用Excel**（考场不允许），现在就停止用Excel做练习
- [ ] 答案逻辑和数字矛盾时，写一句"I believe there may be a calculation error; logically this should be higher/lower"

---

## 五、最后5天冲刺计划

| 日期 | 任务 |
|------|------|
| 5月6日（今天）| 通读本清单，定位薄弱点 |
| 5月7日 | 重点复习：负摊销/部分摊销贷款、ECB计算、GPM练习 |
| 5月8日 | 限时模拟 Mock Exam（2小时严格计时），重点写中间步骤 |
| 5月9日 | 复习理论：MBS三类证券、私募基金瀑布、ESG；结合案例整合 |
| 5月10日 | 轻度回顾公式 + 案例要点，检查计算器电池，早睡 |
| 5月11日 | 考试 14:30，10分钟读题规划策略 |

---

## 六、高频易错点速查

| 易错点 | 正确做法 |
|--------|---------|
| 负摊销贷款 FV 留 0 | FV = 期末未偿本金（大于初始本金），必须输入 |
| ECB < 名义利率（有折扣点时）| 说明计算有误，逻辑上ECB必须更高 |
| 把 IO+CPM 混用当"负摊销" | 负摊销是一种完整自洽的摊销机制，不是两种贷款混合 |
| 季度利率复利换算成年利率 | 直接×4即可，不需要 (1+r)^4 - 1 |
| 子问题重复回答相同风险 | 读全部子问题再分配答题内容 |
| 只列bullet point不解释 | 每点后写一句解释+排序理由 |
| 不写计算中间步骤 | 写出 N/I/Y/PV/PMT/FV，保留最终按键前的数字 |
