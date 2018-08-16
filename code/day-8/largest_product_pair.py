size = int(input("Enter no. of items you want to add: "))
array = []
for n in range(size):
    m = n + 1
    array.insert(n, int(input("Enter item no. %d: " % m)))
max_val = 0
pair = []
for n in range(size-1):
    for m in range(n+1, size):
        val = array[n] * array[m]
        if val > max_val:
            max_val = val
            m1 = array[n]
            m2 = array[m]
        elif val == max_val:
            sec_pair = []
            sec_pair.extend((array[n], array[m]))
pair.extend((m1, m2))
print(pair)
print(sec_pair)
