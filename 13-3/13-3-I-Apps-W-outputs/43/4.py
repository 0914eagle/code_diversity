
def solve(a):
    n = len(a)
    # Initialize the minimum integer to the given integer
    min_int = a
    # Loop through each position in the integer
    for i in range(n-1):
        # If the digits at the current position and the next position have different parity
        if a[i] % 2 != a[i+1] % 2:
            # Swap the digits and check if the result is smaller than the current minimum
            swapped = a[:i] + a[i+1] + a[i] + a[i+2:]
            if swapped < min_int:
                min_int = swapped
    return min_int

