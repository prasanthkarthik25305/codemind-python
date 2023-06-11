def perfect(n):
    for i in range(1,int(n**0.5)+1):
        if(n==i*i):
            return True
    else:
        return False
n=int(input())
l=list(map(int,input().split()))
s=0
for i in l:
    if perfect(i):
        s+=i
print(s)