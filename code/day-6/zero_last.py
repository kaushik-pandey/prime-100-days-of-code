array = [3, 0, 1, 0, 5, 9, 0, 6, 7]
a2 = []
a3 = []
for n in array:
    if n != 0:
        a2.append(n)
    else:
        a3.append(n)
array = a2 + a3
print(array)
