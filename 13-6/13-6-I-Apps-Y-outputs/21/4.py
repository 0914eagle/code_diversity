
def solve(n, m):
    # Initialize the array with all elements as 0
    arr = [0] * n
    # Set the first element as m
    arr[0] = m
    # Iterate from the second element to the last element
    for i in range(1, n):
        # Calculate the difference between the current element and the previous element
        diff = m - arr[i-1]
        # If the difference is positive, set the current element as the difference, otherwise set it as 0
        arr[i] = diff if diff > 0 else 0
    # Return the sum of absolute differences between adjacent elements
    return sum(map(abs, [arr[i+1] - arr[i] for i in range(n-1)]))

