
def solve(n, arr):
    # Sort the array in non-decreasing order
    arr.sort()
    # Initialize the result
    result = 0
    # Loop through the array
    for i in range(n):
        # Calculate the sum of squares up to the current element
        result += arr[i] ** 2
        # If there are still elements left in the array
        if i + 1 < n:
            # Calculate the bitwise AND and OR of the current element and the next element
            and_result = arr[i] & arr[i + 1]
            or_result = arr[i] | arr[i + 1]
            # Replace the current element with the bitwise AND result
            arr[i] = and_result
            # Replace the next element with the bitwise OR result
            arr[i + 1] = or_result
    # Return the result
    return result

