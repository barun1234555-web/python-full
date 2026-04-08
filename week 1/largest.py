a = int(input("enter first number number: "))
b = int(input("enter second number number: "))
c = int(input("enter third number number: "))

if(a>b & a>c):
    print(f"{a} is the greatest")
elif(b>a & b>c):
    print(f"{b} is the greatest")
else:
    print(f"{c} is the greatest")
