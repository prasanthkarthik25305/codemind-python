def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True

def find_prime_product(n):
    for i in range(2, n):
        if n % i == 0:
            factor = i
            if is_prime(factor) and is_prime(n // factor):
                return factor, n // factor
    return -1
    
n = int(input())

result = find_prime_product(n)

if result == -1:
    print(-1)
else:
    print(result[0],result[1])