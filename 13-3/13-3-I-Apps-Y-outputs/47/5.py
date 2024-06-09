
def get_maximum_sum_of_absolute_differences(n, m):
    # Initialize the array with all elements as 0
    arr = [0] * n
    
    # Base case: if n is 1, the only possible array is [m]
    if n == 1:
        return 0
    
    # Initialize the maximum sum of absolute differences
    max_sum = 0
    
    # Iterate over all possible values of the first element
    for i in range(m + 1):
        # Recursively call the function for the remaining elements
        # and calculate the sum of absolute differences
        sum_abs_diff = abs(i - arr[1:])
        sum_abs_diff = sum(sum_abs_diff)
        
        # Update the maximum sum of absolute differences
        if sum_abs_diff > max_sum:
            max_sum = sum_abs_diff
    
    return max_sum

