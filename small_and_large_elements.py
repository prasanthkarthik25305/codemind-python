n=input()
m=n.split()
a=[]
for i in m:
        a.append(min(i))
        a.append(max(i))
print(a[0],a[-1])