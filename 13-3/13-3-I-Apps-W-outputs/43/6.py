
def solve(a):
    n = len(a)
    if n == 1:
        return a
    
    # Initialize the minimum integer as the initial integer
    min_int = a
    
    # Iterate through each position in the integer
    for i in range(n - 1):
        # Check if the current position is adjacent to the next position
        if a[i] != '0' and a[i+1] != '0' and a[i] % 2 != a[i+1] % 2:
            # Swap the current position with the next position
            min_int = min_int[:i] + a[i+1] + a[i] + min_int[i+2:]
    
    return min_int

