n = int(input())
l = list(map(int, input().split()))
a, b = map(int, input().split())

sum_not_in_range = 0

for i in l:
    if i < a or i > b:
        sum_not_in_range += i

print(sum_not_in_range)
