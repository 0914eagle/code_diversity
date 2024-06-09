
def max_sum_after_k_swap(arr, k):
    n = len(arr)
    # Sort the array to get the maximum sum
    arr.sort()
    # Initialize the maximum sum and the current sum
    max_sum = 0
    curr_sum = 0
    # Loop through the array and calculate the current sum
    for i in range(n):
        curr_sum += arr[i]
        # If the current sum is greater than the maximum sum, update the maximum sum
        if curr_sum > max_sum:
            max_sum = curr_sum
        # If the current sum is less than 0, update the current sum to 0
        if curr_sum < 0:
            curr_sum = 0
    # Return the maximum sum
    return max_sum

