n = input()
n = ''.join(filter(str.isdigit, n))  # Remove non-digit characters

c, k = 0, 1

for i in n:
    c += int(i)
    k *= int(i)

if c == k:
    print("Spy Number")
else:
    print("Not Spy Number")
