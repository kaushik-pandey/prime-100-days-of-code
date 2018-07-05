num = int(input("Enter any number to find its factorial: "))
fact = 1
for n in range(1, num+1):
    fact = fact * n
print(fact)
