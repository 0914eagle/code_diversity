
def get_max_additional_birds(l, d, n, positions):
    # Sort the positions of the birds
    positions.sort()
    
    # Initialize the number of additional birds to 0
    additional_birds = 0
    
    # Iterate through the positions of the birds
    for i in range(n):
        # Check if the current bird is within the allowed distance from the pole
        if positions[i] < d or positions[i] > l - d:
            continue
        
        # Check if the current bird is within the allowed distance from the previous bird
        if i > 0 and positions[i] - positions[i-1] < d:
            continue
        
        # Increment the number of additional birds
        additional_birds += 1
    
    # Return the maximum number of additional birds
    return additional_birds

