'''
1: snake
0: gun
-1: water
'''
import random

choice = input('s for snake, g for gun, w for water:').lower()
computer = random.randint(-1,1)
l = {'s': 1, 'g': 0, 'w': -1}

val = l[choice]

if computer==-1 and val==-1:
    print('tie')
elif computer==-1 and val==0:
    print('you lose')
elif computer==-1 and val==1:
    print('you win')

if computer==1 and val==-1:
    print('you lose')
elif computer==1 and val==0:
    print('you win')
elif computer==1 and val==1:
    print('tie')

if computer==0 and val==-1:
    print('you win')
elif computer==0 and val==0:
    print('tie')
elif computer==0 and val==1:
    print('you lose')


print("thank you for playing ")