n=input()
s,k=0,1
for i in n:
    s+=int(i)
    k*=int(i)
print(k-s)