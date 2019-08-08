data=[17,18,2,3,6,9,5,8,89,100]
length=data.__len__()
larger_number=data[0]
for j in range(length):
    for i in range(length-1-j):
        if data[i]>data[i+1]:
            larger_number = data[i]
            data[i] = data[i+1]
            data[i+1] =larger_number
print(data)

