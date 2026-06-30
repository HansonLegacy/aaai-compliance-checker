# Reproducibility Checklist Guide — AAAI 2027

> 来源：`AuthorKit27/ReproducibilityChecklist.tex`

## 概述

AAAI 2027 要求（或建议）提交可重复性清单。该清单涵盖 4 大板块，
以 `.tex` 文件形式提供，可 `\input` 到主论文中或作为独立文档编译。

## 四大检查板块

### 1. General Paper Structure（论文结构）

| # | 检查项 | 选项 |
|---|--------|------|
| 1.1 | 是否包含 AI 方法的概念描述或伪代码 | yes/partial/no/NA |
| 1.2 | 是否清晰区分观点/假设/推测与客观事实 | yes/no |
| 1.3 | 是否为不熟悉该领域的读者提供了教学性参考文献 | yes/no |

### 2. Theoretical Contributions（理论贡献）

| # | 检查项 | 选项 |
|---|--------|------|
| 2.0 | 论文是否有理论贡献？（如否，跳过本板块） | yes/no |
| 2.1 | 所有假设和限制是否清晰正式陈述 | yes/partial/no |
| 2.2 | 所有新声明是否正式陈述（如定理形式） | yes/partial/no |
| 2.3 | 所有新声明的证明是否包含 | yes/partial/no |
| 2.4 | 复杂/新颖结果是否给出证明草图或直觉 | yes/partial/no |
| 2.5 | 使用的理论工具是否有适当引用 | yes/partial/no |
| 2.6 | 所有理论声明是否经实证验证 | yes/partial/no/NA |
| 2.7 | 排除/反驳声明的实验代码是否包含 | yes/no/NA |

### 3. Dataset Usage（数据集使用）

| # | 检查项 | 选项 |
|---|--------|------|
| 3.0 | 论文是否依赖数据集？（如否，跳过本板块） | yes/no |
| 3.1 | 是否说明了选择该数据集的动机 | yes/partial/no/NA |
| 3.2 | 新引入的数据集是否包含在数据附录中 | yes/partial/no/NA |
| 3.3 | 新数据集是否将在发表后公开（允许免费研究使用） | yes/partial/no/NA |
| 3.4 | 来自已有文献的数据集是否有适当引用 | yes/no/NA |
| 3.5 | 来自已有文献的数据集是否公开可用 | yes/partial/no/NA |
| 3.6 | 非公开数据集是否有详细描述，是否解释了为何公开替代方案不满足需求 | yes/partial/no/NA |

### 4. Computational Experiments（计算实验）

| # | 检查项 | 选项 |
|---|--------|------|
| 4.0 | 论文是否包含计算实验？（如否，跳过本板块） | yes/no |
| 4.1 | 是否报告了每个超参数尝试的值数量/范围和最终选择标准 | yes/partial/no/NA |
| 4.2 | 数据预处理代码是否包含在附录 | yes/partial/no |
| 4.3 | 实验所需全部源代码是否包含在代码附录 | yes/partial/no |
| 4.4 | 源代码是否将在发表后公开（允许免费研究使用） | yes/partial/no |
| 4.5 | 新方法的源代码是否有注释说明实现细节和论文引用 | yes/partial/no |
| 4.6 | 如算法依赖随机性，是否描述了种子设置方法以保证可复现 | yes/partial/no/NA |
| 4.7 | 是否说明了计算基础设施（GPU/CPU 型号、内存、OS、库版本） | yes/partial/no |
| 4.8 | 是否正式描述了评估指标并解释了选择动机 | yes/partial/no |
| 4.9 | 是否说明了每个报告结果使用的算法运行次数 | yes/no |
| 4.10 | 实验分析是否超越单一维度汇总（均值/中位数），包含方差/置信度等 | yes/no |
| 4.11 | 性能提升/下降是否使用适当的统计检验（如 Wilcoxon signed-rank） | yes/partial/no |
| 4.12 | 是否列出了所有模型/算法的最终超参数 | yes/partial/no/NA |

## 填写方法

### 作为独立文档编译
```bash
pdflatex ReproducibilityChecklist.tex
```

### 嵌入主论文
在主 `.tex` 文件的 `\end{document}` 之前添加：
```latex
\input{ReproducibilityChecklist.tex}
```

### 填写规则
- 仅替换 "Type your response here" 文本
- 使用 `yes` / `no` / `partial` / `NA` 之一
- **不可**修改 `\question` 命令或其他任何行

## 检查要点

检查 `ReproducibilityChecklist.tex` 时确认：
1. 每项不再显示 "Type your response here"（已替换为具体回答）
2. 回答了所有适用的问题（包括子问题）
3. 对于标记为 `yes` 的板块（如 "Does this paper make theoretical contributions?"），
   其子问题已全部回答
4. 回答了 "no" 的项目在论文中有合理解释
5. `\input` 位置在 `\end{document}` 之前

## 判定逻辑

```
IF 清单中仍存在 "Type your response here" THEN
  → 🟡 WARNING：可重复性清单未完成

IF 适用板块标记为 yes 但子问题未填写 THEN
  → 🟡 WARNING

IF 清单完全缺失且会议要求提交 THEN
  → 🔴 CRITICAL
```
