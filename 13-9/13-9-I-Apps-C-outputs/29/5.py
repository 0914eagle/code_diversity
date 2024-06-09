
def get_maximum_sum(arr):
    # Sort the array in non-decreasing order
    arr.sort()
    # Initialize the maximum sum to be the sum of the first n elements
    max_sum = sum(arr[:n])
    # Loop through the remaining elements
    for i in range(n, len(arr)):
        # If the current element is greater than the largest element in the first n elements, include it
        if arr[i] > arr[n-1]:
            max_sum += arr[i]
    return max_sum

