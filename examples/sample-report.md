# AAAI 2027 Compliance Report — Sample

**Paper**: `example_paper.tex`  
**Mode**: Camera-Ready  
**Date**: 2026-06-30

---

## 🔴 CRITICAL (3 issues) — Must Fix Before Submission

| # | Check | Line | Issue | Fix |
|---|-------|------|-------|-----|
| 1 | Preamble | 12 | Missing: `\frenchspacing` | Add `\frenchspacing` before `\begin{document}` |
| 2 | Forbidden Packages | 8 | `\usepackage{hyperref}` detected | Remove the package; use `\ref{}` for cross-references |
| 3 | Forbidden Commands | 245 | `\vspace{-0.5cm}` near figure caption | Remove negative vspace; crop figure externally instead |

---

## 🟡 WARNING (5 issues) — Should Fix

| # | Check | Line | Issue | Fix |
|---|-------|------|-------|-----|
| 1 | Title | 34 | Title may not be Title Case: "a novel approach" should be "A Novel Approach" | Verify at https://titlecaseconverter.com/ (Chicago style) |
| 2 | Structure | 156 | Abstract contains `\cite{he2016deep}` | Move citation to the main text |
| 3 | Figures | 189 | `\includegraphics[clip=true]{fig3.pdf}` | Remove `clip=true`; crop in external software |
| 4 | Author | 28 | Comma placed before superscript: `Author,\textsuperscript{\rm 1}` | Change to `Author\textsuperscript{\rm 1},` |
| 5 | Tables | 312 | `\resizebox{\columnwidth}{!}{...}` used on table | Remove resizebox; use `\setlength{\tabcolsep}{1mm}` or simplify table |

---

## 🔵 INFO (3 items) — Recommendations

| # | Check | Line | Note |
|---|-------|------|------|
| 1 | Acknowledgments | 498 | 5 sentences detected (guideline: ≤ 3). Consider condensing. |
| 2 | Reproducibility | — | `ReproducibilityChecklist.tex` not found. Verify if required by the conference. |
| 3 | File Size | — | Total source files ~2.3 MB. Ensure `.zip` is ≤ 10 MB before submission. |

---

## 🟢 PASS (22 items) — Verified Compliant

- [x] `\documentclass[letterpaper]{article}` present
- [x] `\usepackage{aaai2027}` present (camera-ready, no `submission` option)
- [x] `\usepackage[hyphens]{url}` present
- [x] `\usepackage{graphicx}` present
- [x] `\urlstyle{rm}` present
- [x] `\def\UrlFont{\rm}` present
- [x] `\usepackage{natbib}` present (no options)
- [x] `\usepackage{caption}` present (no options)
- [x] `\pdfinfo{/TemplateVersion (2027.1)}` present
- [x] No forbidden font packages (times, helvet, courier, lmodern)
- [x] No forbidden packages (geometry, titlesec, authblk, float, etc.)
- [x] No `\setlength` abuse (only tabcolsep used correctly)
- [x] Section order: Abstract → Content → Appendix → Acknowledgments → References
- [x] `\section*{Ethical Statement}` correctly unnumbered
- [x] `\section*{Acknowledgments}` correctly unnumbered
- [x] No `\input` splitting (single .tex file)
- [x] No page break commands in body
- [x] No `\pagestyle` command
- [x] No `\bibliographystyle` command (aaai2027.sty auto-sets)
- [x] All figures in .pdf/.png format
- [x] No pgfplots package
- [x] No minipage figure grouping

---

## 📊 Summary

| Severity | Count | Status |
|----------|-------|--------|
| 🔴 CRITICAL | 3 | **FAIL** |
| 🟡 WARNING | 5 | Needs attention |
| 🔵 INFO | 3 | Optional improvements |
| 🟢 PASS | 22 | Compliant |

**Overall verdict**: NOT READY for submission. Fix 3 critical issues first.
