# Forbidden Packages — AAAI 2027

> 来源：`CameraReady2027.tex` Table 2, §Commands and Packages That May Not Be Used

## 完整禁用包列表（25 项）

| 包名 | 原因 | 典型误用场景 |
|------|------|-------------|
| `authblk` | 冲突作者排版宏 | 用 `\affil` 排作者机构 |
| `babel` | 改变连字/间距 | 多语言支持 |
| `balance` | 干预双栏平衡 | 最后一页双栏对齐 |
| `cjk` | 非 Roman 字体 | 中文/日文/韩文字符 |
| `epsf` | 过时图形支持 | EPS 图支持 |
| `epsfig` | 过时图形支持 | EPS 图支持 |
| `euler` | 数学字体替换 | Euler 数学字体 |
| `float` | 改变浮动体行为 | `[H]` 强制定位 |
| `fullpage` | 改变页边距 | 扩大正文区域 |
| `geometry` | 改变页面尺寸/边距 | 调整页边距以容纳内容 |
| `graphics` | 与 graphicx 冲突 | 替代 graphics 接口 |
| `hyperref` | 嵌入链接/书签 | PDF 超链接、可点击引用 |
| `layout` | 改变页面布局 | 显示/修改布局参数 |
| `lmodern` | 替换字体族 | Latin Modern 字体 |
| `navigator` | 嵌入 PDF 导航 | PDF 书签/缩略图 |
| `pdfcomment` | PDF 注释 | 添加批注 |
| `pgfplots` | 运行时生成图形 | **必须预导出为 PDF 再导入** |
| `psfig` | 过时图形支持 | PostScript 图支持 |
| `pstricks` | PostScript 特殊效果 | PSTricks 绘图 |
| `t1enc` | 字体编码冲突 | T1 字体编码 |
| `times` | 与 newtxtext 冲突 | 尝试设置 Times 字体 |
| `titlesec` | 改变节标题格式 | 自定义 section 样式 |
| `tocbibind` | 改变目录/引用格式 | 自定义参考文献样式 |
| `ulem` | 改变下划线/强调 | `\uline` 下划线命令 |

## 模板注释中额外列出的禁止包（不在 Table 2 但同等重要）

| 包名 | 原因 |
|------|------|
| `flushend` | 干预双栏平衡 |
| `indentfirst` | 改变段首缩进 |
| `multicol` | 改变栏目数 |
| `nameref` | 与引用系统冲突 |
| `savetrees` | 压缩版式节省空间 |
| `setspace` | 改变行距 |
| `stfloats` | 改变浮动体行为 |
| `tabu` | 过时的表格包 |
| `wrapfig` | 文字环绕图形 |

## 检查要点

1. 搜索 `\usepackage{...}` 中出现的包名
2. 注意包名可能以多种形式出现（如 `\usepackage{geometry}`, `\RequirePackage{geometry}`）
3. `pgfplots` 特别危险——许多人用它生成图表但忘记预导出
4. `hyperref` 是最常见的违规——很多人习惯性加载它来做交叉引用

## 判定逻辑

```
IF 包名 in 禁用列表 THEN
  → 🔴 CRITICAL：该包会导致退稿
  → 修复：删除 \usepackage{包名}，移除所有对该包命令的依赖
```
