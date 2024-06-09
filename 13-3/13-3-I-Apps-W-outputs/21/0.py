
def get_max_side_length(planks):
    # Sort the planks in non-decreasing order
    planks.sort()
    # Initialize the maximum side length as 0
    max_side_length = 0
    # Iterate over the planks
    for i in range(len(planks)):
        # Check if the current plank is greater than or equal to the maximum side length
        if planks[i] >= max_side_length:
            # If yes, then update the maximum side length
            max_side_length = planks[i]
            # Break the loop as we have found the maximum side length
            break
    return max_side_length

