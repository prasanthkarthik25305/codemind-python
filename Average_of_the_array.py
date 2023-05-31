n = int(input())
l = input().split()
s = 0
for i in l:
    s += int(i)
print("{:.2f}".format(s/n))
