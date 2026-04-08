def fact(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * fact(n-1)

a = int(input("enter the number for which you want to find factorial : "))
print("Factorial of", a, "is : ", fact(a))