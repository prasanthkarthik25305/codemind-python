# Input
n = input().strip()
n=n.lower()
# Remove white spaces
n = n.replace(" ", "")
#remove repeated elements
n=sorted(set(n))
# Print the modified string
print(len(n))