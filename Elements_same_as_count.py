n = int(input())
l = list(map(int, input().split()))
m = []
count_dict = {}

for num in l:
    if num not in count_dict:
        count_dict[num] = 1
    else:
        count_dict[num] += 1

for num in l:
    if num in count_dict and count_dict[num] == num:
        m.append(num)
        count_dict.pop(num)

if m:
    for num in m:
        print(num, end=" ")
else:
    print("-1")
