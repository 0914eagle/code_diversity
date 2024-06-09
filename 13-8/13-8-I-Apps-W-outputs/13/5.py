
def max_birds_on_wire(l, d, n, positions):
    # Sort the positions of the birds
    positions.sort()
    
    # Initialize the number of additional birds that can sit on the wire
    max_birds = 0
    
    # Iterate through the positions of the birds
    for i in range(n):
        # Check if the current bird is at least 6 cm from both poles
        if positions[i] >= 6 and positions[i] + d <= l - 6:
            # Increment the number of additional birds that can sit on the wire
            max_birds += 1
    
    return max_birds

