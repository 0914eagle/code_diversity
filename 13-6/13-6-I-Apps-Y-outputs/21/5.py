
def solve(n, m):
    # Initialize the array with all elements as 0
    arr = [0] * n
    
    # Base case: if n is 1, the array is just [m]
    if n == 1:
        return m
    
    # Initialize the maximum sum of absolute differences
    max_sum = 0
    
    # Iterate over all possible values of the first element
    for i in range(m + 1):
        # Recursively find the maximum sum of absolute differences for the remaining elements
        remaining_sum = m - i
        remaining_abs_diff_sum = solve(n - 1, remaining_sum)
        
        # Calculate the sum of absolute differences for the current array
        current_abs_diff_sum = abs(i - (m - i))
        
        # Update the maximum sum of absolute differences
        max_sum = max(max_sum, current_abs_diff_sum + remaining_abs_diff_sum)
    
    return max_sum

