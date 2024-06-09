
def solve(n, m):
    # Initialize the array with all elements as 0
    arr = [0] * n
    
    # Base case: if n is 1, the only possible array is [m]
    if n == 1:
        return 0
    
    # Initialize the maximum possible sum of absolute differences
    max_sum = 0
    
    # Iterate over all possible values that the first element of the array can take
    for i in range(m + 1):
        # Recursively find the maximum possible sum of absolute differences for the rest of the array
        rest = solve(n - 1, m - i)
        
        # Calculate the sum of absolute differences for the current array
        current_sum = abs(i - (m - i)) + rest
        
        # Update the maximum possible sum of absolute differences if necessary
        max_sum = max(max_sum, current_sum)
    
    return max_sum

