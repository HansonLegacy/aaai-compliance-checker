# Formatting Specifications — AAAI 2027

> 来源：`CameraReady2027.tex` §Paper Size, Margins, §Type Font and Size, §Text

## 纸张与页边距

| 参数 | 值 |
|------|-----|
| 纸张尺寸 | US Letter (8.5 × 11 inch) |
| 首页上边距 | 1.25 inch |
| 其余页上边距 | 0.75 inch |
| 左边距 | 0.75 inch |
| 右边距 | 0.75 inch |
| 下边距 | 1.25 inch |

> 由 `aaai2027.sty` 自动设置，严禁用 `geometry` 包覆盖。

## 双栏布局

| 参数 | 值 |
|------|-----|
| 栏数 | 2 |
| 每栏宽度 | 3.3 inch |
| 栏间距 (gutter) | 0.375 inch (0.952 cm) |

## 字体

| 元素 | 字体 | 字号 | 行距 |
|------|------|------|------|
| 正文 | Times Roman（newtxtext） | 10 pt | 12 pt |
| 标题 | Times Roman 粗体 | 16 pt | 24 pt |
| 作者 | Times Roman | 12 pt | 15 pt |
| 机构 | Times Roman | 9 pt | 12 pt |
| 图注/表注 | Times Roman | 10 pt | — |
| 表格内容 | Times Roman | 10 pt（必要时 9 pt） | — |
| 参考文献 | Times Roman | 10 pt（必要时 `\small` 即 9 pt） | 10 pt |
| 脚注 | Times Roman | — | — |
| 数学公式 | Computer Modern / Symbol / Lucida | ≥ 6.5 pt | — |
| 代码 | Courier（\ttfamily） | `\footnotesize` | — |
| 页脚版权声明 | — | — | — |

### 字体规则

- **Serif**: `newtxtext`（样式文件自动加载）
- **Sans-serif**: Helvetica / `helvet`（样式文件自动加载）
- **Monospace**: Courier / `courier`（样式文件自动加载）
- **数学**: Computer Modern, Symbol, 或 Lucida
- **严禁** Computer Modern 或 Palatino 用于正文
- **严禁** Type 3 字体（包括图形中的）
- **严禁** 非 Roman 字母的字体包（CJK、阿拉伯语等），必须改用图片

## 段落

- 段首缩进：10 pt
- 段落直接跟在标题/子标题下方时不缩进
- `\frenchspacing` 必须启用（句号后不额外加空格）

## 颜色

- 正文文字**禁止**使用颜色
- 图和少量文字细节（单词级别）可使用颜色
- 颜色必须满足 WCAG 2.0 对比度 ≥ 4.5:1
- 灰度打印必须可读

## 行距与间距

- 正文：12 pt leading
- **禁止修改**任何间距参数（`\baselinestretch`, `\linespread` 等）
- 节标题上下间距由样式文件自动控制，不可修改

## 页面溢出

- **严禁**内容溢出到页边距或栏间距
- 检查 `.log` 文件中的 `overfull` 警告
- `Overfull \hbox` → 调整内容或改用跨栏环境
