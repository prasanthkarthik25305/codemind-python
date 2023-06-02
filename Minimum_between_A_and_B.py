n=int(input())
l=list(map(int,input().split()))
a,b=map(int,input().split())
m=[]
for i in l:
    if i>=a and i<=b:
        m.append(i)
if m:
    print(min(m))
else:
    print("-1")