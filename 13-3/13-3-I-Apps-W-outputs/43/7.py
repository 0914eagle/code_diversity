
def solve(a):
    n = len(a)
    if n == 1:
        return a

    # Initialize the minimum integer as the initial integer
    min_int = a

    # Iterate over each position in the integer
    for i in range(n - 1):
        # If the current position is not the last position and the digits at the current position and the next position have different parity
        if a[i] % 2 != a[i + 1] % 2:
            # Swap the digits at the current position and the next position
            min_int = min_int[:i] + str(a[i + 1]) + str(a[i]) + min_int[i + 2:]
            # Recursively call the function with the swapped digits
            min_int = solve(min_int)

    return min_int

