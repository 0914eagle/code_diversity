
def solve(n, m):
    # Initialize the array with all elements as 0
    arr = [0] * n
    
    # Fill the array with the maximum possible value, i.e., m/n
    for i in range(n):
        arr[i] = m//n
    
    # Calculate the remaining sum
    remaining_sum = m % n
    
    # Distribute the remaining sum among the elements of the array
    for i in range(remaining_sum):
        arr[i] += 1
    
    # Calculate the sum of absolute differences between adjacent elements
    abs_diff_sum = 0
    for i in range(n-1):
        abs_diff_sum += abs(arr[i] - arr[i+1])
    
    return abs_diff_sum

