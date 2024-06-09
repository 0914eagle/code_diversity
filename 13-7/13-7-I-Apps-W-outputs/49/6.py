
def solve(n, a):
    # Sort the array in non-decreasing order
    a.sort()
    # Initialize the result
    result = 0
    # Loop through the array
    for i in range(n):
        # Calculate the sum of squares up to the current element
        result += a[i] * a[i]
        # If there are still elements left in the array
        if i + 1 < n:
            # Calculate the bitwise AND and OR of the current element and the next element
            and_result = a[i] & a[i + 1]
            or_result = a[i] | a[i + 1]
            # If the bitwise AND is not zero
            if and_result != 0:
                # Replace the current element with the bitwise AND result
                a[i] = and_result
            # If the bitwise OR is not zero
            if or_result != 0:
                # Replace the next element with the bitwise OR result
                a[i + 1] = or_result
    # Return the final result
    return result

