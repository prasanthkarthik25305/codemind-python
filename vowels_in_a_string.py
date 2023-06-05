n = input()
vowels = input()
index = -1  # Initialize index to -1 indicating no vowel found

for vowel in vowels:
    if vowel in n:
        index = n.index(vowel)
        break

if index != -1:
    print('True')
    print(index)
else:
    print('False')
