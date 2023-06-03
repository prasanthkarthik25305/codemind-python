n = int(input())
l = list(map(int, input().split()))

max_digits = max(len(str(i)) for i in l)
m = []
s = set()
for i in l:
  if len(str(i)) == max_digits and i not in s:
    m.append(i)
    s.add(i)

for i in m:
  print(i, end=" ")
