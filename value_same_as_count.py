def find_elements(arr):
    unique_elements = []
    seen_elements = set()

    for num in arr:
        if num not in seen_elements:
            count = arr.count(num)
            if num == count:
                unique_elements.append(num)
                seen_elements.add(num)

    print(len(unique_elements))

# Read input
N = int(input())
array = list(map(int, input().split()))

# Find elements satisfying the condition
find_elements(array)
