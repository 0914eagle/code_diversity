
n = int(input())
a = list(map(int, input().split()))

# Function to check if a subarray is strictly increasing
def is_increasing(arr):
    for i in range(len(arr) - 1):
        if arr[i] >= arr[i + 1]:
            return False
    return True

# Initialize variables
max_len = 1
for i in range(n):
    # Case 1: Remove element at index i
    if i > 0 and i < n - 1:
        if a[i - 1] < a[i + 1]:
            max_len = max(max_len, i + 1)
    # Case 2: Remove element at index i-1
    if i > 0:
        if a[i - 1] < a[i]:
            max_len = max(max_len, i)
    # Case 3: Remove element at index i+1
    if i < n - 1:
        if a[i] < a[i + 1]:
            max_len = max(max_len, n - i - 1)

print(max_len)
