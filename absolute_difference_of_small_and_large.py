n=input()
m=n.split()
e=[]
for i in m:
    e.append(ord(max(i))-ord(min(i)))
for i in e:
    print(i,end=" ")