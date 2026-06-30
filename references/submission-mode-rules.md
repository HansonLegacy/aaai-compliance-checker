# Submission Mode Differences — AAAI 2027

> 来源：`AnonymousSubmission2027.tex` §Preparing an Anonymous Submission

## 两种模式对照

| 项目 | 匿名投稿 (submission) | Camera-Ready |
|------|----------------------|--------------|
| `\usepackage` | `\usepackage[submission]{aaai2027}` | `\usepackage{aaai2027}` |
| 作者 | `Anonymous Submission` | 真实姓名 + 机构 |
| Affiliations | 留空 `{}` | 完整地址 + 邮件 |
| 版权声明 | 自动隐藏 | 自动插入 |
| Links 块 | **禁止**（暴露身份） | 允许 |
| PDF Metadata | 必须清理 | 可保留 |
| 自引文献 | 匿名化处理 | 正常引用 |
| 版权表格 | 不需提交 | 必须提交 |
| 可重复性清单 | 视会议要求 | 视会议要求 |

## 匿名投稿细节

### 1. 作者信息
```latex
% 匿名投稿模板
\usepackage[submission]{aaai2027}
...
\author{Anonymous Submission}
\affiliations{}
```

### 2. PDF Metadata
提交前用元数据清理工具清除 PDF 中的作者信息。
检查方法（Adobe Acrobat）：File → Properties → Description 标签页，
确保 Title、Author、Subject 等字段不包含身份信息。

### 3. 自引匿名化
参考文献中引用自己已发表工作时：
- 不要写 "In our previous work..."
- 改为 "Previous work (Author 20xx) has shown..."
- 可以暂时将自引条目的作者名替换为 "Anonymous"

### 4. Links 块
- 匿名投稿**必须完全删除** `links` 块
- 或者全部注释掉
- 代码/数据链接会直接暴露身份

### 5. Acknowledgments
- 匿名投稿中可以暂时省略或匿名化致谢中的资助信息
- Camera-Ready 时再补回

## Camera-Ready 特有要求

### 版权声明
- 由 `aaai2027.sty` 自动在首页底部插入
- **不可**使用 `\nocopyright`（会导致论文不被发表）
- 必须签署并返回版权表格

### Links 块
- 可以添加代码、数据、扩展版本的链接
- 位置：Abstract 和正文之间
```latex
\begin{links}
    \link{Code}{https://github.com/...}
    \link{Datasets}{https://...}
    \link{Extended version}{https://arxiv.org/abs/...}
\end{links}
```

## 检查清单

### 匿名投稿
```
□ \usepackage[submission]{aaai2027}
□ \author{Anonymous Submission}
□ \affiliations{} 为空
□ PDF metadata 已清理
□ 自引已匿名化
□ 无 links 块
□ 无版权声明
```

### Camera-Ready
```
□ \usepackage{aaai2027}（无 submission 选项）
□ 真实作者 + 机构信息
□ 版权声明存在
□ Links 块正确放置（可选）
□ Acknowledgments 完整
```
