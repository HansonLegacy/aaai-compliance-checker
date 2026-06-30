# AAAI Compliance Checker

An AAAI 2027 LaTeX formatting compliance checker for Claude Code & OpenAI Codex CLI.

Given a paper's `.tex` source file (and PDF), it systematically checks compliance against the AAAI 2027 Author Kit, producing a structured report ranked by severity.

## Installation

### Claude Code

```bash
cp -r skills/* ~/.claude/skills/aaai-compliance-checker/
```

Or install as a plugin:
```bash
claude plugins install github.com/HansonLegacy/aaai-compliance-checker
```

### Codex CLI

```bash
cp -r skills/* ~/.agents/skills/aaai-compliance-checker/
```

## Usage

### Natural Language Trigger

In a Claude Code / Codex CLI session:
- "check AAAI format"
- "validate AAAI submission"
- "format check my paper"
- `/aaai-compliance-checker`

### Run Scripts Manually

```bash
python scripts/check_preamble.py paper.tex     # Preamble compliance
python scripts/check_forbidden.py paper.tex    # Forbidden packages/commands scan
python scripts/check_structure.py paper.tex    # Section structure check
```

All scripts use only Python 3.6+ standard library — zero dependencies.

## Check Dimensions

| # | Dimension | Automated | Description |
|---|-----------|-----------|-------------|
| 1 | Submission mode | Manual | Anonymous submission vs Camera-Ready |
| 2 | Preamble | ✅ Script | Required/forbidden lines |
| 3 | Forbidden content | ✅ Script | 25+ forbidden packages, 20+ forbidden commands |
| 4 | Title & authors | Semi-auto | Title Case + author formatting |
| 5 | Section structure | ✅ Script | Ordering, naming, numbering |
| 6 | Figures & tables | Semi-auto | Format, resolution, captions |
| 7 | Citations | Semi-auto | In-text + bibliography format |
| 8 | PDF checks | Manual | Font embedding, Type 3 detection, version |
| 9 | Reproducibility | Semi-auto | Checklist completeness |
| 10 | Submission files | Manual | File manifest, naming, size |

## Output Format

```
[CRITICAL] — Desk-rejection level (forbidden packages/commands, font conflicts)
[WARNING]  — Format violations (wrong font size, figure format, section order)
[INFO]     — Recommendations (Title Case tweaks, citation nuances)
[PASS]     — Verified compliant items
```

See `examples/sample-report.md` for a complete example.

## Dependencies

- Python 3.6+ (stdlib only)
- AAAI 2027 Author Kit (included in `AuthorKit27/`, also available from [AAAI](https://aaai.org/))

## Directory Structure

```
aaai-compliance-checker/
├── SKILL.md                    # Core skill definition
├── plugin.json                 # Claude Code plugin manifest
├── agents/
│   └── openai.yaml             # Codex CLI metadata
├── references/                 # Detailed rule docs (10 files)
├── scripts/                    # Python automation scripts
├── examples/                   # Sample compliance reports
└── AuthorKit27/                # AAAI 2027 official template (reference)
```

## License

MIT © 2026 HansonLegacy
