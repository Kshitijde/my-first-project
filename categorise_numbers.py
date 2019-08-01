data = [3, 234, 56, 343, 408, 782, 4, 11, 999, 1000]
even=[]
odd=[]
not_prime=[]
length=data.__len__()
j=0
k=0
m=0
for i in range(length):
    if int(data[i])%2==0:
        even.append([])
        even[j]=data[i]
        j += 1
    if int(data[i])%2!=0:
        odd.append([])
        odd[k]=data[i]
        k+=1
    for l in range(2,data[i]):
        if int(data[i])%l==0:
            not_prime.append([])
            not_prime[m]=data[i]
            m+=1
            break
data.sort()
print(data)
for items_1 in range(length):
    for items_2 in range(items_1+1,length-1):
        for items in range(2,data[items_1]+1):
            if data[items_1]%items==0 and data[items_2]%items==0:
                break
            if items-data[items_1]>=0:
                print(f"{data[items_1]} and {data[items_2]} are coprime")
print(f"even numbers are {even}")
print(f"odd numbers are {odd}")
print(f"non-prime numbers are {not_prime}")
print("remaining numbers in the list are prime..")


