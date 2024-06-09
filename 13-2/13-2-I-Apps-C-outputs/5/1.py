
def make_smooth(arr, k, s):
    # Calculate the sum of the first k elements
    sum_k = sum(arr[:k])
    # Initialize the minimum number of changes to make
    min_changes = 0
    # Iterate through the array
    for i in range(k, len(arr)):
        # Calculate the sum of the current k elements
        sum_k = sum_k - arr[i - k] + arr[i]
        # If the sum is not equal to s, we need to make a change
        if sum_k != s:
            min_changes += 1
    return min_changes

