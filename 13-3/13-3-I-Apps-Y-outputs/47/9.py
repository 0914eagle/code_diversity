
def solve(n, m):
    # Initialize the array with all elements as 0
    arr = [0] * n
    
    # Base case: if n is 1, the only possible array is [m]
    if n == 1:
        return 0
    
    # Initialize the maximum possible sum of absolute differences
    max_sum = 0
    
    # Iterate over all possible values that the first element can take
    for i in range(m + 1):
        # Recursively call the function for the remaining elements
        # and calculate the sum of absolute differences
        sum_abs_diff = abs(i - arr[1:])
        sum_abs_diff = sum(sum_abs_diff)
        
        # If the current sum is greater than the maximum possible sum,
        # update the maximum possible sum
        if sum_abs_diff > max_sum:
            max_sum = sum_abs_diff
    
    return max_sum

