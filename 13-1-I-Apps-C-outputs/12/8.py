
def solve(n, corners):
    # Initialize an empty dictionary to store the matching
    matching = {}

    # Iterate over the corner pairs
    for i in range(n):
        # Get the current top-left and bottom-right corners
        top_left, bottom_right = corners[i]

        # Check if the top-left corner is already matched
        if top_left in matching:
            # If it is, get the matching bottom-right corner
            matching_bottom_right = matching[top_left]

            # Check if the bottom-right corner is already matched
            if bottom_right in matching:
                # If it is, check if the matching top-left corner is the same as the current top-left corner
                if matching_bottom_right != bottom_right:
                    # If it's not, there is no valid matching, so return "syntax error"
                    return "syntax error"
            else:
                # If the bottom-right corner is not matched, add the current top-left and bottom-right corners to the matching
                matching[top_left] = bottom_right
                matching[bottom_right] = top_left
        else:
            # If the top-left corner is not matched, add the current top-left and bottom-right corners to the matching
            matching[top_left] = bottom_right
            matching[bottom_right] = top_left

    # If we reach this point, we have a valid matching, so return it
    return matching

