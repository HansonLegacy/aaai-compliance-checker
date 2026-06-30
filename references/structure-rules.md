# Section Structure Rules — AAAI 2027

> 来源：`CameraReady2027.tex` §Headings and Sections, §Section Headings, §References

## 强制顺序

论文各部分的出现顺序必须严格遵守：

```
1. Abstract                          （必须）
2. [links 块]                        （仅 Camera-Ready，可选）
3. 正文各节                           （必须）
4. Content Appendices                 （可选，计入页数）
5. Ethical Statement                  （可选，unnumbered）
6. Acknowledgments                    （可选，unnumbered，≤ 3 句）
7. References                         （必须，unnumbered）
8. Supplementary Material / Technical Appendices （仅会议允许时）
```

## 各节详细规则

### Abstract
- 位置：`\maketitle` 之后，`links` 块（如有）之前
- **不得包含引用**（`\cite`, `\citep`, `\citet` 等）
- 自动缩进，不要额外缩进

### Links 块
- 位置：Abstract 之后，正文之前
- 仅在 Camera-Ready 模式下使用
- 匿名投稿**禁止**——链接会暴露身份
- 格式：
  ```latex
  \begin{links}
      \link{Code}{https://...}
      \link{Datasets}{https://...}
      \link{Extended version}{https://...}
  \end{links}
  ```

### 正文各节
- 使用 `\section{...}` 和 `\subsection{...}`
- **不支持** `\subsubsection{...}`（secnumdepth 最大 2）
- 节编号可选：`\setcounter{secnumdepth}{0}`（无编号）/ `1`（节编号）/ `2`（节+子节编号）
- 不要过多使用标题（短论文不需要太多层级）

### Content Appendices
- 使用 `\appendix` 命令后跟 `\section{...}`
- 自动使用字母编号（A, B, C...）
- 计入页数限制
- 接受相同的格式和审稿要求

### Ethical Statement
- **必须 unnumbered**：`\section*{Ethical Statement}`
- 标题必须精确为 "Ethical Statement"
- 内容：工作的伦理影响、社会意义（正面和负面）

### Acknowledgments
- **必须 unnumbered**：`\section*{Acknowledgments}`
- 标题必须精确为 "Acknowledgments"（美式拼写，无 "e" 在 "g" 后）
- 限制 ≤ 3 句
- 不在第一页脚注中放致谢（可用 `\thanks` 放必要的资助声明）
- 内容：同事帮助、资助机构、财务支持、出版许可

### References
- **必须 unnumbered**（自动如此）
- 标题自动为 "References"
- 位置：论文最末尾（**不要在 References 后再放图**）
- 紧接上文，无断页命令
- 使用 `\bibliography{...}` 生成
- 不可手动添加 `\bibliographystyle`（aaai2027.sty 已设置）

### Supplementary Material
- 仅在会议明确允许时提供
- 不同会议政策不同（有的要求单独文件，有的不允许）
- 查阅具体会议的投稿说明

## 禁止的结构性操作

| 操作 | 严重性 |
|------|--------|
| `\input{section1.tex}` 等拆分章节 | 🔴 CRITICAL — 必须是单个 .tex 文件 |
| `\newpage`, `\clearpage`, `\pagebreak` | 🔴 CRITICAL |
| `\pagestyle{...}` 设置页码 | 🔴 CRITICAL |
| References 后放置浮动体（图/表） | 🟡 WARNING |
| 正文中手动调整节标题格式 | 🔴 CRITICAL |
| `\subsubsection{...}` 使用超过 2 级的编号 | 🟡 WARNING |

## 允许的例外

- `\input{ReproducibilityChecklist.tex}` — 在 `\end{document}` 前输入可重复性清单
- `.bib` 文件 — 通过 `\bibliography{...}` 引用，不算拆分子文件

## 快速检查

```
□ Abstract 无 \cite
□ Links 块仅 Camera-Ready，位置在 abstract 后正文前
□ 正文 → Content Appendices → Ethical Statement → Acknowledgments → References
□ Ethical Statement 使用 \section*{}
□ Acknowledgments 使用 \section*{}，≤ 3 句
□ References 在 \end{document} 之前
□ 无 \input 拆分正文
□ 无断页命令
□ 无 \pagestyle
```
