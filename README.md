# AAAI Compliance Checker

AAAI 2027 论文 LaTeX 格式合规检查器 —— 适用于 Claude Code 和 OpenAI Codex CLI。

给定一篇论文的 `.tex` 源文件（及 PDF），逐项检查是否符合 AAAI 2027 Author Kit 的格式与写作规范，输出按严重程度分级的结构化报告。

## 安装

### Claude Code

```bash
# 复制到用户技能目录
cp -r skills/* ~/.claude/skills/aaai-compliance-checker/
```

或作为插件安装：
```bash
claude plugins install github.com/HansonLegacy/aaai-compliance-checker
```

### Codex CLI

```bash
# 复制到用户技能目录
cp -r skills/* ~/.agents/skills/aaai-compliance-checker/
```

## 使用方法

### 自然语言触发

在 Claude Code / Codex CLI 会话中直接说：
- "检查我的论文是否符合 AAAI 格式"
- "validate AAAI submission"
- "format check my paper"
- `/aaai-compliance-checker`

### 手动运行脚本

```bash
python scripts/check_preamble.py paper.tex     # Preamble 合规检查
python scripts/check_forbidden.py paper.tex    # 禁用包/命令扫描
python scripts/check_structure.py paper.tex    # 章节结构检查
```

所有脚本仅依赖 Python 3.6+ 标准库，无需安装第三方包。

## 检查维度

| # | 检查项 | 自动化 | 说明 |
|---|--------|--------|------|
| 1 | 提交模式 | 手动 | 识别匿名投稿 vs Camera-Ready |
| 2 | Preamble | ✅ 脚本 | 必要行/禁止行 |
| 3 | 禁用包/命令 | ✅ 脚本 | 25+ 禁用包，20+ 禁用命令 |
| 4 | 标题与作者 | 半自动 | Title Case + 排版规范 |
| 5 | 章节结构 | ✅ 脚本 | 顺序/命名/编号 |
| 6 | 图表规范 | 半自动 | 格式/分辨率/标注位置 |
| 7 | 引用格式 | 半自动 | 文内引用 + 参考文献 |
| 8 | PDF 检查 | 手动 | 字体嵌入/Type 3/版本 |
| 9 | 可重复性清单 | 半自动 | 填写完整性 |
| 10 | 提交文件 | 手动 | 文件清单/命名/大小 |

## 输出格式

```
[CRITICAL] — 直接退稿级（禁用包/命令、字体冲突、缺少必要 preamble）
[WARNING]  — 格式违规（字号不当、图表格式不对、章节顺序错误）
[INFO]     — 建议改进（Title Case 微调、引用格式细微偏差）
[PASS]     — 检查通过项
```

详见 `examples/sample-report.md`。

## 依赖

- Python 3.6+（仅 stdlib）
- AAAI 2027 Author Kit（已包含在 `AuthorKit27/` 中，也可从 [AAAI 官网](https://aaai.org/) 下载）

## 目录结构

```
aaai-compliance-checker/
├── SKILL.md                    # 核心技能定义
├── plugin.json                 # Claude Code 插件清单
├── agents/
│   └── openai.yaml             # Codex CLI 元数据
├── references/                 # 详细规则文档（10 篇）
├── scripts/                    # Python 自动化检查脚本
├── examples/                   # 示例报告
└── AuthorKit27/                # AAAI 2027 官方模板（参考）
```

## License

MIT © 2026 HansonLegacy
