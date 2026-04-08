
X1 = int(input("Enter the number: "))
X2 = int(input("Enter the range: "))

print(f"Multiplication table of {X1} up to {X2}:")

for i in range(1, X2 + 1):
    print(f"{X1} x {i} = {X1 * i}")