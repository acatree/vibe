# vibe/lexer.py
import re

TOKEN_SPEC = [
    ('PAGE', r'Page'),
    ('SECTION', r'Section'),
    ('LBRACE', r'\{'),
    ('RBRACE', r'\}'),
    ('COLON', r':'),
    ('ARROW', r'->'),
    ('STRING', r'"[^"]*"'),
    ('LIST', r'.*?'),
    ('NEWLINE', r'\n'),
    ('SKIP', r'[ \t]+'),
]

token_regex = '|'.join('(?P<%s>%s)' % pair for pair in TOKEN_SPEC)

def tokenize(code):
    for mo in re.finditer(token_regex, code):
        kind = mo.lastgroup
        value = mo.group()
        if kind == 'SKIP' or kind == 'NEWLINE':
            continue
        yield (kind, value.strip('"'))
