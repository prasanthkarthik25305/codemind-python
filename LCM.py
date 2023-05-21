a,b=map(int,input().split())
if a>b:
    q=a
else:
    q=b
m=[]
n=[]
for i in range(1,q+1):
    m.append(a*i)
for i in range(1,q+1):
    n.append(b*i)
c=set(m).intersection(set(n))
print(min(c))
    
    