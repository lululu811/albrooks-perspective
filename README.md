# Al Brooks 价格行为 · Skill 蒸馏工作目录

> 基于女娲 v2.0 流程建立的思维蒸馏项目

## 目录结构

```
albrooks-perspective/
├── SKILL.md                          # 最终产物（蒸馏完成后生成）
├── README.md                         # 本文件
├── scripts/
│   └── pre_extract.py                # Phase 1.5 预提炼工具
├── references/
│   ├── research/                     # 6个维度的Agent调研结果
│   │   ├── 01-writings.md           # 著作与系统思考
│   │   ├── 02-conversations.md      # 对话与访谈素材
│   │   ├── 03-expression-dna.md     # 表达DNA
│   │   ├── 04-external-views.md     # 他者视角
│   │   ├── 05-decisions.md          # 决策记录
│   │   └── 06-timeline.md          # 人物时间线
│   ├── sources/                      # 一手素材（用户提供的原始文件）
│   │   ├── books/
│   │   ├── transcripts/
│   │   └── articles/
│   ├── extraction-framework.md      # 思维框架提炼方法论
│   └── skill-template.md            # SKILL.md 构建模板
└── knowledge-acquisition/           # 知识获取系统
    ├── config/
    │   ├── tools.yaml
    │   ├── channels.yaml
    │   └── quality-rules.yaml
    └── scripts/
```

## 蒸馏对象

**Al Brooks** —— 价格行为交易法（Price Action）的集大成者，前眼科医生转职全职交易员，以「逐根K线分析」（bar-by-bar analysis）闻名。

## 核心方法论

Al Brooks 的交易体系强调：
- **每根K线都有故事**：不依赖指标，直接读取价格本身的信息
- **80%法则**：80%的突破会失败回到震荡区间，80%的趋势会在某个时刻反转
- **交易者方程式**：每笔交易都是概率×回报 vs 风险的计算
- **市场周期**：震荡→突破→趋势→回调→震荡的循环
- **信号K线与入场K线**：信号K线提示机会，入场K线确认执行
- **通道与测量目标**：通道提供边界，测量移动（Measured Move）提供目标

## 工作流程

### Phase 0: 入口确认
- [ ] 确认蒸馏对象：Al Brooks（价格行为交易大师）
- [ ] 聚焦方向：价格行为分析框架 + 逐根K线解读方法
- [ ] 用途：交易思维顾问、图表分析教练
- [ ] 检查本地素材：是否有一手资料（书籍PDF、课程视频、访谈transcript）

### Phase 1: 信息采集
- [ ] Agent 1: 著作与系统思考（3本核心著作：Trending/Trading Range/Reversals）
- [ ] Agent 2: 对话与访谈素材 ⭐（Brooks Pricing Course视频课程）
- [ ] Agent 3: 表达DNA（技术分析语境下的表达方式）
- [ ] Agent 4: 他者视角（学员评价、其他交易员对比）
- [ ] Agent 5: 决策记录 ⭐（实盘图表分析、入场出场逻辑）
- [ ] Agent 6: 人物时间线（眼科医生→全职交易员→教育者）

### Phase 1.5: 预提炼与质量门禁
```bash
python scripts/pre_extract.py .
```
- [ ] 来源统计通过
- [ ] 一手来源占比 > 50%
- [ ] 矛盾点已标注
- [ ] 缺口维度已识别

### Phase 2: 框架提炼
- [ ] 心智模型提取（3-7个）
- [ ] 决策启发式提取（5-10条）
- [ ] 表达DNA分析
- [ ] 价值观与反模式
- [ ] 内在张力识别

### Phase 2.5: 提炼确认
- [ ] 用户确认提炼结果

### Phase 3: Skill构建
```bash
# 使用 skill-template.md 填充内容
```

### Phase 4: 质量验证
- [ ] 已知测试（3个经典图表分析对比）
- [ ] 边缘测试（1个Al Brooks未讨论过的市场）
- [ ] 风格测试（100字图表解读）

### Phase 5: 双Agent精炼
- [ ] auto-skill-optimizer 评审
- [ ] skill-creator 评审

## 信息源

### 优先采集（一手）
- **著作三部曲**：
  - *Trading Price Action Trends* (2012)
  - *Trading Price Action Trading Ranges* (2012)
  - *Trading Price Action Reversals* (2012)
- **Brooks Pricing Course**（130+小时视频课程）
- **每日图表分析**（官网 blog 的 daily analysis）
- **YouTube访谈**（Traders Studio等）

### 二手来源
- 学员整理的笔记和总结
- 其他价格行为交易员的对比分析
- TradingView上的社区讨论

### 黑名单（不采集）
- 知乎（洗稿严重）
- 微信公众号（无法验证）
- 百度百科

## 核心心智模型（预填）

基于Al Brooks公开方法论的初步提炼：

1. **交易者方程式** - 每笔交易 = 概率×回报 vs 风险
2. **80%法则** - 80%突破失败 + 80%趋势终将反转
3. **信号K线/入场K线** - 信号提示机会，入场确认执行
4. **市场周期四阶段** - Always In Long/Short + Breakout Mode + Channel Mode + Trading Range
5. **测量移动** - 等距目标位（Measured Move）
6. **通道几何** - 通道线 + 微通道 + 通道内交易规则
7. **双顶/双底** - 失败的突破 = 反向信号
8. **缺口与真空** - 价格跳过区域 = 未来回填概率高
9. **最终旗帜** - 趋势末段的最后一个回调 = 反转触发
10. **磁吸效应** - 关键价位（前高/前低/整数位）吸引价格

## 与 albrooks-quant 的解耦设计

本skill聚焦**思维框架**和**分析逻辑**，不实现量化计算：
- 本skill：教你像Al Brooks一样**看图说话**
- `albrooks-quant`：把Al Brooks的形态检测变成**可回测的代码**

解耦原则：
- 本skill不包含具体公式或阈值（那是quant的事）
- `albrooks-quant`不包含主观判断（那是skill的事）
- 两者通过"形态名称"对齐（如"信号K线"在两边都叫这个名字）

## 诚实边界

- 调研截止：2025年初
- Al Brooks主要交易E-mini S&P 500期货，对其他品种的适配需验证
- 价格行为是主观艺术，Skill能给框架，给不了实时盘感
- Al Brooks的方法论在2010年代后有所演化，需注意时效性

## 下一步

当你准备好启动蒸馏时，说"开始蒸馏"或提供Al Brooks的一手素材。
