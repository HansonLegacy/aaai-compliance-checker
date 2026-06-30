#!/usr/bin/env python3
"""Check AAAI 2027 LaTeX preamble compliance.

Usage: python check_preamble.py <paper.tex>

Checks:
  1. Required preamble lines exist
  2. Forbidden font packages absent
  3. natbib/caption have no options
  4. secnumdepth value valid (0/1/2)
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

# Tag constants (avoid inline emoji strings that confuse encodings)
TAG_CRITICAL = '[CRITICAL]'
TAG_WARNING = '[WARNING]'
TAG_INFO = '[INFO]'
TAG_PASS = '[PASS]'


# -- Required lines -----------------------------------------------------------
# Each tuple: (regex_pattern, human_readable, description)
# NOTE: In Python 3.12+ re, \\u in pattern = literal \u (not Unicode escape).
# Always use \\\\ before letters that might be interpreted as regex escapes.

REQUIRED_LINES = [
    (r'\\documentclass\[letterpaper\]\{article\}',
     r'\documentclass[letterpaper]{article}',
     'Preamble line 1, fix paper size to US Letter'),
    (r'\\usepackage(\[submission\])?\{aaai2027\}',
     r'\usepackage{aaai2027} or \usepackage[submission]{aaai2027}',
     'Load AAAI 2027 style file'),
    (r'\\usepackage\[hyphens\]\{url\}',
     r'\usepackage[hyphens]{url}',
     'URL line-breaking support'),
    (r'\\usepackage\{graphicx\}',
     r'\usepackage{graphicx}',
     'Graphics inclusion'),
    (r'\\urlstyle\{rm\}',
     r'\urlstyle{rm}',
     'URLs in Roman font'),
    (r'\\def\\UrlFont\{\\rm\}',
     r'\def\UrlFont{\rm}',
     'URL font definition as Roman'),
    (r'\\usepackage\{natbib\}',
     r'\usepackage{natbib} (must have NO options)',
     'Bibliography management'),
    (r'\\usepackage\{caption\}',
     r'\usepackage{caption} (must have NO options)',
     'Figure/table captions'),
    (r'\\frenchspacing',
     r'\frenchspacing',
     'No extra space after periods'),
    (r'\\pdfinfo\s*\{.*TemplateVersion.*\(2027\.1\)',
     r'\pdfinfo{/TemplateVersion (2027.1)}',
     'Template version metadata'),
]

# -- Forbidden font packages --------------------------------------------------

FORBIDDEN_FONT_PKGS = [
    'times', 'helvet', 'courier', 'lmodern', 't1enc', 'mathptmx',
    'newtxtext', 'newtxmath', 'fontenc', 'fontspec', 'mathpazo',
    'pxfonts', 'txfonts', 'fourier', 'arev', 'venturis',
]

# -- Recommended but optional packages ----------------------------------------

OPTIONAL_PKGS = {
    'algorithm': 'algorithm pseudocode',
    'algorithmic': 'algorithm pseudocode (paired with algorithm)',
    'newfloat': 'code listing floats',
    'listings': 'code listing typesetting',
    'booktabs': 'professional table rules',
}


def read_tex(filepath: str) -> str:
    return Path(filepath).read_text(encoding='utf-8', errors='replace')


def extract_preamble(content: str) -> str:
    m = re.search(r'\\begin\{document\}', content)
    if not m:
        return content
    return content[:m.start()]


def check_required_lines(preamble: str) -> list[dict]:
    issues = []
    for pattern, expected, description in REQUIRED_LINES:
        if not re.search(pattern, preamble, re.DOTALL):
            issues.append({
                'severity': 'CRITICAL',
                'item': 'Missing required preamble line',
                'detail': description,
                'expected': expected,
            })
    return issues


def check_forbidden_font_pkgs(preamble: str) -> list[dict]:
    issues = []
    for pkg in FORBIDDEN_FONT_PKGS:
        # Build pattern safely with .format()
        pattern = r'\\usepackage(\[.*?\])?\s*\{{pkg_name\}}'.format(
            pkg_name=pkg)
        for m in re.finditer(pattern, preamble):
            issues.append({
                'severity': 'CRITICAL',
                'item': 'Forbidden font package: \\usepackage{{{}}}'.format(pkg),
                'detail': ('aaai2027.sty auto-loads newtxtext/helvet/courier; '
                           'extra font packages cause conflicts'),
                'fix': 'Remove \\usepackage{{{}}}'.format(pkg),
            })
    return issues


def check_natbib_caption_options(preamble: str) -> list[dict]:
    issues = []
    # natbib with options
    m = re.search(r'\\usepackage(\[.*?\])\s*\{natbib\}', preamble)
    if m:
        issues.append({
            'severity': 'CRITICAL',
            'item': '\\usepackage{natbib} has options: {}'.format(m.group(1)),
            'detail': 'natbib must not have any options',
            'fix': 'Change to \\usepackage{natbib}',
        })
    # caption with options
    m = re.search(r'\\usepackage(\[.*?\])\s*\{caption\}', preamble)
    if m:
        issues.append({
            'severity': 'CRITICAL',
            'item': '\\usepackage{caption} has options: {}'.format(m.group(1)),
            'detail': 'caption must not have any options',
            'fix': 'Change to \\usepackage{caption}',
        })
    return issues


def check_secnumdepth(preamble: str) -> list[dict]:
    m = re.search(r'\\setcounter\{secnumdepth\}\{(\d)\}', preamble)
    if m:
        val = int(m.group(1))
        if val > 2:
            return [{
                'severity': 'WARNING',
                'item': 'secnumdepth = {} (> 2)'.format(val),
                'detail': ('aaai2027.sty does not support subsubsection '
                           'numbering; secnumdepth max is 2'),
                'fix': 'Change to \\setcounter{secnumdepth}{2} or lower',
            }]
    return []


def check_documentclass_letterpaper(preamble: str) -> list[dict]:
    m = re.search(r'\\documentclass(?:\[(.*?)\])?\{(.*?)\}', preamble)
    if m:
        options = m.group(1) or ''
        doc_class = m.group(2) or ''
        if 'letterpaper' not in options:
            return [{
                'severity': 'CRITICAL',
                'item': 'documentclass missing letterpaper option',
                'detail': 'AAAI requires US Letter paper size',
                'fix': r'\documentclass[letterpaper]{article}',
            }]
        if doc_class != 'article':
            return [{
                'severity': 'CRITICAL',
                'item': 'documentclass is {} instead of article'.format(
                    doc_class),
                'detail': 'AAAI requires the article document class',
                'fix': r'\documentclass[letterpaper]{article}',
            }]
    return []


def check_for_additional_font_cmds(preamble: str) -> list[dict]:
    issues = []
    suspicious = [
        (r'\\renewcommand\{\\familydefault\}', 'modifies default font family'),
        (r'\\renewcommand\{\\rmdefault\}', 'modifies serif font'),
        (r'\\renewcommand\{\\sfdefault\}', 'modifies sans-serif font'),
        (r'\\renewcommand\{\\ttdefault\}', 'modifies monospace font'),
    ]
    for pattern, desc in suspicious:
        if re.search(pattern, preamble):
            issues.append({
                'severity': 'CRITICAL',
                'item': 'Font modification found in preamble: {}'.format(desc),
                'detail': ('Do not modify fonts set by aaai2027.sty'),
                'fix': 'Remove the command',
            })
    return issues


def main():
    if len(sys.argv) < 2:
        print("Usage: python check_preamble.py <paper.tex>")
        sys.exit(1)

    tex_path = sys.argv[1]
    if not Path(tex_path).exists():
        print("Error: file not found: {}".format(tex_path))
        sys.exit(1)

    content = read_tex(tex_path)
    preamble = extract_preamble(content)

    print("=== Preamble Compliance Check: {} ===\n".format(tex_path))
    print("Preamble length: {} characters\n".format(len(preamble)))

    all_issues = []
    all_issues.extend(check_required_lines(preamble))
    all_issues.extend(check_forbidden_font_pkgs(preamble))
    all_issues.extend(check_natbib_caption_options(preamble))
    all_issues.extend(check_secnumdepth(preamble))
    all_issues.extend(check_documentclass_letterpaper(preamble))
    all_issues.extend(check_for_additional_font_cmds(preamble))

    critical = [i for i in all_issues if i['severity'] == 'CRITICAL']
    warnings = [i for i in all_issues if i['severity'] == 'WARNING']

    if critical:
        print("{} CRITICAL ({} issues):".format(TAG_CRITICAL, len(critical)))
        for i, issue in enumerate(critical, 1):
            print("  {}. {}".format(i, issue['item']))
            print("     Detail: {}".format(issue['detail']))
            print("     Fix: {}".format(
                issue.get('fix', issue.get('expected', ''))))
            print()

    if warnings:
        print("{} WARNING ({} issues):".format(TAG_WARNING, len(warnings)))
        for i, issue in enumerate(warnings, 1):
            print("  {}. {}".format(i, issue['item']))
            print("     Detail: {}".format(issue['detail']))
            if 'fix' in issue:
                print("     Fix: {}".format(issue['fix']))
            print()

    if not all_issues:
        print("{} Preamble is AAAI 2027 compliant".format(TAG_PASS))

    # Check for optional recommended packages
    found_optional = []
    for pkg, desc in OPTIONAL_PKGS.items():
        pattern = r'\\usepackage(\[.*?\])?\s*\{{pkg_name\}}'.format(
            pkg_name=pkg)
        if re.search(pattern, preamble):
            found_optional.append('{} ({})'.format(pkg, desc))
    if found_optional:
        print("\n{} Detected recommended packages: {}".format(
            TAG_INFO, ', '.join(found_optional)))

    total = len(critical) + len(warnings)
    status = 'PASS' if total == 0 else ('FAIL' if critical else 'WARN')
    print("\n--- Summary: {} critical, {} warnings, {} ---".format(
        len(critical), len(warnings), status))

    sys.exit(1 if critical else 0)


if __name__ == '__main__':
    main()
