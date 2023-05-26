n=input()
c=0
for i in range(0,len(n)):
    c+=int(n[i])**(i+1)
if int(n)==c:
    print("True")
else:
    print("False")
