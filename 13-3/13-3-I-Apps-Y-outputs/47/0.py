
def solve(n, m):
    # Initialize the array with all elements as 0
    arr = [0] * n
    
    # Base case: if n is 1, the only possible array is [m]
    if n == 1:
        return 0
    
    # Initialize the maximum possible sum of absolute differences
    max_abs_diff = 0
    
    # Iterate over all possible values that the first element can take
    for i in range(m + 1):
        # Recursively find the maximum possible sum of absolute differences for the remaining elements
        remaining_sum = m - i
        remaining_abs_diff = solve(n - 1, remaining_sum)
        
        # Calculate the sum of absolute differences for the current array
        current_abs_diff = abs(i - remaining_sum)
        
        # Update the maximum possible sum of absolute differences if necessary
        max_abs_diff = max(max_abs_diff, current_abs_diff + remaining_abs_diff)
    
    return max_abs_diff

