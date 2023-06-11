def biggest(a, b, c, d):
    big = a
    if big < b:
        big = b
    if big < c:
        big = c
    if big < d:
        big = d
    return big

def get(i):
    k = arr[i]
    if k == 6:
        return 9
    return 6

def array_reversor():
    a = [0] * 4
    a[0] = arr[3]
    a[1] = arr[2]
    a[2] = arr[1]
    a[3] = arr[0]
    arr[0] = a[0]
    arr[1] = a[1]
    arr[2] = a[2]
    arr[3] = a[3]

def array_convertor(n):
    i = 3
    while i >= 0:
        arr[i] = n % 10
        n //= 10
        i -= 1

arr = [0] * 4
n = int(input())
if n == 9999:
    print("9999")
else:
    array_convertor(n)
    a = get(0)
    a = a * 1000 + arr[1] * 100 + arr[2] * 10 + arr[3]
    b = get(1)
    b = arr[0] * 1000 + b * 100 + arr[2] * 10 + arr[3]
    c = get(2)
    c = arr[0] * 1000 + arr[1] * 100 + c * 10 + arr[3]
    d = get(3)
    d = arr[0] * 1000 + arr[1] * 100 + arr[2] * 10 + d
    ans = biggest(a, b, c, d)
    print(ans)
