n=int(input())
a,b,c=0,1,0
i=1
while i<=n:
    a=b
    b=c
    c=a+b
    print(b,end=' ')
    i=i+1