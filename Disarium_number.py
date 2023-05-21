s=input()
n=list(s)
c=0
for i in range(0,len(n)):
    c+=int(n[i])**int(i+1)
if c==int(s):
    print('True')
else:
    print('False')