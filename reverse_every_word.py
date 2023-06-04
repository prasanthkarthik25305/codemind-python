n = input()
l = n.split()
for i in range(len(l)):
    l[i]=l[i][::-1]
print(" ".join(l))
