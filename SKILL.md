---
name: aaai-compliance-checker
description: This skill should be used when the user wants to "check AAAI format",
  "verify LaTeX compliance", "audit paper formatting", "validate AAAI submission",
  "check if my paper follows AAAI rules", "format check my paper", "投稿前检查格式",
  "检查论文是否符合AAAI", "AAAI格式检查", or when the user submits a paper to AAAI
  2027 and needs to ensure compliance with the AAAI Author Kit (AuthorKit27)
  formatting and writing requirements. Covers preamble validation, forbidden
  packages/commands detection, title/author format, section structure,
  figures/tables, citations, PDF-level checks, and submission-mode-specific rules.
version: 1.0.0
---

# AAAI 2027 论文合规检查器

对 LaTeX 论文源文件及编译后的 PDF 进行逐项格式合规检查，依据 AAAI 2027
Author Kit（`AuthorKit27/`）中的规范。输出按严重程度分级的结构化报告。

## 快速参考

| 来源 | 路径 |
|------|------|
| Camera-Ready 模板 | `AuthorKit27/CameraReady2027.tex` |
| 匿名投稿模板 | `AuthorKit27/AnonymousSubmission2027.tex` |
| 样式文件 | `AuthorKit27/aaai2027.sty` |
| 参考文献样式 | `AuthorKit27/aaai2027.bst` |
| 可重复性清单 | `AuthorKit27/ReproducibilityChecklist.tex` |

## 检查工作流（按顺序执行）

### Step 1: 确定提交模式

检查 `\usepackage` 声明确定提交类型：

```
\usepackage[submission]{aaai2027}  → 匿名投稿模式
\usepackage{aaai2027}              → Camera-Ready 模式
```

不同模式的差异点（详见 `references/submission-mode-rules.md`）：
- 匿名投稿：作者写 `Anonymous Submission`，affiliations 留空，无 links 块
- Camera-Ready：版权声明自动插入，links 块允许存在

### Step 2: Preamble 合规检查

运行 `scripts/check_preamble.py <tex文件>` 进行自动检查，或手动逐项核验：

**必须存在的行（8 项，缺一不可）：**

```
\documentclass[letterpaper]{article}
\usepackage{aaai2027}                % 或 \usepackage[submission]{aaai2027}
\usepackage[hyphens]{url}
\usepackage{graphicx}
\urlstyle{rm}
\def\UrlFont{\rm}
\usepackage{natbib}                  % 不可添加任何选项
\usepackage{caption}                 % 不可添加任何选项
\frenchspacing
\pdfinfo{/TemplateVersion (2027.1)}
```

**必须不存在的包（15+ 项）：**
`times`, `helvet`, `courier`, `authblk`, `geometry`, `titlesec`, `hyperref`,
`navigator`, `balance`, `float`, `fullpage`, `ulem`, `CJK`, `indentfirst`, `setspace` …
完整列表见 `references/preamble-requirements.md`。

**可选的推荐包：**
`algorithm` + `algorithmic`（算法），`newfloat` + `listings`（代码列表），
`booktabs`（表格）—— 这些是可选的，但如果使用了算法/代码列表就必须正确配置。

### Step 3: 禁用包与命令扫描

运行 `scripts/check_forbidden.py <tex文件>` 进行自动扫描。

**禁用包（25 项）：**
`authblk`, `babel`, `balance`, `cjk`, `epsf`, `epsfig`, `euler`, `float`,
`fullpage`, `geometry`, `graphics`, `hyperref`, `layout`, `lmodern`,
`navigator`, `pdfcomment`, `pgfplots`, `psfig`, `pstricks`, `t1enc`,
`times`, `titlesec`, `tocbibind`, `ulem`

**禁用命令（20+ 项）：**
`\abovecaption`, `\baselinestretch`, `\break`, `\clearpage`, `\columnsep`,
`\float`, `\linespread`, `\newpage`, `\pagebreak`, `\setlength`（除
`\setlength{\tabcolsep}` 外）, `\textheight`, `\tiny`, `\topmargin`,
`\trim`, `\vskip{-`, `\vspace{-`

