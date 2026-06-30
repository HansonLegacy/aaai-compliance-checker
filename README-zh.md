<a id="readme-top"></a>

<!-- PROJECT SHIELDS -->
[![Contributors][contributors-shield]][contributors-url]
[![Forks][forks-shield]][forks-url]
[![Stargazers][stars-shield]][stars-url]
[![Issues][issues-shield]][issues-url]
[![MIT License][license-shield]][license-url]

<!-- PROJECT LOGO -->
<br />
<div align="center">
  <h3>🔍 AAAI Compliance Checker</h3>
  <p align="center">
    AAAI 2027 LaTeX 论文格式合规检查器 —— 适用于 Claude Code 和 OpenAI Codex CLI。
    <br />
    <a href="#-使用方法"><strong>探索文档 »</strong></a>
    <br />
    <br />
    <a href="https://github.com/HansonLegacy/aaai-compliance-checker/issues/new?labels=bug">报告 Bug</a>
    &nbsp;·&nbsp;
    <a href="https://github.com/HansonLegacy/aaai-compliance-checker/issues/new?labels=enhancement">请求新功能</a>
  </p>

  <p align="center">
    <a href="README.md"><strong>English</strong></a>
    &nbsp;|&nbsp;
    🌐 <a href="README-zh.md">中文</a>
  </p>
</div>

<!-- TABLE OF CONTENTS -->
<details>
  <summary>目录</summary>
  <ol>
    <li><a href="#关于本项目">关于本项目</a></li>
    <li><a href="#检查维度">检查维度</a></li>
    <li>
      <a href="#快速开始">快速开始</a>
      <ul>
        <li><a href="#前置条件">前置条件</a></li>
        <li><a href="#安装">安装</a></li>
      </ul>
    </li>
    <li><a href="#使用方法">使用方法</a></li>
    <li><a href="#路线图">路线图</a></li>
    <li><a href="#贡献">贡献</a></li>
    <li><a href="#许可证">许可证</a></li>
    <li><a href="#联系方式">联系方式</a></li>
    <li><a href="#致谢">致谢</a></li>
  </ol>
</details>

<!-- ABOUT THE PROJECT -->
## 关于本项目

