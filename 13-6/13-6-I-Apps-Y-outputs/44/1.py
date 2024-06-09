
def get_visible_inns(heights):
    # Sort the heights from west to east
    sorted_heights = sorted(heights, reverse=True)
    # Initialize a counter for the number of visible inns
    visible_inns = 0
    # Iterate through the heights from west to east
    for i in range(len(heights)):
        # Check if the current height is greater than or equal to the previous heights
        if sorted_heights[i] >= sorted_heights[i-1]:
            visible_inns += 1
    return visible_inns

