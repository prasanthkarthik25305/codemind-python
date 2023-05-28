n=input()
s,m=0,0
for i in n:
     s+=int(i)**2
k=str(s)
for i in k:
    m+=int(i)
if m==int(n):
    print("Neon Number")
else:
    print("Not Neon Number")