# Preamble Requirements — AAAI 2027

> 来源：`CameraReady2027.tex` §Document Preamble, §The Following Must Appear in Your Preamble

## 必须存在的行（8 项）

以下行必须出现在 `\begin{document}` 之前，且不可修改：

| # | 行 | 说明 |
|---|-----|------|
| 1 | `\documentclass[letterpaper]{article}` | 纸张固定为 US Letter |
| 2 | `\usepackage{aaai2027}` 或 `\usepackage[submission]{aaai2027}` | 样式文件（submission 模式用于匿名投稿） |
| 3 | `\usepackage[hyphens]{url}` | URL 自动换行 |
| 4 | `\usepackage{graphicx}` | 图形插入 |
| 5 | `\urlstyle{rm}` | URL 使用 Roman 字体 |
| 6 | `\def\UrlFont{\rm}` | URL 字体定义为 Roman |
| 7 | `\usepackage{natbib}` | 参考文献管理，**不可加任何选项** |
| 8 | `\usepackage{caption}` | 图表标题，**不可加任何选项** |
| 9 | `\frenchspacing` | 句号后不额外加空格 |
| 10 | `\pdfinfo{/TemplateVersion (2027.1)}` | 模板版本元数据 |

## 绝对禁止的字体包

aaai2027.sty 自动加载 `newtxtext`(serif)、`helvet`(sans-serif)、`courier`(monospace)。
以下包**不可**出现在 preamble 中：

- `\usepackage{times}` — 与 newtxtext 冲突
- `\usepackage{helvet}` — 样式文件已加载
- `\usepackage{courier}` — 样式文件已加载
- `\usepackage{lmodern}` — 替换了字体族
- `\usepackage{t1enc}` — 字体编码冲突

## 绝对禁止的布局/格式包

以下包**不可**出现在 preamble 中（完整列表，共 25 项）：

```
authblk   babel     balance   cjk       epsf      epsfig
euler     float     fullpage  geometry  graphics  hyperref
layout    lmodern   navigator pdfcomment pgfplots  psfig
pstricks  t1enc     times     titlesec  tocbibind ulem
```

补充禁止（来自模板注释的 "DISALLOWED PACKAGES" 区域）：
```
flushend   indentfirst   multicol   nameref
savetrees  setspace      stfloats   tabu
wrapfig
```

## 推荐但可选的行

| 包 | 用途 | 注意事项 |
|----|------|----------|
| `\usepackage{algorithm}` + `\usepackage{algorithmic}` | 算法伪代码 | 如无算法可删除 |
| `\usepackage{newfloat}` + `\usepackage{listings}` | 代码列表 | 需配套 `\DeclareCaptionStyle{ruled}{...}` 等设置 |
| `\usepackage{booktabs}` | 专业表格线 | 推荐使用 |

## 可配置项

- `\setcounter{secnumdepth}{0}` — 可改为 1（显示节编号）或 2（显示节+子节编号），不可 > 2

## 检查方法

```bash
python scripts/check_preamble.py paper.tex
```

自动检查：
1. 10 项必要行是否存在
2. 是否出现禁用包名
3. `natbib` 和 `caption` 是否被添加了选项（`\usepackage{natbib}[...]` 或 `\usepackage{natbib}{...}`）
4. 字体包冲突检测
