
def solve(n, k, arr):
    # Sort the array in non-decreasing order
    arr.sort()
    # Initialize the minimum number of operations to 0
    min_operations = 0
    # Loop through the array and find the first element that is greater than or equal to k
    for i in range(n):
        if arr[i] >= k:
            # If the element is greater than or equal to k, break the loop
            break
        # Otherwise, increment the minimum number of operations by 1
        min_operations += 1
    # Return the minimum number of operations
    return min_operations

