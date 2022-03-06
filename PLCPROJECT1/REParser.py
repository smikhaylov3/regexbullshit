import ply.yacc as yacc
from RENode import RENode
from RELexer import tokens

count = 0

def increment():
  global count
  count = count + 1
  
def reset():
  global count
  count = 0

def p_reStart(p):
    'reStart : re SEMI'
    p[0] = p[1]
    reset()

def p_re_1(p):
  're : term'
  print('THIS IS TERM')
  p[0] = p[1]

def p_re_2(p):
  're : re PLUS term'
  n = RENode()
  n._operator = '+'
  n._lchild = p[1]
  n._rchild = p[3]
  p[0] = n
  n._nullable = ((n._lchild)._nullable) or ((n._rchild)._nullable)
  n._firstpos = ((n._lchild)._firstpos).union((n._rchild)._firstpos)
  n._lastpos = ((n._lchild)._lastpos).union((n._rchild)._lastpos)


def p_term_1(p):
  'term : factor'
  print('THIS IS FACTOR')
  p[0] = p[1]

def p_term_2(p):
  'term : term factor'
  n = RENode()
  n._operator = '.'
  n._lchild = p[1]
  n._rchild = p[2]
  p[0] = n
  n._nullable = (n._lchild)._nullable and (n._rchild)._nullable
  print(n._nullable)
  if ((n._lchild)._nullable == True):
    print('WE WILL MAKE A UNION')
    n._firstpos = ((n._lchild)._firstpos).union((n._rchild)._firstpos)
  else:
    print('WE WILL NOT MAKE A UNION')
    n._firstpos = (n._lchild)._firstpos
  if ((n._rchild)._nullable == True):
    print('WE WILL MAKE A UNION')
    n._lastpos = ((n._lchild)._lastpos).union((n._rchild)._lastpos)
  else:
    print('WE WILL NOT MAKE A UNION')
    n._lastpos = (n._lchild)._lastpos
  
    


def p_factor_1(p):
  'factor : niggle'
  p[0] = p[1]

def p_factor_2(p):
  'factor : factor STAR'
  n = RENode()
  n._operator = '*'
  n._lchild = p[1]
  p[0] = n
  n._nullable = True
  n._firstpos = (n._lchild)._firstpos
  n._lastpos = (n._lchild)._lastpos
 
def p_niggle_1(p):
  'niggle : LETTER'
  n = RENode()
  n._operator = 'leaf'
  p[0] = n
  n._symbol = p[1]
  increment()
  n._position = count
  print('THE NODE ' + str(n._symbol) + ' IS AT POSITION: ' + str(n._position))
  #print(n._position)
  n._nullable = False;
  n._firstpos.add(n._position)
  n._lastpos.add(n._position)



def p_niggle_2(p):
  'niggle : EPSILON'
  n = RENode()
  n._operator = 'leaf'
  p[0] = n
  n._symbol = p[1]
  n._nullable = True;
 
def p_niggle_3(p):
  'niggle : LPAREN re RPAREN'
  p[0] = p[2]

def p_error(p):
  print("Syntax error in input!")

parser = yacc.yacc()

