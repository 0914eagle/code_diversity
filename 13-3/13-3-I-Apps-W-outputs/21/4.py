
def get_max_square_side_length(planks):
    # Sort the planks in descending order
    planks.sort(reverse=True)
    # Initialize the maximum side length of the square as 0
    max_side_length = 0
    # Iterate through the planks
    for i in range(len(planks)):
        # Check if the current plank is greater than the maximum side length
        if planks[i] > max_side_length:
            # If it is, set the maximum side length to the current plank
            max_side_length = planks[i]
        # Check if the sum of the current plank and the maximum side length is equal to the next plank
        elif planks[i] + max_side_length == planks[i+1]:
            # If it is, set the maximum side length to the sum of the current plank and the maximum side length
            max_side_length += planks[i]
    return max_side_length

