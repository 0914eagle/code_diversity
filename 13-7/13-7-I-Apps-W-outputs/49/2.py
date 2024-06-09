
def solve(n, a):
    # Sort the array in non-decreasing order
    a.sort()
    # Initialize the result
    result = 0
    # Loop through the array
    for i in range(n):
        # Calculate the sum of squares up to the current index
        result += a[i] ** 2
        # If the current index is not the last index
        if i != n - 1:
            # Calculate the bitwise AND and OR of the current and next elements
            and_result = a[i] & a[i + 1]
            or_result = a[i] | a[i + 1]
            # Replace the current and next elements with their bitwise AND and OR
            a[i] = and_result
            a[i + 1] = or_result
    # Return the final result
    return result

