import ply.lex as lex

reserved = {}


tokens = ['LPAREN', 'RPAREN', 'LETTER', 'STAR', 'EPSILON', 'SEMI', 'PLUS'] + \
  list(reserved.values())

t_LPAREN = r'\('
t_RPAREN = r'\)'
t_SEMI = r';'
t_PLUS = r'\+'
t_STAR = r'\*'
t_LETTER =  r'[a-zA-Z0-9]'
t_EPSILON = r'\^'

# Ignored characters
t_ignore = " \r\n\t"

#t_ignore_COMMENT = r'\#.*'

def t_error(t):
  print("Illegal character '%s'" % t.value[0])
  #t.lexer.skip(1)
  raise Exception('LEXER ERROR')

lexer = lex.lex()
## Test it out
data = '''
(a+^)(b+bb*);
'''
#
## Give the lexer some input
print("Tokenizing: ",data)
lexer.input(data)
#
## Tokenize
while True:
    tok = lexer.token()
    if not tok:
        break      # No more input
    print(tok)
