
def get_visible_inns(heights):
    # Initialize a counter for the number of visible inns
    visible_inns = 0

    # Iterate through the list of heights
    for i in range(len(heights)):
        # Check if the current height is greater than or equal to all previous heights
        if all(heights[j] <= heights[i] for j in range(i)):
            # If it is, increment the counter
            visible_inns += 1

    # Return the number of visible inns
    return visible_inns

