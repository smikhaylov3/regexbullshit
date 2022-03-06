from REParser import parser
from RENode import RENode

def eval_expression(tree):
  print('TIME TO EVALUATE THE TREE')
  print('********')
  
def read_input():
  result = ''
  while True:
    data = input('INPUT STRING: ').strip() 
    if ';' in data:
      i = data.index(';')
      result += data[0:i+1]
      break
    else:
      result += data + ' '
  return result

def main():
  while True:
    data = read_input()
    print('*************')
    print('THIS IS THE DATA')
    print(data)
    print('*************')

    if data == 'exit;':
      break
    try:
      tree = parser.parse(data)
    except Exception as inst:
      print(inst.args[0])
      continue
    print(tree)
    try:
      answer = eval_expression(tree)
      if isinstance(answer,str):
        print('\nEVALUATION ERROR: '+answer+'\n')
      else:
        pass
       # print('\nThe value is '+str(answer)+'\n')
    except Exception as inst:
      print(inst.args[0])
 
main()
