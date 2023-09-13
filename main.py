import time, os

def prettyPrint(word, color):
  if color == 'black':
    print(f'\033[30m{word}\033[0m', end=' ', sep='')
  elif color == 'red':
    print(f'\033[31m{word}\033[0m', end=' ', sep='')
  elif color == 'green':
    print(f'\033[32m{word}\033[0m', end=' ', sep='')
  elif color == 'brown':
    print(f'\033[33m{word}\033[0m', end=' ', sep='')
  elif color == 'yellow':                                               print(f'\033[1;33m{word}\033[0m', end=' ', sep='')
  elif color == 'blue':
    print(f'\033[34m{word}\033[0m', end=' ', sep='')
  elif color == 'purple':
    print(f'\033[35m{word}\033[0m', end=' ', sep='')
  elif color == 'cyan':
    print(f'\033[36m{word}\033[0m', end=' ', sep='')
  elif color == 'gray':
    print(f'\033[37m{word}\033[0m', end=' ', sep='')
  elif color == 'normal':
    print(f'\033[0m{word}\033[0m', end=' ', sep='')


list1 = []
colors = ['red', 'green', 'yellow', 'blue', 'purple', 'cyan', 'normal', 'gray']

while True:
  time.sleep(1)
  ask1 = input('\033[1mWrite your word or text here: ')
  time.sleep(1)
  ask2 = input('\033[5mEnter the color here: \033[0m')
  print()
  while ask2 not in colors:
    print('\033[1;31mPlease select a color from the available colors: red, green, yellow, blue, purple, cyan, normal, gray.\033[0m')
    print()
    ask2 = input('\033[5mEnter the color here: \033[0m')
    print()
  list = [ask1, ask2]
  list1.append(list)
  request = input('Want to write more? y/n: ')
  print()
  if request != 'y':
    break
    
os.system('clear')
print('\033[1;33mSuper Subroutine\033[0m')
print()
for a in list1:
  time.sleep(2)
  prettyPrint(a[0], a[1])
print('\033[?25l', end='')
  