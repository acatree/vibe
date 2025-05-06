
from .lexer import Lexer
from .parser import parse
from .codegen import generate_html

def build(filepath):
    """Process the Vibe file."""
    with open(filepath, 'r') as file:
        code = file.read()

    # Tokenize the code
    lexer = Lexer()
    tokens = lexer.tokenize(code)
    print("Tokens:", tokens)

    # Parse the tokens into an AST
    ast = parse(tokens)

    # Generate HTML from the AST
    html = generate_html(ast)

    # Write the output HTML to the dist folder
    with open('dist/index.html', 'w') as f:
        f.write(html)

    print("✅ Build complete! Output: dist/index.html")
