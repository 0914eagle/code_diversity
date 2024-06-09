
def solve(n, corners):
    # Initialize an empty dictionary to store the mapping of top-left corners to bottom-right corners
    corner_map = {}

    # Iterate over the list of corner pairs
    for i in range(0, len(corners), 2):
        # Get the top-left and bottom-right corners for the current pair
        top_left, bottom_right = corners[i], corners[i+1]

        # Check if the top-left corner is already in the dictionary
        if top_left in corner_map:
            # If it is, check if the current bottom-right corner is compatible with the existing mapping
            if corner_map[top_left] != bottom_right:
                # If it's not, return "syntax error"
                return "syntax error"
        else:
            # If the top-left corner is not in the dictionary, add it to the dictionary with the current bottom-right corner
            corner_map[top_left] = bottom_right

    # If we reach this point, all corners have been processed and the dictionary contains a valid mapping
    # Return the mapping as a list of pairs
    return [top_left, bottom_right for top_left, bottom_right in corner_map.items()]

