# Input
n = input().strip()
n=n.lower()
# Remove white spaces
n = n.replace(" ", "")
#remove repeated elements
n=sorted(set(n))
# Print the modified string

for i in n:
    print(i,end='')