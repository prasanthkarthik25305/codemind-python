n=int(input())
s=0
while(n>10):
    r=n%10
    n=n//10
    n=n+r
print(n)