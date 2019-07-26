rows=int(input("rows of matrix 1 are.."))
columns=int(input("columns of first and naturally rows of second are.."))
columns2=int(input("columns of second matrix are.."))
matrix_1=[]
matrix_2=[]
result_matrix=[]
for item1 in range(rows):
    matrix_1.append([])
    result_matrix.append([])
    for item2 in range(columns):
        y=int(input("enter your elements in matrix 1 in order row wise"))
        matrix_1[item1].append(y)
print("matrix 1 is")
print(matrix_1)
for item3 in range(columns):
    matrix_2.append([])
    for item4 in range(columns2):
        y=int(input("enter your elements in matrix 2 in order row wise"))
        matrix_2[item3].append(y)
print("second matrix is")
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