n=int(input())
l=list(map(int,input().split()))
k=max(l)
c=0
for i in l:
    if len(str(i))>=len(str(k)):
        c=c+1
print(c)