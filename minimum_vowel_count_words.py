import string

def is_vowel(c):
    return c in set(string.ascii_lowercase + string.ascii_uppercase).intersection('aeiou')

def count_min_vowels(s):
    m = s.split()
    c = 0
    for i in m:
        if len([c for c in i if is_vowel(c)]) == min([len([c for c in w if is_vowel(c)]) for w in m]):
            c += 1
    return c

s = input()
count = count_min_vowels(s)
print(count)
