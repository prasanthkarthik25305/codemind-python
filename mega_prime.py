def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True

def is_mega_prime(n):
    digits = str(n)
    for digit in digits:
        if not is_prime(int(digit)):
            return False
    return True

n = int(input())

if is_prime(n) and is_mega_prime(n):
    print("Mega Prime")
else:
    print("Not Mega Prime")
