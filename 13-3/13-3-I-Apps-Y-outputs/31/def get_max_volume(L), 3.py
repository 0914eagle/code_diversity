
def get_max_volume(L):
    # Initialize the variables to brute force
    a = 1
    b = 1
    c = 1
    
    # Loop through all possible combinations of a and b
    while a + b <= L:
        # Loop through all possible combinations of b and c
        while b + c <= L:
            # Check if the current combination is the maximum volume
            if a * b * c > L:
                return a * b * c
            # Increment c by 0.1
            c += 0.1
        # Reset c and increment b by 0.1
        c = 1
        b += 0.1
    # If the loop completes, return the maximum volume
    return a * b * c

