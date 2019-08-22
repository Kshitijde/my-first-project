#to sort a list using selecction sort
unsorted_list=[2,6,3,1,5]
sorted_list=[]
for i in range(len(unsorted_list)):
    minimum = unsorted_list[0]
    for j in range(len(unsorted_list)):
        if unsorted_list[j]<minimum:
            minimum=unsorted_list[j]
        if j==len(unsorted_list)-1:
            index = unsorted_list.index(minimum)
            unsorted_list[index],unsorted_list[0]=unsorted_list[0],unsorted_list[index]
    sorted_list.append(unsorted_list[0])
    unsorted_list.pop(0)
print(sorted_list)