完整列表及例外说明见 `references/forbidden-packages.md` 和
`references/forbidden-commands.md`。

### Step 4: 标题与作者格式

- 标题使用 Title Case（Chicago Manual of Style 规则）。
  用 https://titlecaseconverter.com/（选 Chicago + Show explanations）验证。
- 标题区域无手动字体大小命令（`\textbf`, `\Large`, `\huge` 等）干预。
- 多机构作者用 `\textsuperscript{\rm x}` 格式关联，逗号在上标后面。
- 作者块未使用 `authblk` 包或 `table` 环境。
- 邮件地址为 roman 字体（非 monospace）。
- 匿名投稿：`\author{Anonymous Submission}`，`\affiliations{}` 为空。
- Camera-Ready：版权声明自动存在，未使用 `\nocopyright`。

详细规则见 `references/author-title-rules.md`。

### Step 5: 章节结构与顺序

运行 `scripts/check_structure.py <tex文件>` 进行自动检查。

**必须遵守的顺序：**
1. Abstract（不得包含 `\cite` 引用）
2. [可选] `links` 块（仅 Camera-Ready，位于 abstract 和正文之间）
3. 正文各节（可选编号，最多 subsection 级）
4. [可选] Content Appendices（用 `\appendix` + 字母编号）
5. [可选] Ethical Statement（unnumbered：`\section*{Ethical Statement}`）
6. [可选] Acknowledgments（unnumbered：`\section*{Acknowledgments}`，≤ 3 句）
7. References（unnumbered，紧随正文，无断页命令）
8. [可选] Supplementary Material（仅会议允许时）

**禁止项：**
- `\input` 拆分子文件（`.bib` 和 `ReproducibilityChecklist.tex` 除外）
- `\pagestyle` 命令
- 任何断页命令（`\newpage`, `\clearpage`, `\pagebreak`）
- References 后有浮动体

详细规则见 `references/structure-rules.md`。

### Step 6: 图表规范

- **格式**：仅 `.jpg`, `.png`, `.pdf`（禁用 `.gif`, `.eps`, `.ps`）
- **裁剪**：LaTeX 外完成；禁用 `clip=true`, `trim`, `viewport` 选项
- **组合图**：禁用 `minipage` 组合多图
- **pgfplots**：不可在正文中使用；须预导出为 PDF 再 `\includegraphics`
- **图注/表注**：在图/表**下方**，10pt Roman，不加粗不斜体
- **表格**：禁用 `\resizebox`；允许 `\setlength{\tabcolsep}` 压缩列间距
- **浮动体**：优先 `[t]` 或 `[b]`，不得集中堆放文末
- **分辨率**：位图 ≥ 300 dpi（需检查 PDF 中的图像属性）
- **颜色**：仅用于图和少量文字（单词级别）；正文无颜色命令；
  WCAG 2.0 对比度 ≥ 4.5:1
- **无 overfull boxes**：检查 `.log` 文件

详细规则见 `references/figure-table-rules.md`。

### Step 7: 引用格式

- 文内引用格式：`(作者, 年份)` — 两位用 "and"，三位及以上用 "et al."
- 无 `\bibliographystyle` 命令（aaai2027.sty 自动设置）
- 参考文献字号 ≥ `\small` (9pt)
- 不得加载 `hyperref` 或 `navigator` 包
- Abstract 中无 `\cite` 引用

详细规则见 `references/citation-rules.md`。

### Step 8: PDF 层面检查

对编译后的 PDF 进行以下检查：

- [ ] PDF 版本 ≥ 1.5（查看 PDF 属性）
- [ ] 无密码保护
- [ ] 字体全部嵌入（File → Properties → Fonts，检查无 Type 3）
- [ ] 无嵌入链接或书签
- [ ] 无页码（页眉/页脚为空）
- [ ] 页面尺寸为 US Letter (8.5 × 11 inch)
- [ ] 内容未溢出到页边距（无 overfull boxes）
- [ ] 匿名投稿：PDF metadata 中无作者信息

