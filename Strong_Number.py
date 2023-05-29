def fact(n):
    s=1
    for i in range(1,n+1):
        s*=i
    return s
n=input()
k=0
for i in n:
    k+=fact(int(i))
if k==int(n):
    print("The number",n,"is a strong number")
else:
     print("The number",n,"is not a strong number")