def is_palindrome(n):

    # Convert the number to a string
    s = str(n)

    # Reverse the string
    s = s[::-1]

    # Convert the string back to a number
    n_reversed = int(s)

    # Return True if the number is equal to its reversed version
    return n == n_reversed

# Driver code
if __name__ == "__main__":

    n = int(input())
    l = list(map(int, input().split()))
    c = 0
    for i in l:
        if is_palindrome(i) == True:
            c = c + 1
    print(c)
