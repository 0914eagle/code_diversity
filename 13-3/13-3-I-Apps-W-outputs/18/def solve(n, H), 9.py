
def solve(n, H):
    # Initialize the heights of the sand pillars as a list of zeros
    heights = [0] * (n + 1)
    
    # Set the height of the first sand pillar to be the height of the fence
    heights[0] = H
    
    # Initialize the number of spots occupied to be 1
    spots = 1
    
    # Loop through the remaining sand packs
    for i in range(1, n):
        # If the current height is less than or equal to the height of the fence, set the height to be the height of the fence
        if heights[i] <= H:
            heights[i] = H
        # Otherwise, set the height to be one more than the previous height
        else:
            heights[i] = heights[i - 1] + 1
        
        # If the absolute difference between the current height and the previous height is greater than 1, increase the number of spots occupied
        if abs(heights[i] - heights[i - 1]) > 1:
            spots += 1
    
    # Return the number of spots occupied
    return spots

