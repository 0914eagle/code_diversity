
def get_max_square_side_length(plank_lengths):
    # Sort the plank lengths in descending order
    plank_lengths.sort(reverse=True)
    
    # Initialize the maximum side length of the square as 0
    max_side_length = 0
    
    # Iterate over the plank lengths
    for i in range(len(plank_lengths)):
        # Check if the current plank length is equal to the maximum side length
        if plank_lengths[i] == max_side_length:
            # If it is, return the maximum side length
            return max_side_length
        # Check if the current plank length is greater than the maximum side length
        elif plank_lengths[i] > max_side_length:
            # If it is, set the maximum side length to the current plank length
            max_side_length = plank_lengths[i]
    
    # If no plank length is equal to the maximum side length, return the maximum side length
    return max_side_length

