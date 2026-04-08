a = int(input("enter the side of triangle: "))
b = int(input("enter the side of triangle: "))
c = int(input("enter the side of triangle: "))

if(a==b==c):
    print("equilateral triangle")
elif(a==b & a!=c):
    print("isosceles triangle")
else:
    print("scalen triangle")