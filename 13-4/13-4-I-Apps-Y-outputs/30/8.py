
def solve(n, k, arr):
    # Sort the array in non-decreasing order
    arr.sort()
    # Initialize the number of operations to 0
    operations = 0
    # Loop through the array and find the first index where the value is greater than or equal to k
    for i in range(n):
        if arr[i] >= k:
            break
    # If no such index exists, return -1
    if i == n:
        return -1
    # Otherwise, loop through the array and divide the values by 2, rounding down, until the value is equal to k
    for j in range(i, n):
        while arr[j] > k:
            arr[j] //= 2
            operations += 1
    # Return the number of operations required
    return operations

