words = ["apple", "banana", "kiwi", "education"]
vowel_data = []
vowels = "aeiouAEIOU"

for w in words:
    count = 0
    for ch in w:
        if ch in vowels:
            count += 1
    
    vowel_data.append((count, w))

vowel_data.sort()

sorted_words = []
for count, word in vowel_data:
    sorted_words.append(word)

print("Sorted by vowel count:", sorted_words)