
def solve(n, m):
    # Initialize the array with all elements as 0
    arr = [0] * n
    # Set the first element as m
    arr[0] = m
    # Initialize the maximum sum of absolute differences
    max_sum = 0
    # Loop through the array and calculate the sum of absolute differences
    for i in range(n-1):
        max_sum += abs(arr[i] - arr[i+1])
    # Return the maximum sum of absolute differences
    return max_sum

