
def solve(n, H):
    # Initialize the heights of the pillars as a list of zeros
    heights = [0] * (n + 1)
    
    # Set the height of the first pillar to be the height of the fence
    heights[0] = H
    
    # Initialize the number of spots as 1
    spots = 1
    
    # Loop through the remaining pillars
    for i in range(1, n):
        # If the height of the current pillar is less than or equal to the height of the previous pillar, set it to be one more than the previous pillar
        if heights[i - 1] <= heights[i]:
            heights[i] = heights[i - 1] + 1
        # Otherwise, set it to be one less than the previous pillar
        else:
            heights[i] = heights[i - 1] - 1
        
        # Increment the number of spots
        spots += 1
    
    # Return the number of spots
    return spots

