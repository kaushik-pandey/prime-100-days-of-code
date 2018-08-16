import time
start = time.time()
size = int(input("Enter size of array: "))
array = []
for n in range(size):
    m = n + 1
    array.insert(n, int(input("Enter element no. %d: " % m)))
print("Before", array)

for n in range(size-1):
    f = 0
    for m in range(n, size):
        if array[n] > array[m]:
            temp = array[n]
            array[n] = array[m]
            array[m] = temp
            f = 1
    if f == 1:
        continue
    else:
        break
end = time.time()
print("time", end - start)
print("After", array)
