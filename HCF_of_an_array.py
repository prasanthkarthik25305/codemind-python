def gcd(a,b):
    while b!=0:
        a,b=b,a%b
    return a

n=int(input())
a=list(map(int,input().split()))
result=a[0]
for i in range(1,n):
    result=gcd(result,a[i])
print(result)