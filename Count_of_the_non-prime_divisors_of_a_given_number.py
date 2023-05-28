def isprime(k):
    if k<2:
        return False
    for i in range(2,int(k**0.5)+1):
        if k%i==0:
            return False
    else:
        return True
m=int(input())
c=0
for i in range(1,m+1):
    if m%i==0:
        if isprime(i):
           continue
        else:
           c+=1
print(c)
    