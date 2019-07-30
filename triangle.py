x1=int(input("x-coordinate of first point are:"))
x2=int(input("x-coordinate of second point are:"))
x3=int(input("x-coordinate of third point are:"))
y1=int(input("y-coordinate of first point are:"))
y2=int(input("y-coordinate of second point are:"))
y3=int(input("y-coordinate of third point are:"))
def distance (x,y,w,z):
    distancee=((x-w)**2+(y-z)**2)**0.5
    print(f"distance is {distancee}")
    return distancee


a=distance(x1,y1,x2,y2)
b=distance(x2,y2,x3,y3)
c=distance(x3,y3,x1,y1)
if a+b>c and b+c>a and c+a>b:
    print("congrats it is a triangle.")
    s=(a+b+c)/2
    area=((s)*(s-a)*(s-b)*(s-c))**0.5
    print(f"area is {area}")
else:
    print("lol it wasnt even a triangle.")


