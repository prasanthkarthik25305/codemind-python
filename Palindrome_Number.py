t = int(input())

for _ in range(t):
    a = int(input())
    s = 0  # Reset s to 0 for each number
    b = a
    k = abs(a)
    
    while k > 0:
        r = k % 10
        s = s * 10 + r
        k = k // 10
        
    if a > 0 and s == b:
        print("True")
    elif a < 0 and -s == b:
        print("True")
    else:
        print("False")
