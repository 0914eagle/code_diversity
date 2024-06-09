
def get_visible_inns(heights):
    # Initialize a variable to store the number of visible inns
    visible_inns = 0

    # Iterate through the list of heights
    for i in range(len(heights)):
        # Check if the current height is greater than or equal to the height of the previous inn
        if i == 0 or heights[i] >= heights[i-1]:
            # If it is, increment the number of visible inns
            visible_inns += 1

    # Return the number of visible inns
    return visible_inns

