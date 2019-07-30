data = [3, 234, 56, 343, 408, 782, 0, 11, 999, 1000]
even=[]
odd=[]
not_prime=[]
j=0
k=0
m=0
for i in range(10):
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
print(f"even numbers are {even}")
print(f"odd numbers are {odd}")
print(f"non-prime numbers are {not_prime}")
print("remaining numbers in the list are prime..")


