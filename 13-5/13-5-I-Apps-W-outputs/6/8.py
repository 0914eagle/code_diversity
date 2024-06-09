
def get_min_remainder(n, m):
    # Convert the integer to a string
    n_str = str(n)
    
    # Initialize the minimum remainder to the remainder of the first good shift
    min_remainder = int(n_str) % m
    
    # Iterate over the good shifts of the integer
    for i in range(len(n_str)):
        # Calculate the remainder of the current good shift
        remainder = int(n_str[i:] + n_str[:i]) % m
        
        # Update the minimum remainder if necessary
        if remainder < min_remainder:
            min_remainder = remainder
    
    return min_remainder

