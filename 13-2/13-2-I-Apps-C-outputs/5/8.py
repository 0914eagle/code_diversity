
def get_min_changes(arr, k, s):
    # Calculate the sum of the first k elements
    sum_k = sum(arr[:k])
    # Initialize the minimum number of changes to 0
    min_changes = 0
    # Iterate over the remaining elements
    for i in range(k, len(arr)):
        # Calculate the sum of the current k elements
        sum_k = sum_k - arr[i - k] + arr[i]
        # If the sum is not equal to s, increment the minimum number of changes
        if sum_k != s:
            min_changes += 1
    # Return the minimum number of changes
    return min_changes

