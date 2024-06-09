
def solve(n, m):
    # Initialize the array with 0s
    arr = [0] * n
    # Set the first element to m
    arr[0] = m
    # Calculate the maximum possible value of the sum of absolute differences
    max_value = abs(arr[0] - arr[1])
    for i in range(1, n-1):
        # Calculate the sum of absolute differences for the current array
        current_value = abs(arr[i] - arr[i+1])
        # If the current sum is greater than the maximum possible value, update the maximum possible value
        if current_value > max_value:
            max_value = current_value
    return max_value

