
def solve(a):
    n = len(a)
    if n == 1:
        return a
    
    # Initialize the minimum integer as the initial integer
    min_int = a
    
    # Iterate over each pair of adjacent digits
    for i in range(n-1):
        # If the digits have different parity, swap them and check if the result is smaller than the current minimum
        if a[i] % 2 != a[i+1] % 2:
            swapped_int = a[:i] + a[i+1] + a[i] + a[i+2:]
            if swapped_int < min_int:
                min_int = swapped_int
    
    return min_int

