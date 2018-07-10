m = n = int(input("Enter size of matrix:\n"))
matrix = []
transpose = []
for i in range(0, m):
    matrix.append([])
    transpose.append([])
for i in range(0, m):
    for j in range(0, n):
        matrix[i].append(j)
        matrix[i][j] = 0
        transpose[i].append(j)
        transpose[i][j] = 0
for i in range(0, m):
    for j in range(0, n):
        print('entry in row: ', i+1,' column: ', j+1)
        matrix[i][j] = int(input())

for i in range(0, m):
    for j in range(0, n):
        transpose[i][j] = matrix[j][i]
        print(transpose[i][j], end=" ")
    print('\n')
