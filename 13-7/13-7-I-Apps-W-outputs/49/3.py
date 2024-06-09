
def solve(n, arr):
    # Sort the array in non-decreasing order
    arr.sort()
    # Initialize the result
    result = 0
    # Loop through the array
    for i in range(n):
        # Calculate the square of the current element
        result += arr[i] ** 2
    # Return the result
    return result

