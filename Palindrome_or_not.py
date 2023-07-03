n=input().lower()
n=n.split()
c=0
for i in n:
    if i[::-1]==i:
        c=1
if c==0:
    print('False')
else:
    print('True')