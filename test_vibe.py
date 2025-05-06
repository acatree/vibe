from vibe.lexer import Lexer

print("Testing Vibe...")
lexer = Lexer()
test_code = '''
Page {
    Section: "Welcome"
    Section: "About"
}
'''

result = lexer.tokenize(test_code)
print(result)
