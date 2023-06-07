n=input()
m=n.split()
for i in m:
    c=min(i)
    if c.lower() in i and c.upper() in i:
        c=c.lower()
print(c)
        