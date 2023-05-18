n=int(input())
c=0
for i in range(1,n//2):
    if i*(i+1)==n:
        c=c+1
if c==1:
    print('YES')
else:
    print('NO')