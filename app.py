print('Hi,i am your calculator')
y=input('Enter first number ')
x=input("Enter second number ")
print("for addition enter 1")
print("for sub enter 2")
print("for multiplication enter 3")
print("for div enter 4")
z=input("enter operation code ")
if int(z)==1:
    print(f"your answer is {int(x)+int(y)}")
elif int(z)==2:
    print(f"your answer is {int(x)-int(y)}")
elif int(z)==3:
    print(f"your answer is {int(x)*int(y)}")
elif int(z)==4:
    print(f"your answer is {int(x)/int(y)}")
else:
    print("Sorry,incorrect code!")