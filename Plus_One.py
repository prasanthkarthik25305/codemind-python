n = int(input())
digits = list(map(int, input().split()))

carry = 1
for i in range(len(digits) - 1, -1, -1):
    digits[i] += carry
    if digits[i] <= 9:
        carry = 0
        break
    digits[i] = 0

if carry == 1:
    digits.insert(0, 1)  # Prepend 1 to the list if carry is still 1

for digit in digits:
    print(digit, end=' ')
