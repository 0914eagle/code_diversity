
def solve(n, a):
    # Sort the array in non-decreasing order
    a.sort()
    # Initialize the result
    result = 0
    # Loop through the array
    for i in range(n):
        # Calculate the sum of squares up to the current element
        result += a[i] ** 2
        # If there are more elements after the current one, calculate the minimum sum of squares for the remaining elements
        if i + 1 < n:
            result += min(a[i + 1:] ** 2)
    return result

