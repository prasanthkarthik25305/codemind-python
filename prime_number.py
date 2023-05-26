import math
def isprime(n):
    if n<2:
        return False
    for i in range(2,int(math.sqrt(n))+1):
        if n%i==0:
            return False
    else:
        return True
n=int(input())
if isprime(n):
     print("prime")
else:
    print("not a prime")