n=int(input())
m=int(input())
c,k=0,0
for i in range(1,n):
    if(n%i==0):
        c+=i
for j in range(1,m):
    if(m%j==0):
        k+=j
if c==m and k==n:
    print("Amicable")
else:
    print("Not Amicable")