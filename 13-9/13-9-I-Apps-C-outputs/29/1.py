
def get_maximum_sum(arr):
    # Sort the array in non-decreasing order
    arr.sort()
    # Initialize the maximum sum to be the sum of the first n elements
    max_sum = sum(arr[:n])
    # Iterate through the array and calculate the sum of the first n elements with each sign change
    for i in range(n):
        max_sum = max(max_sum, sum(arr[:i]) + sum(arr[i:]))
    return max_sum

