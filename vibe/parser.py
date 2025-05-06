# vibe/parser.py

def parse(tokens):
    tokens = list(tokens)
    pos = 0
    ast = {}

    def expect(expected_type, pos):
        if pos >= len(tokens):
            raise SyntaxError(f"Expected {expected_type} but got {tok_type}")
        tok_type, tok_val = tokens[pos]
        if tok_type != expected_type:
            raise SyntaxError(f"Expected {expected_type}, but got end of input")
        return tok_val, pos + 1

    def parse_section(pos):
        _, pos = expect('SECTION', pos)
        title, pos = expect('STRING', pos)
        _, pos = expect('LBRACE', pos)
        content = {}
        while tokens[pos][0] != 'RBRACE':
            key, pos = expect('STRING', pos)
            _, pos = expect('COLON', pos)
            val_type, val = tokens[pos]
            if val_type == 'STRING':
                content[key] = val
                pos += 1
            elif val_type == 'LIST':
                content[key] = eval(val)
                pos += 1
            elif val_type == 'STRING' and tokens[pos + 1][0] == 'ARROW':
                label = val
                pos += 2  # skip STRING + ARROW
                link, pos = expect('STRING', pos)
                content[key] = {'label': label, 'link': link}
            else:
                raise SyntaxError(f"Unexpected token {val_type}")
        _, pos = expect('RBRACE', pos)
        return {'title': title, 'content': content}, pos

    # Start parsing the page
    _, pos = expect('PAGE', pos)
    page_title, pos = expect('STRING', pos)
    _, pos = expect('LBRACE', pos)
    sections = []
    while pos < len(tokens) and tokens[pos][0] != 'RBRACE':
        section, pos = parse_section(pos)
        sections.append(section)
    _, pos = expect('RBRACE', pos)

    ast['Page'] = {'title': page_title, 'sections': sections}
    return ast
