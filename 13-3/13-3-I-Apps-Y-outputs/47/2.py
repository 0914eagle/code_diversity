
def solve(n, m):
    # Initialize the array with 0s
    arr = [0] * n
    
    # Fill the array with values from m down to 0
    for i in range(n):
        arr[i] = m - i
    
    # Calculate the sum of absolute differences between adjacent elements
    sum_abs_diff = 0
    for i in range(n - 1):
        sum_abs_diff += abs(arr[i] - arr[i + 1])
    
    return sum_abs_diff

