import time
import random
print('''
How to play->
Press in 2 seconds
'r' for rock
'p' for paper
'c' for scissor
on Go after countdown stops

''')
cont = input("Press 'y' to start countdown and play")
if cont == 'y':
    print("countdown starts now")
    for n in range(1, 4):
        time.sleep(1)
        print(n)

    time.sleep(1)
    print("Go\n")
    hand = input()
    comp = random.choice(['r', 'p', 's'])
    if hand == comp:
        print("oh! It's a tie")
    elif hand == 'p' and comp == 's':
        print("Oops! You lost")
    elif hand == 'p' and comp == 'r':
        print("Yay! You won")
    elif hand == 'r' and comp == 'p':
        print("Oops! You lost")
    elif hand == 'r' and comp == 's':
        print("Yay! You won")
    elif hand == 's' and comp == 'r':
        print("Oops! You lost")
    elif hand == 's' and comp == 'p':
        print("Yay! You won")
    else:
        print("You better play by rules")