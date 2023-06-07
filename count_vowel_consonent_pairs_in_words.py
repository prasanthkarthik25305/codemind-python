n = input()
m = n.split()
v = 'aeiou'
c = 0
for i in m:
    for char in range(len(i)):
        if i[char] not in v and i[len(i) - char - 1] in v:
            c = c + 1
print(c)
