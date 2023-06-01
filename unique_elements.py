def print_unique_elements(arr):
    unique_elements = []
    seen_elements = set()

    for num in arr:
        if num not in seen_elements:
            unique_elements.append(num)
            seen_elements.add(num)

    for num in unique_elements:
        print(num, end=' ')

# Read input
N = int(input())
array = list(map(int, input().split()))

# Print unique elements
print_unique_elements(array)
