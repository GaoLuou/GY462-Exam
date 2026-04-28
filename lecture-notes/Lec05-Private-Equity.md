# Lecture 5 — 私募股权投资 Private Equity Investment Vehicles

## 核心主题 Key Topics
私募股权基金结构、LP/GP 角色、优先回报率、利润分成瀑布、IRR 偏好与回溯机制

---

## 1. 私募股权基金结构 PE Fund Structure

```
投资者 LP (Limited Partners) ──资金──▶ 基金
                                          │
                              基金管理人 GP (General Partner)
                                          │
                                          ▼
                                    物业投资 Properties
```

| | LP（有限合伙人） | GP（普通合伙人/管理人） |
|--|----------------|----------------------|
| 角色 | 被动出资方 | 主动管理方 |
| 典型出资比例 | 90% 资金 + 80% 利润 | 10% 资金 + 20% 利润 |
| 责任 | 有限责任（不参与管理） | 无限责任（通常设单独实体） |
| 典型 LP | 养老金、大学基金、高净值个人 | Blackstone、Cerberus、专业 RE 机构 |

---

## 2. 关键术语 Key Terms

| 术语 | 中文 | 含义 |
|------|------|------|
| Preferred Return / "Pref" | 优先回报率 | LP 先获得固定收益（如 9%）后再分配超额利润 |
| Promote / Carried Interest | 利润分成 / 附带权益 | GP 在超过 Pref 后获得的超额利润份额 |
| Waterfall | 瀑布式分配 | 规定利润按优先级逐层分配的规则 |
| Pari Passu | 同等比例 | 按出资比例等比分配 |
| IRR Lookback | IRR 回溯 | 按最终整体 IRR 目标重新分配出售收益 |

---

## 3. 瀑布分配模式 Waterfall Structures ⭐

### 模式一：超过 Pref 后分成（Option 1）
```
1. 所有人按比例获得 Pref 回报（如 9%）
2. 剩余利润：80% → LP（按出资比例），20% → GP（Promote）
```

### 模式二：先给 LP 达到 Pref，再 80/20 分（Option 2）
```
1. LP 先获得 Pref
2. 剩余全部按 80/20 分（GP 拿 Promote 部分）
```

### 例：Prushansky Pension（LP: $90M）vs Bhavik Fund（GP: $10M）
总利润 $25M，Pref = 9%

**Option 1 结果：**
- Pref 总额 = $9M（Prushansky 8.1M，Bhavik 0.9M）
- 剩余 $16M：Prushansky 80%×90% = 11.52M；Bhavik 80%×10% + 20% = 4.48M
- Bhavik 总计 = **$5.38M**；Prushansky = **$19.62M**

---

## 4. 复杂案例 Complex Example（ICI vs PDI）

**结构：** ICI（LP: $45M），PDI（GP: $5M），总投资 $50M

**瀑布规则：**
1. ICI 先获 5% non-cumulative pref
2. PDI 获 5% non-cumulative pref
3. 超额按 50/50 分
4. 出售时：先还 ICI 本金，再还 PDI 本金
5. ICI 达到 12% IRR；剩余 50/50 分

### 现金流瀑布（经营）
| 年 | 可分配 | ICI 获得 | PDI 获得 |
|----|--------|---------|---------|
| 1 | $1M | $1M（全给pref） | 0 |
| 2 | $2M | $2M（pref） | 0 |
| 3 | $5M | $3.5M | $1.5M |
| 4 | $6M | $4M | $2M |
| 5 | $6.5M | $4.25M | $2.25M |

### IRR 偏好（12% Target for ICI）
- 出售额外支付 ICI 至 12% IRR = $16.8M
- 剩余 50/50 分
- **ICI IRR = 13.22%，PDI IRR = 26.64%**（PDI 超额受益）

### IRR 回溯（Lookback）
- 整体调整使 ICI 恰好 12%，PDI 获得剩余
- **ICI IRR = 12%，PDI IRR = 32.94%**（PDI 风险补偿）

---

## 5. 非累积 vs 累积优先回报 Non-Cumulative vs Cumulative Pref

| | 非累积 Non-Cumulative | 累积 Cumulative |
|--|---------------------|----------------|
| 当期不足 | 不补偿 | 累积到后续年份 |
| 对 LP | 风险较高 | 更有保障 |
| 常见程度 | 相对常见 | 较少见 |

---

## 6. 基金主要功能 Fund Functions
- 汇集资本：解决单一投资者资金不足问题
- 限制杠杆 / 提供股权补充
- 分散风险：跨物业投资
- 专业管理：GP 有市场专业知识和交易网络

---

## 考试高频考点 Exam Focus Points

> **历年真题分析 Based on Past Exams 2013–2025**

1. **LP/GP 结构、角色与风险分配** ★★★★ — 2019, 2020, 2022, 2025
   - LP（有限合伙人）：被动出资，优先获得固定回报（Pref），损失有限
   - GP（普通合伙人）：主动管理，承担更高风险，换取 Promote 超额收益
   - 2022、2025 均考理论题讨论 LP/GP 风险如何分配

2. **Waterfall 瀑布分配计算** ★★★★ — 2020（完整计算题含 Lookback）
   - 顺序：①LP 获 Pref → ②GP 获 Pref → ③按比例（如 50/50）分超额
   - 出售时：先还 LP 本金 → 还 GP 本金 → 再按目标 IRR 分 → 剩余再分

3. **Promote 激励机制** ★★★★ — 2025（理论题重点）
   - Promote = GP 超过 Pref 后获得的超额利润分成（如 20%）
   - 核心逻辑：GP 只有在创造超额回报后才获得额外收益 → 激励努力管理

4. **Deal-by-Deal vs Whole Fund 结算方式** ★★★ — 2025（新考点）
   - Deal-by-deal：每笔交易独立结算 Promote（美国常见）→ GP 早期受益，LP 风险高
   - Whole Fund：所有交易合并计算 Promote（英国常见）→ LP 更有保障

5. **IRR Lookback（回溯条款）计算** ★★★ — 2020（完整计算）
   - 从售价中先补足 LP 达到目标 IRR（如 10%）所需金额
   - 方法：用 PV 公式反算 x，使得 LP 现金流 IRR 恰好等于目标；剩余全给 GP
   - 2020 具体题目：IRR preference（12%）条件下，剩余 50/50 vs lookback 时 GP IRR 从 15.9% 跳到 20.3%
