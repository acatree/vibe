# vibe/parser.py

def parse(tokens):
    tokens = list(tokens)
    pos = 0
    ast = {}

    def expect(expected_type):
        nonlocal pos
        if pos >= len(tokens):
            raise SyntaxError(f"Expected {expected_type} but got EOF")
        tok_type, tok_val = tokens[pos]
        if tok_type != expected_type:
            raise SyntaxError(f"Expected {expected_type} but got {tok_type}")
        pos += 1
        return tok_val

    def parse_section():
        expect('SECTION')
        title = expect('STRING')
        expect('LBRACE')
        content = {}
        while tokens[pos][0] != 'RBRACE':
            key = expect('STRING')
            expect('COLON')
            val_type, val = tokens[pos]
            if val_type == 'STRING':
                pos += 1
                content[key] = val
            elif val_type == 'LIST':
                pos += 1
                content[key] = eval(val)
            elif val_type == 'STRING' and tokens[pos + 1][0] == 'ARROW':
                label = val
                pos += 2  # skip STRING + ARROW
                link = expect('STRING')
                content[key] = {'label': label, 'link': link}
            else:
                raise SyntaxError(f"Unexpected token {tokens[pos]}")
        expect('RBRACE')
        return {'title': title, 'content': content}

    expect('PAGE')
    page_title = expect('STRING')
    expect('LBRACE')
    sections = []
    while pos < len(tokens) and tokens[pos][0] != 'RBRACE':
        sections.append(parse_section())
    expect('RBRACE')

    ast['Page'] = {'title': page_title, 'sections': sections}
    return ast