使用 Adobe Acrobat Reader 或命令行工具（`pdfinfo`, `pdffonts`）进行检查。

### Step 9: 可重复性清单

如果会议要求提交 Reproducibility Checklist：
- 检查 `ReproducibilityChecklist.tex` 是否已填写（每项不再显示 "Type your response here"）
- 检查回答了所有适用的问题（yes/partial/no/NA）
- 验证 `\input{ReproducibilityChecklist.tex}` 位置在 `\end{document}` 之前

详细规则见 `references/reproducibility-checklist.md`。

### Step 10: 提交文件清单

- [ ] 单个 `.tex` 源文件（无 `\input` 拆分）
- [ ] `.bib` 参考文献文件
- [ ] 实际使用的图形文件（不多不少）
- [ ] `.bbl`, `.aux` 等 LaTeX 生成文件
- [ ] 打包为 `.zip`，总大小 ≤ 10 MB
- [ ] 以第一作者姓命名

## 输出格式

检查报告按 4 级 flag 组织，按严重程度降序排列：

```
🔴 CRITICAL — 直接退稿级
  禁用包/命令、字体包冲突、缺少必要 preamble 行、非 US Letter 纸张

🟡 WARNING  — 格式违规
  字号不当、图表格式不对、章节顺序错误、标题未用 Title Case

🔵 INFO     — 建议改进（默认折叠）
  Title Case 微调建议、引用格式细微偏差、最佳实践推荐

🟢 PASS     — 检查通过项
  列出所有通过检查的项目，确认无需修改
```

每项问题需包含：
- 严重级别 flag
- 所在行号（`.tex` 文件）或 PDF 页码
- 违规内容摘要
- 修复建议（引用 Author Kit 中的具体规则）

## 自动化脚本

三个 Python 脚本覆盖可自动化检查的部分：

- **`scripts/check_preamble.py <tex>`** — Preamble 必要行/禁用字体包检查
- **`scripts/check_forbidden.py <tex>`** — 禁用包和命令的正则扫描
- **`scripts/check_structure.py <tex>`** — 章节顺序、`\input` 使用、断页命令检查

所有脚本仅使用 Python 3.6+ 标准库，无需额外安装依赖。

## 与现有工具的协同

| 场景 | 推荐顺序 |
|------|----------|
| 投稿前全面检查 | 本技能（格式）→ `/paper-review`（学术质量） |
| 写作中 | `/abstract-writing` / `/introduction-writing` / `/research-paper-writing` 写内容 → 本技能验格式 |
| 快速查规则 | `aaai-paper` 命令（参考手册，见 `~/.claude/commands/aaai-paper.md`） |

## 附加资源

### Reference 文件

各维度详细规则存放在 `references/` 中，按需加载：

- **`references/preamble-requirements.md`** — Preamble 必须/禁止/可选行完整列表
- **`references/forbidden-packages.md`** — 25 项禁用包及典型误用场景
- **`references/forbidden-commands.md`** — 20+ 项禁用命令及例外说明
- **`references/formatting-specs.md`** — 字体/字号/行距/页边距精确数值
- **`references/author-title-rules.md`** — 标题 Title Case + 作者排版规范
- **`references/structure-rules.md`** — 章节顺序、编号、命名规范
- **`references/figure-table-rules.md`** — 图/表格式、分辨率、标注位置
- **`references/citation-rules.md`** — 文内引用 + 参考文献列表格式
- **`references/submission-mode-rules.md`** — 匿名投稿 vs Camera-Ready 所有差异
- **`references/reproducibility-checklist.md`** — 可重复性清单填写指南

### 脚本

- **`scripts/check_preamble.py`** — Preamble 自动合规检查
- **`scripts/check_forbidden.py`** — 禁用包/命令正则扫描
- **`scripts/check_structure.py`** — 章节结构和环境检查

### 示例

- **`examples/sample-report.md`** — 完整合规报告输出样例
