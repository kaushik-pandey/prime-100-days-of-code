size = int(input("Enter no. of elements you want to add to array: "))
array = []
for n in range(size):
    m = n + 1
    array.insert(n, int(input("Enter element no. %d: " % m)))

for n in array:
    if array.count(n) > 1:
        print(n, " is the first duplicate element")
        break
dup = []
for n in array:
    if array.count(n) > 1:
        if n not in dup:
            dup.append(n)
print("This is the sub-array of duplicate items: ", dup)
