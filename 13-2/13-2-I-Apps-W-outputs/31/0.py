
def solve(n, H):
    # Initialize the heights of the sand pillars as a list of zeros
    heights = [0] * (n + 1)
    
    # Set the height of the first pillar to be the height of the fence
    heights[0] = H
    
    # Initialize the number of spots occupied to be 1
    spots = 1
    
    # Loop through the remaining spots
    for i in range(1, n):
        # If the current spot is higher than the previous spot, set its height to be the difference between the previous spot and the fence height
        if heights[i-1] > heights[i]:
            heights[i] = heights[i-1] - H
        # Otherwise, set its height to be one less than the previous spot
        else:
            heights[i] = heights[i-1] - 1
        
        # If the current spot is not zero, increase the number of spots occupied
        if heights[i] != 0:
            spots += 1
    
    return spots

