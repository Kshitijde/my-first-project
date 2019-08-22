#to sort a list using insertion sort
unsorted_list=[2,3,43,8,1,0,]
sorted_list=[]
for i in range(len(unsorted_list)):
    sorted_list.append(unsorted_list[i])
    for j in range(len(sorted_list)-1):
        k=len(sorted_list)-1-j
        if j!=len(sorted_list)-2 and sorted_list[k]<sorted_list[k-1]:
            sorted_list[k],sorted_list[k-1]=sorted_list[k-1],sorted_list[k]
        elif j!=len(sorted_list)-2 and sorted_list[k]>sorted_list[k-1]:
            break
        if j==((len(sorted_list))-2) and sorted_list[k]<sorted_list[k-1]:
            sorted_list[k],sorted_list[k-1]=sorted_list[k-1],sorted_list[k]
print(sorted_list)

