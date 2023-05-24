N, R = map(int, input().split())

for i in range(1, R + 1):
    if i % 2 != 0:  # Exclude multiples of 2
        result = N * i
        print(f"{N} x {i} = {result}")
