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
    An AAAI 2027 LaTeX formatting compliance checker for Claude Code & OpenAI Codex CLI.
    <br />
    <a href="#-usage"><strong>Explore the docs »</strong></a>
    <br />
    <br />
    <a href="https://github.com/HansonLegacy/aaai-compliance-checker/issues/new?labels=bug">Report Bug</a>
    &nbsp;·&nbsp;
    <a href="https://github.com/HansonLegacy/aaai-compliance-checker/issues/new?labels=enhancement">Request Feature</a>
  </p>

  <p align="center">
    🌐 <a href="README.md"><strong>English</strong></a>
    &nbsp;|&nbsp;
    <a href="README-zh.md">中文</a>
  </p>
</div>

<!-- TABLE OF CONTENTS -->
<details>
  <summary>Table of Contents</summary>
  <ol>
    <li><a href="#about-the-project">About The Project</a></li>
    <li><a href="#check-dimensions">Check Dimensions</a></li>
    <li>
      <a href="#getting-started">Getting Started</a>
      <ul>
        <li><a href="#prerequisites">Prerequisites</a></li>
        <li><a href="#installation">Installation</a></li>
      </ul>
    </li>
    <li><a href="#usage">Usage</a></li>
    <li><a href="#roadmap">Roadmap</a></li>
    <li><a href="#contributing">Contributing</a></li>
    <li><a href="#license">License</a></li>
    <li><a href="#contact">Contact</a></li>
    <li><a href="#acknowledgments">Acknowledgments</a></li>
  </ol>
</details>

<!-- ABOUT THE PROJECT -->
## About The Project

