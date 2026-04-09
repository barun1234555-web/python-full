s = input("Enter a string: ")
n = int(input("Enter value of n: "))

freq = {}

for ch in s:
    freq[ch] = freq.get(ch, 0) + 1

sorted_chars = sorted(freq.items(), key=lambda x: x[1], reverse=True)

top_chars = sorted_chars[:n]

for ch, count in top_chars:
    positions = []
    for i in range(len(s)):
        if s[i] == ch:
            positions.append(i)

    print("Character:", ch)
    print("Frequency:", count)
    print("Positions:", positions)