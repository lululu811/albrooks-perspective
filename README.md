# albrooks-perspective

> 把 Al Brooks 的价格行为交易思维蒸馏成一个可复用的 AI Skill —— 让 AI 以「逐根 K 线分析」的方式陪你看图、审视交易决策、解读价格行为。
>
> *An AI skill distilled from Al Brooks' price action framework: bar-by-bar chart analysis, probability thinking, and disciplined trade review.*

---

## 这是什么

本项目是一份 **思维蒸馏产物**（基于女娲 v2.0 流程）。它把 Al Brooks —— 价格行为交易法的集大成者、前眼科医生转职全职交易员 —— 的公开方法论提炼为一份可供 AI Agent 加载的 `SKILL.md`。

一旦安装到你的 AI Agent（如 Claude Code），当你说出「用 Al Brooks 的视角看看这个图」这类请求时，Agent 会**直接以 Al Brooks 的身份**回应：

- 用概率语言说话（从不说「一定」）
- 永远**从左侧开始**：先看背景（Context），再看信号 K 线
- 按 **背景 → 信号 → 风险 → 陷阱** 四步分析图表
- 落实 Al Brooks 的 10 个核心心智模型和 10 条决策启发式

> ⚠️ **非投资建议**：本 Skill 是思维框架与学习方法，不构成任何投资建议。交易有风险，入市需谨慎。

---

## 核心能力

| 能力 | 说明 |
|------|------|
| 🎭 **角色扮演** | 激活后以 Al Brooks 本人语气、节奏、词汇直接回应 |
| 🧠 **10 大心智模型** | 市场周期四态、Always In、交易者方程式、背景+信号+跟随、80% 法则、测量移动/磁吸、大反转(MTR)、急速变通道、开盘/90 分钟定理、双重随机性 |
| 🎯 **决策启发式** | 背景先于信号、趋势只做顺势、区间高抛低吸、回报≥2 倍风险、数 K 线等二次入场、止损在信号 K 之外、看跟随确认突破、早盘等反转、沃尔玛交易法、多时间框架对齐 |
| 🗣️ **表达 DNA** | 复刻其概率化、条件句、自嘲式冷幽默的说话方式 |
| 📊 **图表分析协议** | 有图先取真实行情 → 判断背景 → 识别信号 → 评估风险 → 检测陷阱 |
| 🚫 **诚实的边界** | 明确标注方法主观、主用于 ES、未量化验证，不与量化项目混淆 |

---

## 快速开始

### 安装到 Claude Code

```bash
# 方法 A：软链（推荐，源目录改动即时生效）
ln -s /path/to/albrooks-perspective ~/.claude/skills/albrooks-perspective

# 方法 B：直接复制（独立副本）
cp -r /path/to/albrooks-perspective ~/.claude/skills/albrooks-perspective
```

其他支持 skill 的 Agent（Codex / OpenCode 等）同理，把目录放进它对应的 skills 目录即可。

### 触发方式

出现以下关键词时，Skill 会自动激活：

- 「用 Al Brooks 的视角」
- 「价格行为分析」「逐根 K 线分析」
- 「Brooks 会怎么看」「Al Brooks mode」
- 「看看这个图」

### 示例提问

> 用 Al Brooks 的视角看这张 5 分钟 ES 图，当前是交易区间还是趋势？有没有值得入场的信号 K 线？

> 我这笔交易止损被打掉了，但市场又回去了，是不是我错了？

> 用 Al Brooks 的方式解释一下什么是「测量移动」。

首次激活会声明一次免责声明，之后不再重复；说「退出角色」即可恢复正常模式。

---

## 项目结构

```
albrooks-perspective/
├── SKILL.md                    # 最终产物：可直接加载的技能文件
├── README.md                   # 本文件
├── scripts/
│   ├── pre_extract.py          # Phase 1.5 预提炼工具
│   └── quality_gate.py         # 质量门禁脚本
├── references/
│   ├── research/               # 6 个维度的调研结果
│   │   ├── 01-writings.md      #   著作与系统思考
│   │   ├── 02-conversations.md #   对话与访谈素材
│   │   ├── 03-expression-dna.md#   表达 DNA
│   │   ├── 04-external-views.md#   他者视角
│   │   ├── 05-decisions.md     #   决策记录
│   │   └── 06-timeline.md      #   人物时间线
│   ├── extraction-framework.md # 思维框架提炼方法论
│   └── skill-template.md       # SKILL.md 构建模板
└── knowledge-acquisition/      # 知识获取系统
    ├── config/                 #   tools / channels / quality-rules
    └── scripts/                #   channel_manager / quality_evaluator
```

> 📌 **语料说明**：本仓库只包含蒸馏产物与工程代码。课程转写、书籍、抓取文章等原始素材（`references/sources/`）**不随仓库分发**，以免涉及版权。

---

## 与 albrooks-quant 的关系

本 Skill 刻意与量化项目 `albrooks-quant` 解耦：

- **本 Skill**：教你像 Al Brooks 一样 **看图说话**（思维框架 + 主观判断）
- **albrooks-quant**：把形态检测变成 **可回测的代码**（量化计算）

两者通过「形态名称」对齐（如「信号 K 线」在两边都这么叫），但互不越界：本 Skill 不给具体公式阈值，quant 不做主观判断。

---

## 本地开发

### 质量门禁

检查 6 个调研文件是否达到进入下一阶段的质量标准（来源数量、一手占比、置信度标注、矛盾/缺口标注、过程密度）：

```bash
python3 scripts/quality_gate.py .
```

### 预提炼报告

生成 Phase 1.5 预提炼报告（来源统计、置信度总评、矛盾点、缺口、时间跨度、思想转折点信号）：

```bash
python3 scripts/pre_extract.py .
```

### 蒸馏流程

项目按 Phase 0 → 5 推进：入口确认 → 信息采集 → 预提炼与质量门禁 → 框架提炼 → 提炼确认 → Skill 构建 → 质量验证 → 双 Agent 精炼。详见 `references/extraction-framework.md` 与 `references/skill-template.md`。

---

## 调研来源与诚实边界

- 调研截止：2025 年初，基于 Al Brooks 公开课程、著作与访谈整理
- 方法高度主观：两个学过同样课程的人可能对同一图表做出不同分析
- 主要适用于 E-mini S&P 500（ES），其他品种需自行验证
- 方法论未做系统化回测，概率判断属于经验估计（量化验证交给 `albrooks-quant`）

---

## 版权与许可

- `SKILL.md` 及本仓库工程内容为作者原创整理，基于 Al Brooks 公开课程与著作的 **学习性提炼**，仅供学习交流。
- 原始素材（课程转写、书籍摘录等）版权归原作者所有，本仓库不包含也不授权分发这些素材。
- 本项目的任何内容**不构成投资建议**。

---

## 致谢

基于 Al Brooks 公开的《Trading Price Action》三部曲、Brooks Pricing Course 视频课程及相关访谈，以及中文社区「方方土」系列的学习性梳理蒸馏而成。
