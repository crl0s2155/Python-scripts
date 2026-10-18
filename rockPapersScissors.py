print('Rock Paper scissors')

print('1)👊🏽')
print('2)👋🏽')
print('3)✌🏽')

import random
cpu = random.randint(1, 3)

r = 1
p = 2
s = 3



player = int(input('Enter choice: '))

if player == r and cpu == r:
  print('tie, play again')
elif player == p and cpu == p:
  print('tie, play again')
elif player == s and cpu == s:
  print('tie, play again')
elif player == r and cpu == p:
  print('you lose')
elif player == r and cpu == s:
  print('you win')
elif player == p and cpu == r:
  print('you win')
elif player == p and cpu == s:
  print('you lose')
elif player == s and cpu == r:
  print('you lose')
elif player == s and cpu == p:
  print('you win')
else:
  print('error try again')

print('you chose:') , print(player)
print('cpu chose:') , print(cpu)
