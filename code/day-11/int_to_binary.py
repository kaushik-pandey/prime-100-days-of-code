num = int(input("Enter positive number:\n"))
n = 1
c = 8
if num >= 0:
    binary = []
    while n <= c:
        rem = num % 2
        binary.append(rem)
        num = num // 2
        if n == 8 and num != 0:
            c = c + 8
        n += 1

    print(binary[::-1])
else:
    print("Enter positive integer")
