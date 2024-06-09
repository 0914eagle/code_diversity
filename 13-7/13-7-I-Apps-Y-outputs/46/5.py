
def get_largest_perfect_power(x):
    # Initialize a list to store the perfect powers
    perfect_powers = []
    
    # Loop through all possible values of b
    for b in range(1, x + 1):
        # Loop through all possible values of p
        for p in range(2, x + 1):
            # Check if b^p is a perfect power and is less than or equal to x
            if b ** p <= x and b ** p >= b:
                # Add b^p to the list of perfect powers
                perfect_powers.append(b ** p)
    
    # Return the largest perfect power
    return max(perfect_powers)

