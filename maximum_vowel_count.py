n=input().lower()
m=n.split()
v='aeiou'
l=[]
for i in m:
    c=0
    for char in i:
        if char in v:
            c=c+1
    l.append(c)
print(max(l))