def is_palindrome(n):

    # Convert the number to a string
    s = str(n)

    # Reverse the string
    s = s[::-1]

    # Convert the string back to a number
    n_reversed = int(s)

    # Return True if the number is equal to its reversed version
    return n_reversed

# Driver code
if __name__ == "__main__":

    n = int(input())
    l = list(map(int, input().split()))
    for i in l:
        k=is_palindrome(i)
        print(k,end=' ')
