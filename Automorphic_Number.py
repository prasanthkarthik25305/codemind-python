n=input()
m=str(int(n)**2)
if int(n)==int(m)%10**len(n):
    print("Automorphic Number")
else:
    print("Not an Automorphic Number")