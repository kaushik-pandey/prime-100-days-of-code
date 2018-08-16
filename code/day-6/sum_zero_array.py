size = int(input("Enter no. of items you want to add:\n"))
array = []
for n in range(size):
    array.append(0)
    print("Enter ", n+1, " element")
    array[n] = int(input())
s = 0
for n in range(size-1):
    for m in range(n, size):
            # s = array[n] + array[m]
            # if s == 0:
            #     sum_zero = []
            #     sum_zero.append(array[n])
            #     sum_zero.append(array[m])
            #     print(sum_zero)
            # elif m == size:
            #     sum_zero = []
            #     s = s + array[m+1]
            #     sum_zero.append(s)
            #     print(sum_zero)
            s = s + array[m]
            if s != 0:
                continue
            elif s == 0:
                sum_zero = []
                sum_zero.append(array[n])
                sum_zero.append(array[m])
                print(sum_zero)
