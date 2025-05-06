# vibe/build.py

from .lexer import tokenize
from .parser import parse
from .codegen import generate_html

def build(filepath):
    with open(filepath, 'r') as f:
        code = f.read()
    tokens = tokenize(code)
    ast = parse(tokens)
    html = generate_html(ast)
    with open('dist/index.html', 'w') as f:
        f.write(html)
    print("✅ Build complete! Output: dist/index.html")
