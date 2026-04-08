s1 = input("Enter first string: ")
s2 = input("Enter second string: ")

set1 = set(s1)
set2 = set(s2)

common = set1 & set2

print("Common letters:", common)