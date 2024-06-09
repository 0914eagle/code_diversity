
def get_max_side_length(planks):
    # Sort the planks in non-decreasing order
    planks.sort()
    # Initialize the maximum side length to 0
    max_side_length = 0
    # Iterate through the planks
    for i in range(len(planks)):
        # Check if the current plank is greater than the maximum side length
        if planks[i] > max_side_length:
            # If it is, set the maximum side length to the current plank
            max_side_length = planks[i]
    return max_side_length

