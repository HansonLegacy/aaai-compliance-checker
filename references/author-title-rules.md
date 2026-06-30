# Title & Author Formatting Rules — AAAI 2027

> 来源：`CameraReady2027.tex` §Title and Authors, §Formatting Author Information

## 标题规则

### Title Case（Chicago Manual of Style）

标题必须使用 Title Case，**非** Sentence case。规则：

- **大写**：动词（包括 be, is, using, go 等短动词）、名词、副词、形容词、代词、
  连字符术语的两个词
- **小写**：冠词（a, an, the）、连词（and, but, or）、介词（in, of, to, for...）
  —— 除非直接跟在冒号或长破折号后面

**验证工具**：https://titlecaseconverter.com/（选择 "Chicago" + "Show explanations"）

### 标题格式

- 位置：跨双栏居中
- 字体：16 pt 粗体
- 行距：24 pt
- 严禁手动调整标题格式（`\textbf`, `\Large`, `\huge`, `\textsf` 等）
- `\title{...}` 中可使用 `\\` 换行，可使用 `\thanks{...}` 添加脚注致谢

## 作者规则

### 单机构

```latex
\author{
    Author 1, Author 2, ..., Author n\\
}
\affiliations{
    Address line 1\\
    Address line 2\\
    email@example.com
}
```

- 作者之间用逗号分隔
- 机构地址每行一个 `\\`
- 邮件必须使用 Roman 字体（非 `\texttt`, `\url`）

### 多机构

```latex
\author{
    AuthorOne\equalcontrib\textsuperscript{\rm 1,\rm 2},
    AuthorTwo\equalcontrib\textsuperscript{\rm 2},
    AuthorThree\textsuperscript{\rm 3},\\
    AuthorFour\textsuperscript{\rm 4},\\
    AuthorFive\textsuperscript{\rm 5}
}
\affiliations{
    \textsuperscript{\rm 1}Affiliation One,\\
    \textsuperscript{\rm 2}Affiliation Two,\\
    ...
    email1@xxx.com, email2@xxx.com
}
```

### 关键规则

1. **上标关联**：多机构必须用 `\textsuperscript{\rm x}` 将作者与机构编号关联
2. **上标后逗号**：逗号放在上标**后面**，非前面
   - ✅ `AuthorOne\textsuperscript{\rm 1,\rm 2},`
   - ❌ `AuthorOne,\textsuperscript{\rm 1,\rm 2}`
3. **无空格**：作者名和上标之间无空格
4. **禁止 authblk**：严禁使用 `authblk` 包
5. **禁止 table 排作者**：严禁使用 `table` 环境排列作者信息
6. **换行**：用 `\\` 在作者列表中换行以改善可读性

### 特殊标记

| 命令 | 用途 | 位置 |
|------|------|------|
| `\equalcontrib` | 标注同等贡献 | 作者名后，上标前 |
| `\corresponding` | 标注通讯作者 | 作者名后，上标后 |
| `\thanks{...}` | 标题/作者脚注致谢 | `\title{}` 或 `\author{}` 内 |

### 作者格式

- 字体：12 pt
- 行距：15 pt
- 居中

### 机构格式

- 字体：9 pt Roman
- 行距：12 pt

## 匿名投稿特殊规则

- `\author{Anonymous Submission}`（固定文本）
- `\affiliations{}`（留空）
- 禁用 `links` 块（会泄露身份）
- PDF metadata 必须清理
- 自引文献需匿名化处理
- 使用 `\usepackage[submission]{aaai2027}` 自动去除版权声明

## 检查清单

- [ ] 标题经 Title Case 验证（titlecaseconverter.com Chicago 模式）
- [ ] `\author{...}` 格式符合单机构或多机构规范
- [ ] 无 `authblk` 包
- [ ] 无 `table` 环境用于作者排版
- [ ] 逗号在上标后面
- [ ] 上标用 `\rm` 字体
- [ ] 邮件地址用 Roman 字体
- [ ] 匿名投稿：作者 = "Anonymous Submission"，affiliations = {}
- [ ] Camera-Ready：版权声明存在
