def add_fun(a, b):
    return a + b


def sub_fun(a, b):
    return a - b


def mul_fun(a, b):
    return a * b


def div_fun(a, b):
    return a / b


while True:
    choice = int(input('''
    Press 1 for addition
    Press 2 for subtraction
    Press 3 for multiplication
    Press 4 for division
    ''')
             )
    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))
    if choice == 1:
        print(add_fun(num1, num2))
    elif choice == 2:
        print(sub_fun(num1, num2))
    elif choice == 3:
        print(mul_fun(num1, num2))
    elif choice == 4:
        print(div_fun(num1, num2))
    else:
        print("Invalid choice")

    cont = input('''
    Do you want to continue? 
    Press 'y' for Yes | 'n' for No ''')
    if cont == 'n':
        break

