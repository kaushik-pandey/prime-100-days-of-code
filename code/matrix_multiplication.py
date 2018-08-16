row1 = int(input("Enter no. of rows for first matrix:"))
col1 = int(input("Enter no. of column for second matrix:"))
row2 = int(input("Enter no. of rows for second matrix:"))
col2 = int(input("Enter no. of column for second matrix:"))
if col1 == row2:
    matrix1 = []
    matrix2 = []
    for m in range(row1):
        for n in range(col1):
            matrix1.append(0)
    for m in range(row1):
        for n in range(col1):
            matrix2.append(0)

    for m in range(row1):
        for n in range(col1):
            val = int(input("Enter value for matrix1[{}][{}]".format(m, n)))
            matrix1[m, n] = val
        print('\n')

    for m in range(row2):
        for n in range(col2):
            val = int(input("Enter value for matrix2[{}][{}]".format(m, n)))
            matrix2[m][n] = val
        print('\n')

    for m in range(row1):
        for n in range(col1):
            print(matrix1[m][n])
        print('\n')
    for m in range(row2):
        for n in range(col2):
            print(matrix2[m][n])
        print('\n')
else:
    print("Multiplication not possible. Enter valid row and column")


