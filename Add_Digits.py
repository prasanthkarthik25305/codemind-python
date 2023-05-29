n = int(input())
s = 0

while n > 0 or s > 9:  # Repeat until we get a single-digit sum
    if n == 0:  # If n becomes 0, update n with the current sum value
        n = s
        s = 0
    else:
        r = n % 10
        s += r
        n = n // 10

print(s)
