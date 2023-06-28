s=input()
l=[]
for i in s:
    if int(i)%2!=0:
        l.append(int(i))
for i in range(len(l)):
    l[i]=l[i]*l[i]
for i in l:
    print(i,end='')
        