def isprime(k):
    if k<2:
        return False
    for i in range(2,int(k**0.5)+1):
        if k%i==0:
            return False
    else:
        return True
n=int(input())
m=int(input())
c=0
for i in range(n,m+1):
    if isprime(i):
        print(i)
    