**AAAI Compliance Checker** 是一个 Claude Code / Codex CLI 技能，能够根据 [AAAI 2027 Author Kit](https://aaai.org/authorkit27/) 格式规范，对 LaTeX 论文进行系统性合规检查。它自动完成传统上需要逐项手工核对的工作——扫描 `.tex` 源文件（及编译后的 PDF），输出按严重程度分级的结构化报告。

### 为什么不直接看 Author Kit？

AAAI Author Kit 是一份 30 页的 PDF，分散列出了数十条禁用包、命令、preamble 要求以及结构规则。遗漏任何一条都可能导致直接退稿。本技能：

- **自动化机械性检查**（preamble、禁用包/命令、章节顺序）
- **精确定位行号**，直指违规位置
- **提供修复建议**，附带回引 Author Kit 的具体规则
- **跨工具运行**——同一份技能文件同时支持 Claude Code 和 Codex CLI

### 输出示例

```
[CRITICAL] 第 8 行: 禁用包: \usepackage{hyperref}
            hyperref 与 aaai2027.sty 不兼容
            修复: 删除该行并移除所有对 hyperref 的依赖

[WARNING]  第 34 行: 标题可能不是 Title Case: "a novel approach"
            修复: 在 https://titlecaseconverter.com/ 验证（选 Chicago 风格）

[INFO]     第 498 行: Acknowledgments 约 5 句（建议 ≤ 3 句）

[PASS]     22 项检查通过
```

<p align="right">(<a href="#readme-top">回到顶部</a>)</p>

<!-- CHECK DIMENSIONS -->
## 检查维度

| # | 检查项 | 方式 | 说明 |
|---|--------|------|------|
| 1 | 提交模式 | 手动 | 识别匿名投稿 vs Camera-Ready |
| 2 | Preamble | ✅ 脚本 | 10 项必要行，15+ 项禁用包 |
| 3 | 禁用内容 | ✅ 脚本 | 25+ 禁用包，20+ 禁用命令 |
| 4 | 标题与作者 | 半自动 | Title Case（Chicago）、作者机构格式 |
| 5 | 章节结构 | ✅ 脚本 | 顺序、编号、命名规范 |
| 6 | 图表规范 | 半自动 | 格式（.jpg/.png/.pdf）、分辨率、标注 |
| 7 | 引用格式 | 半自动 | 文内引用、参考文献样式、Abstract 规则 |
| 8 | PDF 检查 | 手动 | 字体嵌入、Type 3 检测、PDF 版本 |
| 9 | 可重复性 | 半自动 | 可重复性清单填写完整性 |
| 10 | 提交文件 | 手动 | 文件清单、压缩包命名、大小限制 |

<p align="right">(<a href="#readme-top">回到顶部</a>)</p>

<!-- GETTING STARTED -->
## 快速开始

### 前置条件

- Python 3.6+（仅依赖标准库——零额外依赖）
- [Claude Code](https://claude.ai/code) **或** [OpenAI Codex CLI](https://developers.openai.com/codex)
- 一篇准备投稿 AAAI 2027 的 LaTeX 论文

### 安装

#### Claude Code

```bash
# 方式一：插件安装（推荐）
claude plugins install github.com/HansonLegacy/aaai-compliance-checker

# 方式二：手动复制
git clone https://github.com/HansonLegacy/aaai-compliance-checker.git
cp -r aaai-compliance-checker/* ~/.claude/skills/aaai-compliance-checker/
```

#### Codex CLI

```bash
git clone https://github.com/HansonLegacy/aaai-compliance-checker.git
cp -r aaai-compliance-checker/* ~/.agents/skills/aaai-compliance-checker/
```

<p align="right">(<a href="#readme-top">回到顶部</a>)</p>

<!-- USAGE -->
## 使用方法

### 自然语言触发（技能自动激活）

在 Claude Code 或 Codex CLI 会话中直接说：

> "检查我的论文是否符合 AAAI 2027 格式要求。"
>
> "AAAI 投稿格式检查。"
>
> "帮我验证论文是否符合 AAAI Author Kit 规范。"

或显式调用：
- Claude Code：`/aaai-compliance-checker`
- Codex CLI：`$aaai-compliance-checker`

### 手动运行脚本

```bash
# 运行三项自动检查
python scripts/check_preamble.py paper.tex      # Preamble 合规检查
python scripts/check_forbidden.py paper.tex     # 禁用内容扫描
python scripts/check_structure.py paper.tex     # 章节结构验证
```

每个脚本退出码：`0`（通过）或 `1`（发现问题）——适合接入 CI 流水线。

<p align="right">(<a href="#readme-top">回到顶部</a>)</p>

<!-- ROADMAP -->
## 路线图

- [x] Preamble 合规检查（10 项必要行）
- [x] 禁用包扫描（25+ 项）
- [x] 禁用命令扫描（20+ 项）
- [x] 章节结构与顺序检查
- [x] Claude Code 插件支持
- [x] Codex CLI agent skill 兼容
- [x] 中英双语文档
- [ ] PDF 自动检查（字体嵌入、Type 3 检测）
- [ ] Title Case 自动验证（接入 titlecaseconverter.com）
- [ ] LaTeX log 文件解析（overfull box 检测）
- [ ] CI/CD 集成示例（GitHub Actions）
- [ ] AAAI 2028 支持（待 Author Kit 发布）

查看 [open issues](https://github.com/HansonLegacy/aaai-compliance-checker/issues) 获取完整的功能规划列表。

<p align="right">(<a href="#readme-top">回到顶部</a>)</p>

<!-- CONTRIBUTING -->
## 贡献

开源社区的壮大离不开每个人的贡献。任何形式的贡献都**非常感谢**。

1. Fork 本项目
2. 创建特性分支（`git checkout -b feature/AmazingFeature`）
3. 提交更改（`git commit -m 'Add some AmazingFeature'`）
4. 推送到分支（`git push origin feature/AmazingFeature`）
5. 发起 Pull Request

<p align="right">(<a href="#readme-top">回到顶部</a>)</p>

<!-- LICENSE -->
## 许可证

基于 MIT License 分发。详见 `LICENSE` 文件。

<p align="right">(<a href="#readme-top">回到顶部</a>)</p>

<!-- CONTACT -->
## 联系方式

HansonLegacy — [@HansonLegacy](https://github.com/HansonLegacy)

项目链接：[https://github.com/HansonLegacy/aaai-compliance-checker](https://github.com/HansonLegacy/aaai-compliance-checker)

<p align="right">(<a href="#readme-top">回到顶部</a>)</p>

<!-- ACKNOWLEDGMENTS -->
## 致谢

- [AAAI 2027 Author Kit](https://aaai.org/authorkit27/) — 官方格式规范
- [Best-README-Template](https://github.com/othneildrew/Best-README-Template)
- [Anthropic Claude Code Skills 文档](https://github.com/anthropics/claude-code)
- [OpenAI Codex CLI Agent Skills](https://developers.openai.com/codex/skills)

<p align="right">(<a href="#readme-top">回到顶部</a>)</p>

<!-- MARKDOWN LINKS & IMAGES -->
[contributors-shield]: https://img.shields.io/github/contributors/HansonLegacy/aaai-compliance-checker.svg?style=for-the-badge
[contributors-url]: https://github.com/HansonLegacy/aaai-compliance-checker/graphs/contributors
[forks-shield]: https://img.shields.io/github/forks/HansonLegacy/aaai-compliance-checker.svg?style=for-the-badge
[forks-url]: https://github.com/HansonLegacy/aaai-compliance-checker/network/members
[stars-shield]: https://img.shields.io/github/stars/HansonLegacy/aaai-compliance-checker.svg?style=for-the-badge
[stars-url]: https://github.com/HansonLegacy/aaai-compliance-checker/stargazers
[issues-shield]: https://img.shields.io/github/issues/HansonLegacy/aaai-compliance-checker.svg?style=for-the-badge
[issues-url]: https://github.com/HansonLegacy/aaai-compliance-checker/issues
[license-shield]: https://img.shields.io/github/license/HansonLegacy/aaai-compliance-checker.svg?style=for-the-badge
[license-url]: https://github.com/HansonLegacy/aaai-compliance-checker/blob/master/LICENSE
