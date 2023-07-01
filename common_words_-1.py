a=input().lower()
b=input().lower()
a,b,c=a.split(),b.split(),0
for i in a:
    for j in b:
        if i==j:
            c=c+1
print(c)