**AAAI Compliance Checker** is a Claude Code / Codex CLI skill that systematically validates LaTeX papers against the [AAAI 2027 Author Kit](https://aaai.org/authorkit27/) formatting requirements. It automates what is traditionally a tedious manual checklist — scanning your `.tex` source (and compiled PDF) for violations, then producing a structured, severity-ranked report.

### Why not just read the Author Kit?

The AAAI Author Kit is a 30-page PDF. It lists dozens of forbidden packages, commands, preamble requirements, and structural rules — all spread across multiple sections. Missing even one can lead to desk rejection. This skill:

- **Automates the mechanical checks** (preamble, forbidden packages/commands, section ordering)
- **Surfaces the exact line number** of every violation
- **Provides fix suggestions** with references back to the Author Kit
- **Works across tools** — same skill file runs in both Claude Code and Codex CLI

### Output Example

```
[CRITICAL] Line 8: Forbidden package: \usepackage{hyperref}
            hyperref is incompatible with aaai2027.sty
            Fix: Remove the line and all dependencies on hyperref

[WARNING]  Line 34: Title may not be Title Case: "a novel approach"
            Fix: Verify at https://titlecaseconverter.com/ (Chicago style)

[INFO]     Line 498: Acknowledgments ~5 sentences (guideline: <= 3)

[PASS]     22 items verified compliant
```

<p align="right">(<a href="#readme-top">back to top</a>)</p>

<!-- CHECK DIMENSIONS -->
## Check Dimensions

| # | Dimension | Method | Description |
|---|-----------|--------|-------------|
| 1 | Submission Mode | Manual | Anonymous submission vs Camera-Ready identification |
| 2 | Preamble | ✅ Script | 10 required lines, 15+ forbidden packages |
| 3 | Forbidden Content | ✅ Script | 25+ forbidden packages, 20+ forbidden commands |
| 4 | Title & Authors | Semi-auto | Title Case (Chicago), author affiliation format |
| 5 | Section Structure | ✅ Script | Ordering, numbering, naming conventions |
| 6 | Figures & Tables | Semi-auto | Format (.jpg/.png/.pdf), resolution, captions |
| 7 | Citations | Semi-auto | In-text format, bibliography style, abstract rules |
| 8 | PDF Checks | Manual | Font embedding, Type 3 detection, PDF version |
| 9 | Reproducibility | Semi-auto | Reproducibility Checklist completeness |
| 10 | Submission Files | Manual | File manifest, archive naming, size limit |

<p align="right">(<a href="#readme-top">back to top</a>)</p>

<!-- GETTING STARTED -->
## Getting Started

### Prerequisites

- Python 3.6+ (stdlib only — zero dependencies)
- [Claude Code](https://claude.ai/code) **or** [OpenAI Codex CLI](https://developers.openai.com/codex)
- A LaTeX paper targeting AAAI 2027

### Installation

#### Claude Code

```bash
# Option 1: Plugin install (recommended)
claude plugins install github.com/HansonLegacy/aaai-compliance-checker

# Option 2: Manual copy
git clone https://github.com/HansonLegacy/aaai-compliance-checker.git
cp -r aaai-compliance-checker/* ~/.claude/skills/aaai-compliance-checker/
```

#### Codex CLI

```bash
git clone https://github.com/HansonLegacy/aaai-compliance-checker.git
cp -r aaai-compliance-checker/* ~/.agents/skills/aaai-compliance-checker/
```

<p align="right">(<a href="#readme-top">back to top</a>)</p>

<!-- USAGE -->
## Usage

### Via Natural Language (Skill Auto-Trigger)

In any Claude Code or Codex CLI session:

> "Check my paper against AAAI 2027 formatting requirements."
>
> "Validate AAAI submission compliance."
>
> "Run AAAI format check on my LaTeX paper."

Or invoke explicitly:
- Claude Code: `/aaai-compliance-checker`
- Codex CLI: `$aaai-compliance-checker`

### Via Python Scripts (Standalone)

```bash
# Run all three automated checks
python scripts/check_preamble.py paper.tex      # Preamble compliance
python scripts/check_forbidden.py paper.tex     # Scan for forbidden content
python scripts/check_structure.py paper.tex     # Section structure verification
```

Each script exits with code `0` (pass) or `1` (issues found) — suitable for CI pipelines.

<p align="right">(<a href="#readme-top">back to top</a>)</p>

<!-- ROADMAP -->
## Roadmap

- [x] Preamble compliance check (10 required lines)
- [x] Forbidden packages scan (25+ packages)
- [x] Forbidden commands scan (20+ commands)
- [x] Section structure & ordering check
- [x] Claude Code plugin support
- [x] Codex CLI agent skill compatibility
- [x] Dual-language documentation (EN / 中文)
- [ ] PDF-level automated checks (font embedding, Type 3 detection)
- [ ] Title Case auto-validation via titlecaseconverter.com
- [ ] LaTeX log file parser for overfull box detection
- [ ] CI/CD integration example (GitHub Actions)
- [ ] AAAI 2028 support (when Author Kit is released)

See the [open issues](https://github.com/HansonLegacy/aaai-compliance-checker/issues) for a full list of proposed features.

<p align="right">(<a href="#readme-top">back to top</a>)</p>

<!-- CONTRIBUTING -->
## Contributing

Contributions are what make the open source community such an incredible place to learn, inspire, and create. Any contributions you make are **greatly appreciated**.

1. Fork the Project
2. Create your Feature Branch (`git checkout -b feature/AmazingFeature`)
3. Commit your Changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the Branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

<p align="right">(<a href="#readme-top">back to top</a>)</p>

<!-- LICENSE -->
## License

Distributed under the MIT License. See `LICENSE` for more information.

<p align="right">(<a href="#readme-top">back to top</a>)</p>

<!-- CONTACT -->
## Contact

HansonLegacy — [@HansonLegacy](https://github.com/HansonLegacy)

Project Link: [https://github.com/HansonLegacy/aaai-compliance-checker](https://github.com/HansonLegacy/aaai-compliance-checker)

<p align="right">(<a href="#readme-top">back to top</a>)</p>

<!-- ACKNOWLEDGMENTS -->
## Acknowledgments

- [AAAI 2027 Author Kit](https://aaai.org/authorkit27/) — official formatting specification
- [Best-README-Template](https://github.com/othneildrew/Best-README-Template)
- [Anthropic Claude Code Skills Documentation](https://github.com/anthropics/claude-code)
- [OpenAI Codex CLI Agent Skills](https://developers.openai.com/codex/skills)

<p align="right">(<a href="#readme-top">back to top</a>)</p>

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
