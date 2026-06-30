# Figure & Table Rules — AAAI 2027

> 来源：`CameraReady2027.tex` §Illustrations and Figures, §Tables

## 图形（Figures）

### 文件格式

| 允许 | 禁止 |
|------|------|
| `.jpg` | `.gif`（分辨率过低） |
| `.png` | `.eps` |
| `.pdf` | `.ps` |

### 分辨率
- 位图最低 **300 dpi**
- 禁止 72 dpi 屏幕截图
- 矢量图优先

### 裁剪
- **必须在 LaTeX 外**用图像软件裁剪
- **禁止**以下命令/选项：
  - `clip=true`
  - `trim=...`
  - `viewport=...`
  - `\includegraphics*[clip,...]{...}`
- 原因：裁剪不彻底会导致隐藏图层在最终出版时重现

### pgfplots
- **禁止**在正文中使用 `pgfplots` 包
- 须预导出为 PDF，再用 `\includegraphics` 导入
- pgfplots 生成的边界框不稳定

### 放置
- 优先 `[t]`（页面顶部），其次 `[b]`（页面底部）
- 在首次讨论的页面或下一页出现
- **不得**集中堆放在文末
- 跨栏图用 `figure*` 环境

### 禁止项
- `minipage` 组合多图
- `\begin{center}...\end{center}`（用 `\centering` 代替，节省空间）
- 图形侵入上/下/侧边距

### 图注（Caption）
- 位置：图**下方**
- 字体：10 pt Roman
- **不可**加粗、斜体（个别单词需要区分时可斜体）
- 标签和图形内文字 ≥ 9 pt
- 推荐宽度：`0.9\columnwidth`（单栏）或 `0.8\textwidth`（跨栏）

### 图形内文字
- 使用 Times Roman 或 Helvetica
- 线宽 ≥ 0.5 pt（禁止发丝线）
- 所有字体必须嵌入
- 推荐使用 Adobe Illustrator 或类似工具

### 颜色
- 灰度打印测试必须通过
- 色盲友好
- 不只靠颜色区分信息

## 表格（Tables）

### 字号
- 默认：10 pt Roman
- 必要时：9 pt（不可更小）

### 禁止项
- `\resizebox{...}{...}{...}` — 无法控制最终字号
- `\tiny`, `\scriptsize` 等字号命令

### 允许的压缩方法
- `\setlength{\tabcolsep}{1mm}` — **唯一**允许的 setlength 例外
- 减少数值小数位数
- 缩短列标题
- 某些列使用双行

### 跨栏
- 单栏放不下 → 使用 `table*` 跨双栏
- 跨双栏仍放不下 → 拆分为两个独立表格

### 表注（Caption）
- 位置：表**下方**（不是上方）
- 字体：10 pt Roman
- **不可**加粗、斜体

### 推荐
- 使用 `booktabs` 包（`\toprule`, `\midrule`, `\bottomrule`）

## 算法（Algorithms）

- 推荐：`algorithm` + `algorithmic` 包
- 作为浮动体，优先 `[t]` 或 `[b]`
- 标题在算法**上方**，左对齐，用横线包围
- 算法体以另一条横线结束
- 行号可选

## 代码列表（Listings）

- 推荐：`newfloat` + `listings` 包
- 作为浮动体，优先 `[t]` 或 `[b]`
- 标题在代码**上方**，左对齐，用横线包围
- 行号必须在文本栏内
- 禁止背景色

## 检查清单

```
□ 所有图为 .jpg / .png / .pdf
□ 分辨率 ≥ 300 dpi
□ 裁剪在 LaTeX 外完成（无 clip/trim/viewport）
□ 无 minipage 组合图
□ 无 pgfplots 包
□ 图注/表注在下方，10pt Roman，未加粗/斜体
□ 表无 \resizebox
□ 浮动体优先 [t]/[b]
□ 颜色满足 WCAG 2.0
□ 灰度打印测试通过
□ 无 overfull boxes
```
