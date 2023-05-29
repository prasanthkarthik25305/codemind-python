n=int(input())
a,b,c=0,1,0
d=0
while d<n:
    a=b
    b=c
    c=a+b
    print(b,end=' ')
    d=d+1