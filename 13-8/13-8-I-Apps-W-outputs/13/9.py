
def get_max_birds(l, d, n, positions):
    # Sort the positions of the birds already on the wire
    positions.sort()
    
    # Initialize the maximum number of additional birds as the total length of the wire
    max_birds = l
    
    # Iterate through the positions of the birds already on the wire
    for i in range(n):
        # Calculate the distance between the current bird and the next bird
        dist = positions[i+1] - positions[i] - d
        
        # If the distance is greater than the maximum number of additional birds, update the maximum number of additional birds
        if dist > max_birds:
            max_birds = dist
    
    # Return the maximum number of additional birds
    return max_birds

