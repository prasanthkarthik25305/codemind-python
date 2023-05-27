n = input()
c = 1
for i in n:
    if n.count(i) > 1:
        c = 0
        break
if c == 1:
    print("Unique Number")
else:
    print("Not Unique Number")
