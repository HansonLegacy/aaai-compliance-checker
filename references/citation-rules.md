# Citation Rules — AAAI 2027

> 来源：`CameraReady2027.tex` §Citations, §References

## 文内引用格式

### 基本格式
- `(作者姓 年份)` — 例如 `(Newell 1980)`
- 使用 `natbib` 的 `\cite{}` 命令自动生成

### 多作者处理

| 作者数 | 格式 | 示例 |
|--------|------|------|
| 1 位 | (姓 年份) | `(Newell 1980)` |
| 2 位 | (姓1 and 姓2 年份) | `(Feigenbaum and Engelmore 1988)` |
| 3 位 | (姓1, 姓2, and 姓3 年份) | `(Ford, Hayes, and Glymour 1992)` |
| 4+ 位 | (姓1 et al. 年份) | `(Ford et al. 1997)` |

### 年份歧义
- 同作者同年多篇：加小写字母区分 `(Li 2023a)`, `(Li 2023b)`

### Abstract 规则
- Abstract 中**不得**包含任何引用

## 参考文献列表

### 格式
- 使用 `aaai2027.bst` 样式文件
- **不可**手动设置 `\bibliographystyle{...}`（aaai2027.sty 自动设置）
- 使用 BibTeX 生成

### 字号
- 默认：与正文相同（10 pt）
- 超页时可缩小至 `\small`（9 pt）
- **不可**小于 9 pt

### 可用引用命令

| 命令 | 效果 |
|------|------|
| `\cite{key}` | 完整引用："(Author Year)" |
| `\shortcite{key}` | 仅年份："(Year)" |
| `\citeauthor{key}` | 仅作者名（无括号） |
| `\citeyear{key}` | 仅年份（无括号） |

以上及所有 `natbib` 标准命令均可使用。

### 参考文献条目类型

| 文献类型 | BibTeX class |
|----------|-------------|
| 书籍 | `@book` |
| 期刊/杂志 | `@article` |
| 会议论文 | `@inproceedings` |
| 技术报告 | `@techreport` |
| 博士论文 | `@phdthesis` |
| 即将出版 | `@misc` + `note="Forthcoming"` |
| arXiv | `@misc` + `eprint` + `archivePrefix="arXiv"` |
| 网页 | `@misc` + `howpublished="\url{...}"` + `note="Accessed: YYYY-mm-dd"` |

## 禁止项

| 禁止 | 原因 |
|------|------|
| `hyperref` 包 | 嵌入链接/书签，破坏参考文献 |
| `navigator` 包 | 嵌入 PDF 导航，破坏参考文献 |
| `\bibliographystyle{...}` | aaai2027.sty 已自动设置 |

## 检查清单

```
□ 文内引用格式正确（作者, 年份）
□ Abstract 无 \cite
□ 无 \bibliographystyle 命令
□ 使用 aaai2027.bst
□ 参考文献字号 ≥ \small
□ 无 hyperref / navigator
□ BibTeX 条目类型正确（@article, @inproceedings 等）
□ arXiv 论文使用 @misc + eprint
□ 网页资源标注 Accessed 日期
```
