
def get_max_volume(L):
    # Initialize the variables to find the maximum volume
    a = b = c = 0
    
    # Loop through all possible values of a
    for a in range(1, L + 1):
        # Find the maximum value of b that satisfies the condition
        b = (L - a) / 2
        
        # Find the maximum value of c that satisfies the condition
        c = math.sqrt(L**2 - a**2 - b**2)
        
        # Check if the current combination is the maximum volume
        if a + b + c == L:
            return a * b * c
    
    # If no combination is found, return 0
    return 0

