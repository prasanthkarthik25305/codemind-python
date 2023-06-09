n=input()
m=n.split()
a=[]
for i in m:
        a.append(min(i))
        a.append(max(i))
for i in a:
    print(i,end=' ')