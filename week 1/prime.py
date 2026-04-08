"""a = int(input("enter the first number"))
b = int(input("enter the second number"))

for i in range(a , b+1):
    for j in range (2 , b+1):
        if (i%j == 0):
            print("not prime")
        else:
            print(i)"""



a = int(input("Enter the first number: "))
b = int(input("Enter the second number: "))

print(f"Prime numbers between {a} and {b} are:")

for i in range(a, b + 1):
    if i > 1:                    
        prime = True
        for j in range(2, int(i**0.5) + 1):  
            if i % j == 0:
                prime = False
                break
        if prime:
            print(i)