
def max_operations(arr, pairs):
    # Sort the array in non-decreasing order
    arr.sort()
    # Initialize a variable to store the maximum number of operations
    max_ops = 0
    # Iterate over the good pairs
    for i, j in pairs:
        # Check if the pair is valid
        if i + j % 2 == 1 and 1 <= i < j <= len(arr):
            # Divide both numbers by the smaller one
            smaller = min(arr[i], arr[j])
            arr[i] //= smaller
            arr[j] //= smaller
            # Increment the maximum number of operations
            max_ops += 1
    # Return the maximum number of operations
    return max_ops

