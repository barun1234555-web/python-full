a = str(input("enter the string: "))
b = str(input("enter the string: "))
if sorted(a) == sorted(b):
    print("Anagram")
else:
    print("Not Anagram")
