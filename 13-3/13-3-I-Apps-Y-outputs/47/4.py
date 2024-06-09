
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
        # Recursively find the maximum sum of absolute differences for the remaining elements
        remaining_sum = solve(n - 1, m - i)
        
        # Calculate the sum of absolute differences for the current array
        current_sum = abs(i - (m - i)) + remaining_sum
        
        # Update the maximum possible sum of absolute differences
        max_sum = max(max_sum, current_sum)
    
    return max_sum

