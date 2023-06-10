# Input
n = input().strip()
n=n.lower()
# Remove white spaces
n = n.replace(" ", "")
c=0
for i in n:
    if n.count(i)==1:
        c=c+1
# Print the modified string
print(c)