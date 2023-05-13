n=int(input())
l=list(map(int,input().split()))
m=list(map(int,input().split()))
s,k=0,0
for i in range(len(l)):
    s+=l[i]
for i in range(len(m)):
    k+=m[i]
if k-s<=0:
    print(0)
else:
    print(k-s)