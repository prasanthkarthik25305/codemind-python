n=int(input())
l=list(map(int,input().split()))
m=[]
for i in l:
    if(l.count(i)==i):
        m.append(i)
if m:
    print(min(m),max(m))
else:
    print("-1")
        