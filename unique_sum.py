n=int(input())
l=list(map(int,input().split()))
l=set(l)
s=0
for i in l:
    s+=i
print(s)