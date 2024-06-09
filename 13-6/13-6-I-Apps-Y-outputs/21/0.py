
def solve(n, m):
    # Initialize the array with 0s
    arr = [0] * n
    # Set the first element to the sum
    arr[0] = m
    # Loop through the array and calculate the absolute differences
    for i in range(1, n):
        arr[i] = abs(arr[i-1] - 1)
    # Return the maximum absolute difference
    return max(arr)

