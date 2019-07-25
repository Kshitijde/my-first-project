matrix_1=[[1,2],[3,4]]
matrix_2=[[2,3],[4,5]]
#multiply these two now.
result_matrix=[[],[],[]]
i=0
j=0
k=0
output=0
for rows in matrix_1:
    k += 1
    for columns in matrix_2[1]:
        j += 1
        for eachnewelemnt in matrix_2[1]:
            i += 1
            output+=int(matrix_1[k-1][i-1])*int(matrix_2[i-1][j-1])
        result_matrix[k-1].append(output)
        i=0
        output=0
    j=0
    i=0
print(result_matrix)