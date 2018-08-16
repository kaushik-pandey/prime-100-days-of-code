num = int(input("Enter positive number:\n"))
binary = []
if num < 0:
    c_num = -num
else:
    c_num = num
while c_num != 0:
    rem = c_num % 2
    binary.append(rem)
    c_num = c_num // 2
if num > 0:
    binary.append(0)
else:
    binary.append(1)

print(binary[::-1])
