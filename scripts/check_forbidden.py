#!/usr/bin/env python3
"""Scan LaTeX file for AAAI 2027 forbidden packages and commands.

Usage: python check_forbidden.py <paper.tex>

Checks:
  1. Forbidden \\usepackage entries
  2. Forbidden commands (\\baselinestretch, \\clearpage, \\tiny, etc.)
  3. Negative vspace/vskip near figures/tables/sections
  4. \\setlength usage (only \\tabcolsep allowed)
"""

import re
import sys
from pathlib import Path

# Fix Unicode emoji output on Windows GBK terminals
if sys.platform == 'win32':
    try:
        sys.stdout.reconfigure(encoding='utf-8')
    except Exception:
        pass

TAG_CRITICAL = '[CRITICAL]'
TAG_WARNING = '[WARNING]'
TAG_INFO = '[INFO]'
TAG_PASS = '[PASS]'

# -- Forbidden packages -------------------------------------------------------

FORBIDDEN_PACKAGES = [
    'authblk', 'babel', 'balance', 'cjk', 'epsf', 'epsfig', 'euler',
    'float', 'flushend', 'fullpage', 'geometry', 'graphics', 'hyperref',
    'indentfirst', 'layout', 'lmodern', 'multicol', 'nameref', 'navigator',
    'pdfcomment', 'pgfplots', 'psfig', 'pstricks', 'savetrees', 'setspace',
    'stfloats', 't1enc', 'tabu', 'times', 'titlesec', 'tocbibind', 'ulem',
    'wrapfig',
]

# -- Forbidden commands (regex patterns) ---------------------------------------
# Each: (pattern, command_name, description, exception_note_or_None)

# Commands that are ALWAYS forbidden (even in comments they shouldn't exist
# in a real paper, but we skip comments to avoid matching template instructions).
# Layout params like \textwidth, \columnsep, \topmargin are NOT listed here
# because they can appear legitimately as length references (e.g.
# \includegraphics[width=0.8\textwidth]{...}). Their MODIFICATION is caught
# by check_setlength_abuse() instead.

FORBIDDEN_COMMANDS = [
    # Page control
    (r'\\clearpage\b', '\\clearpage', 'no page breaks allowed', None),
    (r'\\newpage\b', '\\newpage', 'no page breaks allowed', None),
    (r'\\pagebreak\b', '\\pagebreak', 'no page breaks allowed', None),
    (r'\\pagestyle\b', '\\pagestyle', 'no page numbers/headers/footers', None),

    # Spacing modifications (these always modify, never just reference)
    (r'\\baselinestretch\b', '\\baselinestretch',
     'no line spacing modifications', None),
    (r'\\linespread\b', '\\linespread',
     'no line spacing modifications', None),
    (r'\\abovecaption\b', '\\abovecaption',
     'no caption spacing modifications', None),
    (r'\\belowcaption\b', '\\belowcaption',
     'no caption spacing modifications', None),
    (r'\\abovedisplay\b', '\\abovedisplay',
     'no math display spacing modifications', None),
    (r'\\belowdisplay\b', '\\belowdisplay',
     'no math display spacing modifications', None),
    (r'\\addtolength\b', '\\addtolength',
     'no LaTeX length modifications', None),
    (r'\\topskip\b', '\\topskip',
     'no page layout modifications', None),

    # Font size
    (r'\\tiny\b', '\\tiny', 'font size too small, not acceptable', None),

    # Float manipulation
    (r'\\float\b', '\\float', 'no float behavior changes', None),

    # Graphics -- but only when used as commands, not in comments
    (r'clip\s*=\s*true', 'clip=true',
     'no in-LaTeX cropping -- crop externally',
     'Crop figures in graphics software before including'),
    (r'\\trim\b', '\\trim',
     'no in-LaTeX trimming -- crop externally',
     'Crop figures in graphics software before including'),

    # Other forbidden
    (r'\\nocopyright\b', '\\nocopyright',
     'disabling copyright notice -- paper will not be published', None),
    (r'\\pubnote\b', '\\pubnote', 'command not allowed', None),
    (r'\\balance\b', '\\balance', 'command not allowed', None),
    (r'\\resizebox\b', '\\resizebox',
     'no table resizing (uncontrolled font size)',
     'Use \\setlength{\\tabcolsep}{1mm} or simplify table content'),

    # Page layout commands (only when used as layout modifications)
    (r'\\oddsidemargin\b', '\\oddsidemargin',
     'no page layout modifications', None),
    (r'\\evensidemargin\b', '\\evensidemargin',
     'no page layout modifications', None),
    (r'\\parindent\b', '\\parindent',
     'no paragraph indent modifications', None),
    (r'\\parskip\b', '\\parskip',
     'no paragraph spacing modifications', None),
]


def read_tex(filepath: str) -> str:
    return Path(filepath).read_text(encoding='utf-8', errors='replace')


def strip_latex_comments(content: str) -> str:
    """Remove LaTeX comments (lines starting with %% not preceded by backslash).
    Keeps the newline structure so line numbers stay correct."""
    lines = content.split('\n')
    result = []
    for line in lines:
        stripped = line.strip()
        # If the line is a comment (starts with %, not \%)
        if stripped.startswith('%') and not stripped.startswith('\\%'):
            result.append('')  # Keep empty line for line number alignment
        else:
            result.append(line)
    return '\n'.join(result)


def get_line_number(content: str, pos: int) -> int:
    return content[:pos].count('\n') + 1


