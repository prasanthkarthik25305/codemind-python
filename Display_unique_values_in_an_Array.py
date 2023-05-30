t = int(input())  # Takes an input for the number of test cases (assuming t is the number of test cases)
l = list(map(int, input().split()))  # Takes a space-separated input and converts it into a list of integers
m = []  # Creates an empty list

for i in l:
    # Checks if the count of the current element in the list is less than or equal to 1
    if l.count(i) <= 1:
        m.append(i)  

# Checks if the list m is not empty
if m:
    # Iterates over each element in the list m and prints it followed by a space
    for i in m:
        print(i, end=' ')
else:
    print("-1")  # Prints -1 if the list m is empty
