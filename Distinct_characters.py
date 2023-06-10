# Input
n = input().strip()
n=n.lower()
# Remove white spaces
n = n.replace(" ", "")
c=[]
for i in n:
    if n.count(i)==1:
        c.append(i)
c=sorted(c)
# Print the modified string
for i in c:
    print(i,end='')