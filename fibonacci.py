sequence=[1,2]
i=1
j=2
k=0
output=0
while True:
    j_new=i+j
    i=j
    j=j_new
    if j>4000000:
        break
    if j%2==0:
        output+=j
print(output)