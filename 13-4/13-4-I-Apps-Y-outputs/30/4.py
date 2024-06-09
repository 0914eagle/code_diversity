
def solve(n, k, arr):
    # Sort the array in non-decreasing order
    arr.sort()
    # Initialize the minimum number of operations to 0
    min_operations = 0
    # Loop through the array and find the first index where the value is greater than or equal to k
    for i in range(n):
        if arr[i] >= k:
            break
    # If all values in the array are less than k, return -1
    if i == n:
        return -1
    # Loop through the array and calculate the minimum number of operations required to make all values equal to k
    for i in range(i, n):
        min_operations += (arr[i] - k) // 2
        arr[i] = k
    return min_operations

