n=input().lower()
n=n.split()
c=0
for i in n:
    if i[::-1]==i:
        c=c+1
print(c)