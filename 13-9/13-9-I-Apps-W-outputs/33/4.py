
def get_min_height(n, k):
    # Initialize the height as 0
    height = 0
    
    # Iterate through each point with an odd x-coordinate
    for i in range(1, 2*n, 2):
        # Increase the height by 1 for each point with an odd x-coordinate
        height += 1
        
        # If the current height is greater than the area, return the previous height
        if height > k:
            return height - 1
    
    # Return the final height
    return height