def check_forbidden_packages(content: str) -> list[dict]:
    issues = []
    for pkg in FORBIDDEN_PACKAGES:
        # Build pattern: \usepackage[opts]{pkg}
        pattern = r'\\usepackage(\[.*?\])?\s*\{{pkg_name\}}'.format(
            pkg_name=pkg)
        for m in re.finditer(pattern, content):
            line_no = get_line_number(content, m.start())
            issues.append({
                'severity': 'CRITICAL',
                'line': line_no,
                'item': 'Forbidden package: \\usepackage{{{}}}'.format(pkg),
                'detail': '{} is incompatible with aaai2027.sty'.format(pkg),
                'fix': 'Remove the line and all dependencies on {}'.format(pkg),
            })
    return issues


def check_forbidden_commands(content: str) -> list[dict]:
    issues = []
    seen = set()

    for pattern, cmd_name, desc, exception_note in FORBIDDEN_COMMANDS:
        for m in re.finditer(pattern, content):
            line_no = get_line_number(content, m.start())
            key = (line_no, cmd_name)
            if key in seen:
                continue
            seen.add(key)

            detail = desc
            if exception_note:
                detail += ' (alternative: {})'.format(exception_note)

            issues.append({
                'severity': 'CRITICAL',
                'line': line_no,
                'item': 'Forbidden command: {}'.format(cmd_name),
                'detail': detail,
                'fix': 'Remove the command' if not exception_note
                       else exception_note,
            })
    return issues


def check_setlength_abuse(content: str) -> list[dict]:
    issues = []
    # Match \setlength{target}{value}
    pattern = re.compile(r'\\setlength\s*\{([^}]+)\}')
    tabcolsep_ok = re.compile(r'\\setlength\s*\{\s*\\tabcolsep\s*\}')

    for m in pattern.finditer(content):
        if tabcolsep_ok.search(m.group(0)):
            continue
        line_no = get_line_number(content, m.start())
        target = m.group(1).strip()
        issues.append({
            'severity': 'CRITICAL',
            'line': line_no,
            'item': '\\setlength used on {} (only \\tabcolsep allowed)'.format(
                target),
            'detail': ('\\setlength is forbidden; '
                       '\\setlength{\\tabcolsep} is the only exception'),
            'fix': 'Remove this line',
        })
    return issues


def check_negative_vspace_near_float(content: str) -> list[dict]:
    issues = []
    lines = content.split('\n')

    neg_pattern = re.compile(
        r'(\\vspace\s*\{-\s*[^}]+\}|\\vskip\s*-\s*[^\n%]+)')

    float_starts = re.compile(
        r'\\(?:section|subsection|subsubsection|caption|'
        r'begin\s*\{(?:figure|table|algorithm|listing)\})')

    for m in neg_pattern.finditer(content):
        line_no = get_line_number(content, m.start())
        # Check context: within 10 lines of a float/section/caption
        ctx_start = max(0, line_no - 10)
        ctx_end = min(len(lines), line_no + 10)
        context_text = '\n'.join(lines[ctx_start:ctx_end])

        if float_starts.search(context_text):
            issues.append({
                'severity': 'CRITICAL',
                'line': line_no,
                'item': ('Negative spacing near float/section: '
                         '{}').format(m.group(0)[:60]),
                'detail': ('Negative vspace/vskip is STRICTLY forbidden near '
                           'figures, tables, captions, sections, subsections, '
                           'subsubsections, or references'),
                'fix': 'Remove the negative spacing command',
            })
        else:
            issues.append({
                'severity': 'WARNING',
                'line': line_no,
                'item': 'Negative spacing used: {}'.format(m.group(0)[:60]),
                'detail': ('Negative vspace/vskip is discouraged; '
                           'strictly forbidden near floats/headings'),
                'fix': 'Consider removing or using positive spacing instead',
            })

    return issues


def main():
    if len(sys.argv) < 2:
        print("Usage: python check_forbidden.py <paper.tex>")
        sys.exit(1)

    tex_path = sys.argv[1]
    if not Path(tex_path).exists():
        print("Error: file not found: {}".format(tex_path))
        sys.exit(1)

    content = read_tex(tex_path)
    # Strip LaTeX comments to avoid false positives from template instructions
    scanned = strip_latex_comments(content)

    print("=== Forbidden Content Scan: {} ===\n".format(tex_path))

    all_issues = []
    all_issues.extend(check_forbidden_packages(scanned))
    all_issues.extend(check_forbidden_commands(scanned))
    all_issues.extend(check_setlength_abuse(scanned))
    all_issues.extend(check_negative_vspace_near_float(scanned))

    all_issues.sort(key=lambda x: x.get('line', 0))

    critical = [i for i in all_issues if i['severity'] == 'CRITICAL']
    warnings = [i for i in all_issues if i['severity'] == 'WARNING']

    if critical:
        print("{} CRITICAL ({} issues):".format(TAG_CRITICAL, len(critical)))
        for i, issue in enumerate(critical, 1):
            print("  {}. [Line {}] {}".format(i, issue['line'], issue['item']))
            print("     {}".format(issue['detail']))
            print("     Fix: {}".format(issue['fix']))
            print()

    if warnings:
        print("{} WARNING ({} issues):".format(TAG_WARNING, len(warnings)))
        for i, issue in enumerate(warnings, 1):
            print("  {}. [Line {}] {}".format(i, issue['line'], issue['item']))
            print("     {}".format(issue['detail']))
            print("     Fix: {}".format(issue['fix']))
            print()

    if not all_issues:
        print("{} No forbidden packages or commands found".format(TAG_PASS))

    total = len(critical) + len(warnings)
    status = 'PASS' if total == 0 else ('FAIL' if critical else 'WARN')
    print("\n--- Summary: {} critical, {} warnings, {} ---".format(
        len(critical), len(warnings), status))

    sys.exit(1 if critical else 0)


if __name__ == '__main__':
    main()
