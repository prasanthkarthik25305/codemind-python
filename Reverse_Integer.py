n=int(input())
s,k=0,0
if n<0:
    s=abs(n)
    while(s>0):
        r=s%10
        k=k*10+r
        s=s//10
else:
    while(n>0):
        r=n%10
        s=s*10+r
        n=n//10
if n<0:
    print(k*-1)
else:
    print(s)
