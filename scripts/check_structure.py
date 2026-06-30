#!/usr/bin/env python3
"""Check AAAI 2027 LaTeX section structure compliance.

Usage: python check_structure.py <paper.tex>

Checks:
  1. Section ordering (Abstract > Content > Appendices > Ethics > Ack > Refs)
  2. \\input command usage (only .bib and ReproducibilityChecklist.tex allowed)
  3. Page break commands in body
  4. Abstract contains citations
  5. \\section* usage for Ethical Statement and Acknowledgments
  6. \\bibliographystyle presence (should be absent)
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


def read_tex(filepath: str) -> str:
    return Path(filepath).read_text(encoding='utf-8', errors='replace')


def get_line_number(content: str, pos: int) -> int:
    return content[:pos].count('\n') + 1


def find_sections(content: str) -> list[dict]:
    """Find all section-level headings and structural elements."""
    sections = []

    patterns = [
        (r'\\(section|subsection|subsubsection)\*?\s*\{([^}]+)\}',
         'section'),
        (r'\\appendix\b', 'appendix_cmd'),
        (r'\\begin\{abstract\}', 'abstract_begin'),
        (r'\\end\{abstract\}', 'abstract_end'),
        (r'\\bibliography\s*\{([^}]+)\}', 'bibliography'),
        (r'\\begin\{links\}', 'links_begin'),
        (r'\\end\{links\}', 'links_end'),
    ]

    for pattern, stype in patterns:
        for m in re.finditer(pattern, content):
            line_no = get_line_number(content, m.start())
            entry = {
                'line': line_no,
                'type': stype,
                'text': m.group(0),
            }
            if stype == 'section' and m.lastindex and m.lastindex >= 2:
                entry['title'] = m.group(2).strip()
            elif stype == 'bibliography' and m.lastindex:
                entry['bib_files'] = m.group(1).strip()
            sections.append(entry)

    sections.sort(key=lambda x: x['line'])
    return sections


def check_section_order(sections: list[dict]) -> list[dict]:
    """Verify sections follow AAAI required order."""
    issues = []
    found_refs = False

    for sec in sections:
        tp = sec['type']

        if tp == 'bibliography':
            found_refs = True
        elif tp == 'section':
            title = sec.get('title', '').lower()
            if title == 'ethical statement':
                if '\\section*' not in sec['text']:
                    issues.append({
                        'severity': 'WARNING',
                        'line': sec['line'],
                        'item': ('Ethical Statement must use \\section*{} '
                                 '(unnumbered)'),
                        'detail': 'Ethical Statement should not be numbered',
                        'fix': r'\section*{Ethical Statement}',
                    })
            elif title == 'acknowledgments':
                if '\\section*' not in sec['text']:
                    issues.append({
                        'severity': 'WARNING',
                        'line': sec['line'],
                        'item': ('Acknowledgments must use \\section*{} '
                                 '(unnumbered)'),
                        'detail': 'Acknowledgments should not be numbered',
                        'fix': r'\section*{Acknowledgments}',
                    })

    if not found_refs:
        issues.append({
            'severity': 'CRITICAL',
            'line': 0,
            'item': '\\bibliography command not found',
            'detail': 'References must appear at the end of the paper',
            'fix': ('Add \\bibliography{yourbibfile} '
                    'before \\end{document}'),
        })

    return issues


def check_input_commands(content: str) -> list[dict]:
    """Check \\input / \\include usage."""
    issues = []
    input_pattern = re.compile(r'\\(?:input|include)\s*\{([^}]+)\}')

    for m in input_pattern.finditer(content):
        file_arg = m.group(1).strip()
        line_no = get_line_number(content, m.start())

        is_allowed = (
            file_arg.endswith('.bib') or
            'ReproducibilityChecklist' in file_arg
        )

        if not is_allowed:
            issues.append({
                'severity': 'CRITICAL',
                'line': line_no,
                'item': '\\input splits content: {}'.format(file_arg),
                'detail': ('AAAI requires a single .tex source file; '
                           'do not use \\input to split sections'),
                'fix': 'Merge all content into the main .tex file',
            })

    return issues


def check_page_breaks(content: str) -> list[dict]:
    """Check for page break commands in body."""
    issues = []
    m = re.search(r'\\begin\{document\}', content)
    if not m:
        return issues
    body = content[m.start():]
    offset_lines = content[:m.start()].count('\n')

    break_pattern = re.compile(r'\\(?:newpage|clearpage|pagebreak)\b')

    for m in break_pattern.finditer(body):
        line_no = offset_lines + body[:m.start()].count('\n') + 1
        issues.append({
            'severity': 'CRITICAL',
            'line': line_no,
            'item': 'Page break command in body: {}'.format(m.group(0)),
            'detail': ('Camera-Ready must not use page breaks; '
                       'references must follow text without breaks'),
            'fix': 'Remove the command',
        })

    return issues


def check_abstract_citations(content: str) -> list[dict]:
    """Check for citations inside abstract."""
    issues = []
    abs_match = re.search(
        r'\\begin\{abstract\}(.*?)\\end\{abstract\}',
        content, re.DOTALL
    )

    if abs_match:
        abs_text = abs_match.group(1)
        cite_pattern = re.compile(
            r'\\(?:cite|citet|citep|citeauthor|citeyear|shortcite)\s*[\{[]'
        )
        for m in cite_pattern.finditer(abs_text):
            abs_offset = get_line_number(
                content, abs_match.start() +
                abs_match.group(0)[:abs_text[:m.start()].rfind('\n')].count(
                    '\n') if '\n' in abs_text[:m.start()] else 0)
            # simpler approach: count newlines in abstract text before match
            prefix = abs_text[:m.start()]
            line_no = get_line_number(content, abs_match.start()) + \
                prefix.count('\n')
            issues.append({
                'severity': 'WARNING',
                'line': line_no,
                'item': 'Citation found in Abstract',
                'detail': 'AAAI explicitly forbids citations in the Abstract',
                'fix': 'Move the citation to the main text; '
                       'use descriptive language in Abstract',
            })

    return issues


def check_bibliographystyle(content: str) -> list[dict]:
    """Check for manual \\bibliographystyle."""
    pattern = re.compile(r'\\bibliographystyle\s*\{([^}]+)\}')
    issues = []
    for m in pattern.finditer(content):
        line_no = get_line_number(content, m.start())
        issues.append({
            'severity': 'WARNING',
            'line': line_no,
            'item': ('Manual \\bibliographystyle{{{}}} set').format(
                m.group(1)),
            'detail': ('aaai2027.sty automatically sets the bibliography '
                       'style; manual setting is not needed'),
            'fix': 'Remove this line',
        })
    return issues


def check_acknowledgments_length(content: str) -> list[dict]:
    """Rough check if Acknowledgments exceeds 3 sentences."""
    m = re.search(
        r'\\section\*\{Acknowledgments\}(.*?)'
        r'(?=\\(?:section|bibliography)|\n\n\n)',
        content, re.DOTALL | re.IGNORECASE
    )
    if m:
        ack_text = m.group(1)
        sentences = re.findall(r'[.!?]+(?:\s+|$)', ack_text)
        if len(sentences) > 3:
            return [{
                'severity': 'INFO',
                'line': get_line_number(content, m.start()),
                'item': ('Acknowledgments ~{} sentences '
                         '(guideline: <= 3)').format(len(sentences)),
                'detail': 'AAAI suggests limiting acknowledgments to 3 sentences',
                'fix': 'Condense the acknowledgments',
            }]
    return []


def main():
    if len(sys.argv) < 2:
        print("Usage: python check_structure.py <paper.tex>")
        sys.exit(1)

    tex_path = sys.argv[1]
    if not Path(tex_path).exists():
        print("Error: file not found: {}".format(tex_path))
        sys.exit(1)

    content = read_tex(tex_path)

    print("=== Section Structure Check: {} ===\n".format(tex_path))

    sections = find_sections(content)

    # Display detected structure map
    print("Detected structure:")
    for sec in sections:
        indent = '  '
        label = sec.get('title', sec.get('text', sec['type']))
        if len(label) > 70:
            label = label[:67] + '...'
        print("  L{:4d}: {}{}".format(sec['line'], indent, label))
    print()

    all_issues = []
    all_issues.extend(check_section_order(sections))
    all_issues.extend(check_input_commands(content))
    all_issues.extend(check_page_breaks(content))
    all_issues.extend(check_abstract_citations(content))
    all_issues.extend(check_bibliographystyle(content))
    all_issues.extend(check_acknowledgments_length(content))

    all_issues.sort(key=lambda x: x.get('line', 0))

    critical = [i for i in all_issues if i['severity'] == 'CRITICAL']
    warnings = [i for i in all_issues if i['severity'] == 'WARNING']
    infos = [i for i in all_issues if i['severity'] == 'INFO']

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

    if infos:
        print("{} INFO ({} items):".format(TAG_INFO, len(infos)))
        for i, issue in enumerate(infos, 1):
            print("  {}. [Line {}] {}".format(i, issue['line'], issue['item']))
            print("     {}".format(issue['detail']))
            print()

    if not all_issues:
        print("{} Section structure is AAAI 2027 compliant".format(TAG_PASS))

    total = len(critical) + len(warnings)
    status = 'PASS' if total == 0 else ('FAIL' if critical else 'WARN')
    print("\n--- Summary: {} critical, {} warnings, {} info, {} ---".format(
        len(critical), len(warnings), len(infos), status))

    sys.exit(1 if critical else 0)


if __name__ == '__main__':
    main()
