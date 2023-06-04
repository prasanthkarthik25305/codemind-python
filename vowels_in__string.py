def get_unique_vowels(string):
    vowels = 'aeiouAEIOU'
    unique_vowels = []
    seen_vowels = set()
    for char in string:
        if char in vowels and char not in seen_vowels:
            unique_vowels.append(char)
            seen_vowels.add(char)
    if not unique_vowels:
        return -1
    return ' '.join(unique_vowels)

string = input()
print(get_unique_vowels(string))
