def isprime(n):
    if n<=1:
        return False
    
    for i in range(2,int(n**0.5)+1):
        if n%i==0:
            return False
    return True
def  alldigits(n):
    while n>0: 
        digit=n%10
        if not isprime(digit):
            return False
        n=n//10
    return True
def mega(n):
    return isprime(n) and alldigits(n)
    
n=int(input())
if mega(n):
    print("Mega Prime")
else:
    print("Not Mega Prime")