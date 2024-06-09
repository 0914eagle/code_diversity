
def get_min_remainder(n, m):
    # Convert the integer to a string
    n_str = str(n)
    
    # Initialize the minimum remainder to the remainder of the first shift
    min_rem = n_str[0] % m
    
    # Iterate over the other shifts
    for i in range(1, len(n_str)):
        # Calculate the remainder of the current shift
        rem = (int(n_str[i:] + n_str[:i]) % m)
        
        # Update the minimum remainder if necessary
        if rem < min_rem:
            min_rem = rem
    
    return min_rem

