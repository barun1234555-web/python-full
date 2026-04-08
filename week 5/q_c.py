s = input("Enter a string: ")

result = [ ]
count = 1

for i in range(1, len(s)):
    if s[i] == s[i-1]:
        count += 1
    else:
        result.append((s[i-1], count))
        count = 1

result.append((s[-1], count))

print(result)