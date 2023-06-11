m = int(input())
e=0
a, b, c = 0, 1, 0
while c <= m:
    if c==m:
        e=1
    a = b
    b = c
    c = a + b
if e==0:
    print("False")
else:
    print("True")