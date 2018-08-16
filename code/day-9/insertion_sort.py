import time
start = time.time()
size = int(input("Enter size of array: "))
array = []
for n in range(size):
    m = n + 1
    array.insert(n, int(input("Enter element no. %d: " % m)))
print("Before", array)

for n in range(size):
    for m in range(n, 0):
