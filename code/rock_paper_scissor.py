import time
import random
print('''
How to play->
Press
'r' for rock
'p' for paper
'c' for scissor

''')
cont = input("Press any key to continue")
if cont:
    print("countdown starts now")
    for n in range(1, 4):
        time.sleep(1)
        print(n)

    time.sleep(1)
    print("Go\n")
    hand = input()
    comp = random.randint(1, 4)
    if hand == 'r':
        if comp == 1:
            print("Tie")
        elif comp == 2:
            print(" computer won")
        elif comp == 3:
            print(" You won")
        else:
            print("invalid game")

    if hand == 'p':
        if comp == 1:
            print("You won")
        elif comp == 2:
            print("tie")
        elif comp == 3:
            print(" computer won")
        else:
            print("invalid game")

    if hand == 's':
        if comp == 1:
            print("computer won")
        elif comp == 2:
            print(" You won")
        elif comp == 3:
            print("Tie")
        else:
            print("invalid game")
