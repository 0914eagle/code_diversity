
def get_maximum_sum(arr):
    # Sort the array in non-decreasing order
    arr.sort()
    # Initialize the maximum sum to be the sum of the first n elements
    max_sum = sum(arr[:len(arr)//2])
    # Iterate over the remaining elements
    for i in range(len(arr)//2, len(arr)):
        # Add the current element to the maximum sum
        max_sum += arr[i]
    # Return the maximum sum
    return max_sum

