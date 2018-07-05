num = int(input("Enter any number to find its factor: "))
print(num, '{', end="")

for n in range(1, num+1):
    if num % n/2 == 0:
        print(n, end=" ")

print('}', end="")
