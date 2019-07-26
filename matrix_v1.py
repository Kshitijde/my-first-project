total=int(input("no of matrices to be multiplied"))
rows = int(input("rows of matrix 1 are.."))
columns = int(input("columns of first and naturally rows of second are.."))
matrix_1=[]
result_matrix=[]
for item1 in range(rows):
    matrix_1.append([])
    result_matrix.append([])
    for item2 in range(columns):
        y = int(input("enter your elements in matrix 1 in order row wise"))
        matrix_1[item1].append(y)
print("matrix 1 is")
print(matrix_1)
for times in range(total-1):
    columns2=int(input("columns of next matrix are.."))
    matrix_2=[]
    for item3 in range(columns):
        matrix_2.append([])
        for item4 in range(columns2):
            y=int(input("enter your elements in next matrix in order row wise"))
            matrix_2[item3].append(y)
    print("next matrix is")
    print(matrix_2)
    i=0
    j=0
    k=0
    output=0
    for rowss in range(rows):
        k += 1
        for columnss in range(columns2):
            j += 1
            for columnsinmatrix1 in range(columns):
                i += 1
                output +=int(matrix_1[k-1][i-1])*int(matrix_2[i-1][j-1])
            result_matrix[k-1].append(output)
            i=0
            output=0
        j=0
        i=0
    print("resultant matrix is ")
    print(result_matrix)
    matrix_1 = result_matrix
    result_matrix=[]
    for item1 in range(rows):
        result_matrix.append([])