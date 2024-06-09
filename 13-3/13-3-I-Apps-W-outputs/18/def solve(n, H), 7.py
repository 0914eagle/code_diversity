
def solve(n, H):
    # Initialize the heights of the sand pillars as a list of zeros
    heights = [0] * (n + 1)
    
    # Set the height of the first sand pillar to be the height of the fence
    heights[0] = H
    
    # Initialize the number of spots occupied to be 1
    spots = 1
    
    # Loop through the remaining spots
    for i in range(1, n):
        # If the height of the current spot is less than or equal to the height of the previous spot, set it to be one more than the previous spot
        if heights[i - 1] <= heights[i]:
            heights[i] = heights[i - 1] + 1
        # Otherwise, set it to be one less than the previous spot
        else:
            heights[i] = heights[i - 1] - 1
        
        # Increment the number of spots occupied
        spots += 1
    
    # Return the number of spots occupied
    return spots

