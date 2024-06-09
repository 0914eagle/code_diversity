
def get_maximum_sum(n, m):
    # Initialize the array with 0s
    arr = [0] * n
    # Set the first element to m
    arr[0] = m
    # Loop through the array and calculate the sum of absolute differences
    for i in range(1, n):
        arr[i] = arr[i-1] - 1
    # Return the sum of absolute differences
    return sum(map(abs, arr))

