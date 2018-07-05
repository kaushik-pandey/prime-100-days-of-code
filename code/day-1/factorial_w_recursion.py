num = int(input("Enter any number to find its factorial: "))


def factorial(arg):
    if arg <= 1:
        return 1
    else:
        return arg * factorial(arg-1)


print(factorial(num))
