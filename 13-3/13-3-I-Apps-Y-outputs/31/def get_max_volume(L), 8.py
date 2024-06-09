
def get_max_volume(L):
    # Initialize the variables to find the maximum volume
    a = b = c = 0
    
    # Loop through all possible values of a
    for a in range(1, L + 1):
        # Find the maximum value of b and c that satisfies the condition
        b = (L - a) / 2
        c = math.sqrt(L**2 - b**2)
        
        # Check if the volume is maximum
        if a * b * c > max_volume:
            max_volume = a * b * c
    
    return max_volume

