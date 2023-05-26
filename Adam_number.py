n=input()
s=n[-1::-1]
m=str(int(n)**2)
k=str(int(s)**2)
if m==k[-1::-1]:
    print("True")
else:
    print("False")