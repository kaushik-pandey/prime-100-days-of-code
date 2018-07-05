string_input = input("Enter any string: ")
# print(string_input[-1])
for n in range(1, len(string_input)+1):
    print(string_input[-n], end="")
