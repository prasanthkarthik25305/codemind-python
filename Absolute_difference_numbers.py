N, X = input().split()
N = str(N)
X = int(X)

first_x_digits = int(N[:X])
last_x_digits = int(N[-X:])

absolute_difference = abs(first_x_digits - last_x_digits)
print(absolute_difference)
