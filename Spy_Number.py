n=int(input())
m=n
s,k=0,1
while n!=0:
    r=n%10
    s+=r
    k*=r
    n=n//10
if s==k:
    print('Spy Number')
else:
    print('Not Spy Number')
