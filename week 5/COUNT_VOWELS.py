# a = str(input("enter a string"))
# b = ["a" , "e" , "i" , "o" , "u"]
# count = 0
# i = 0
# for v in a:
#     if(v in a):
#         count = count+1
# print(count)


s = input("Enter a string: ") 

vowels = "aeiouAEIOU" # Includes both small and capital letters
count = 0 

for ch in s:
    if ch in vowels: # Check if the current character is a vowel
        count += 1 

print("Number of vowels:", count)