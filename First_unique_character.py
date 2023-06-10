
# Input
n = input().strip().lower()

    # Initialize a dictionary to count character occurrences
char_count = {}

# Count the occurrences of each character
for char in n:
    char_count[char] = char_count.get(char, 0) + 1

# Find the first unique character
for char in n:
    if char_count[char] == 1:
        print(char)
        break
else:
    print("-1")
