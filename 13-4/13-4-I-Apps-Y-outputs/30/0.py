
def solve(n, k, arr):
    # Sort the array in non-decreasing order
    arr.sort()
    # Initialize the number of operations to 0
    operations = 0
    # Loop through the array and find the first index where the value is greater than or equal to k
    for i in range(n):
        if arr[i] >= k:
            break
    # If all values in the array are less than k, return -1
    if i == n:
        return -1
    # Loop through the array backwards and find the first index where the value is less than or equal to k
    for j in range(n-1, i-1, -1):
        if arr[j] <= k:
            break
    # Calculate the minimum number of operations required to make the values at indices i and j equal
    operations += (arr[i] - arr[j]) // 2
    # Set the values at indices i and j to be equal
    arr[i] = arr[j]
    # Loop through the array from index j+1 to the end and find the first index where the value is greater than or equal to k
    for i in range(j+1, n):
        if arr[i] >= k:
            break
    # If all values in the array are less than k, return -1
    if i == n:
        return -1
    # Loop through the array backwards from index i-1 to the start and find the first index where the value is less than or equal to k
    for j in range(i-1, -1, -1):
        if arr[j] <= k:
            break
    # Calculate the minimum number of operations required to make the values at indices i and j equal
    operations += (arr[i] - arr[j]) // 2
    # Set the values at indices i and j to be equal
    arr[i] = arr[j]
    # Return the total number of operations required
    return operations

