import random

c = 'y'
while c == 'y':
    num1 = random.randint(1, 1000)
    num2 = random.randint(1, 1000)
    op = random.choice(['-', '+'])
    print(num1, op, num2, '= ?')
    answer = int(input("Your answer = \n"))
    if op == '+':
        if answer == num1 + num2:
            print("right answer")
        else:
            print("wrong answer")

    if op == '-':
        if answer == num1 - num2:
            print("right answer")
        else:
            print("wrong answer")

    c = input("Do you want to continue?\nPress 'y' for yes, else 'n' for no\n")
