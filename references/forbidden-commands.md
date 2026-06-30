# Forbidden Commands — AAAI 2027

> 来源：`CameraReady2027.tex` Table 1, §Commands and Packages That May Not Be Used

## 完整禁用命令列表

### 页面控制类（直接退稿）

| 命令 | 替代方案 |
|------|----------|
| `\clearpage` | 删除；让 LaTeX 自动分页 |
| `\newpage` | 删除；让 LaTeX 自动分页 |
| `\pagebreak` | 删除；让 LaTeX 自动分页 |
| `\break` | 删除 |
| `\pagestyle{...}` | 删除；AAAI 禁止页码 |

### 版式/间距修改类

| 命令 | 说明 | 例外 |
|------|------|------|
| `\baselinestretch` | 改变行距 | 无 |
| `\linespread{...}` | 改变行距 | 无 |
| `\abovecaption` | 改变图注上方间距 | 无 |
| `\belowcaption` | 改变图注下方间距 | 无 |
| `\abovedisplay` | 改变公式上方间距 | 无 |
| `\belowdisplay` | 改变公式下方间距 | 无 |
| `\columnsep` | 改变栏间距 | 无 |
| `\topmargin` | 改变上边距 | 无 |
| `\textheight` | 改变文本高度 | 无 |
| `\addevensidemargin` | 改变偶数页边距 | 无 |
| `\addsidemargin` | 改变边距 | 无 |
| `\addtolength` | 改变 LaTeX 长度 | 无 |
| `\setlength{...}{...}` | 改变长度变量 | **仅 `\setlength{\tabcolsep}{...}` 允许** |
| `\float` | 改变浮动体行为 | 无 |

### 字号修改类

| 命令 | 说明 |
|------|------|
| `\tiny` | 字号过小，不可接受 |

### 图形操作类

| 命令 | 说明 | 替代方案 |
|------|------|------|
| `\clip` | 裁剪图形 | 在 LaTeX 外用图像软件裁剪 |
| `\trim` | 裁剪图形 | 在 LaTeX 外用图像软件裁剪 |
| `clip=true` | `\includegraphics` 选项 | 在 LaTeX 外用图像软件裁剪 |
| `viewport=...` | `\includegraphics` 选项 | 在 LaTeX 外用图像软件裁剪 |

### 负间距类

| 模式 | 说明 |
|------|------|
| `\vspace{-...}` | **严禁**在图、表、标题、节标题、参考文献附近使用 |
| `\vskip{-...}` | **严禁**在图、表、标题、节标题、参考文献附近使用 |

> 负间距在其他位置也极不推荐。AAAI 模板注释："may never be used around tables, figures, captions, sections, subsections, subsubsections, or references."

### 其他禁止

| 命令 | 说明 |
|------|------|
| `\nocopyright` | 禁用版权声明——论文将不被发表 |
| `\pubnote` | 不可在文档中使用 |
| `\balance` | 不可使用 |

## 允许的例外

| 例外 | 条件 |
|------|------|
| `\setlength{\tabcolsep}{1mm}` | 仅用于压缩表格列间距，是**唯一**允许的 setlength |

## 检查方法

```bash
python scripts/check_forbidden.py paper.tex
```

正则扫描所有禁用命令的出现。对 `\vspace{-` 和 `\vskip{-` 额外检查是否在图/表/节标题附近。

## 判定逻辑

```
IF 禁用命令出现 AND 非例外项 THEN
  → 🔴 CRITICAL：该命令会导致退稿
  → 修复：删除该命令

IF \setlength 出现 AND 参数非 \tabcolsep THEN
  → 🔴 CRITICAL

IF \vspace{- 或 \vskip{- 出现在 figure/table/section 环境 200 行内 THEN
  → 🔴 CRITICAL
```
