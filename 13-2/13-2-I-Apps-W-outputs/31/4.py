
def get_min_spots(n, H):
    # Initialize the height of the first spot as 1
    heights = [1]
    # Initialize the number of spots as 1
    spots = 1
    # Loop through the remaining spots
    for i in range(1, n):
        # If the current spot is within the fence, set its height to 1
        if i <= H:
            heights.append(1)
        # Otherwise, set its height to the minimum of the previous two spots
        else:
            heights.append(min(heights[i-1], heights[i-2]) + 1)
        # Update the number of spots
        spots += 1
    # Return the minimum number of spots
    return spots

