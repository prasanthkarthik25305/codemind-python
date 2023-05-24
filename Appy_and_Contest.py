from math import gcd

t = int(input())

for _ in range(t):
    n, a, b, k = map(int, input().split())

    problems_solved = n // a + n // b - 2 * (n // (a * b // gcd(a, b)))

    if problems_solved >= k:
        print("Win")
    else:
        print("Lose")
