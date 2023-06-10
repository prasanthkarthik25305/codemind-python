s11=input().lower()
s1=s11.split()
s22=input().lower()
s2=s22.split()
c=[]

for i in s2:
 if i in s1:
     c.append(i)
for i in c:
    print(i,end=' ')