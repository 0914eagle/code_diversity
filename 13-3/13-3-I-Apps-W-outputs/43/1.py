
def solve(a):
    n = len(a)
    if n == 1:
        return a
    
    # Initialize the minimum integer as the initial integer
    min_int = a
    
    # Iterate over all possible pairs of adjacent digits
    for i in range(n-1):
        for j in range(i+1, n):
            # If the digits are of different parity, swap them and check if the result is smaller than the current minimum
            if a[i] % 2 != a[j] % 2:
                new_int = a[:i] + a[j] + a[i] + a[j+1:]
                if new_int < min_int:
                    min_int = new_int
    
    return min_int

