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

class Lexer:
    def __init__(self):
        self.token_regex = '|'.join(f'(?P<{name}>{pattern})' for name, pattern in TOKEN_SPEC)

    def tokenize(self, code):
        tokens = []
        for mo in re.finditer(self.token_regex, code):
            kind = mo.lastgroup
            value = mo.group()
            if kind in ('SKIP', 'NEWLINE'):
                continue
            tokens.append((kind, value))
        return tokens
