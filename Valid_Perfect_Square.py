import math as m

t = int(input())

for _ in range(t):
    n = int(input())
    sqrt_n = m.sqrt(n)
    
    if sqrt_n == int(sqrt_n):
        print("True")
    else:
        print("False")
