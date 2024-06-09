
def solve(a):
    n = len(a)
    # Initialize the minimum integer to the given integer
    min_int = a
    # Loop through each position in the integer
    for i in range(n-1):
        # If the digits at the current position and the next position are of different parity, swap them
        if a[i] % 2 != a[i+1] % 2:
            min_int = min_int[:i] + a[i+1] + a[i] + min_int[i+2:]
    return min_int

