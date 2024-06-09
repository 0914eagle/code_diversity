
def get_nearest_fraction(x, y, n):
    # Initialize the minimum difference and the corresponding fraction
    min_diff = float('inf')
    nearest_frac = None
    
    # Iterate through all possible denominators
    for b in range(1, n+1):
        # Calculate the current fraction
        a = x*b//y
        
        # Calculate the current difference
        diff = abs(x/y - a/b)
        
        # If the current difference is less than the minimum difference, update the minimum difference and the corresponding fraction
        if diff < min_diff:
            min_diff = diff
            nearest_frac = a, b
    
    # Return the nearest fraction
    return str(nearest_frac[0]) + '/' + str(nearest_frac[1])

