
def solve(n, corners):
    # Initialize an empty dictionary to store the matching
    matching = {}

    # Iterate over the corner pairs
    for i in range(n):
        # Get the top-left and bottom-right corners for the current pair
        top_left, bottom_right = corners[i]

        # Check if the top-left corner is already matched
        if top_left in matching:
            # If it is, get the matching bottom-right corner
            matching_bottom_right = matching[top_left]

            # Check if the bottom-right corner is already matched
            if bottom_right in matching:
                # If it is, check if the matching top-left corner is the same as the current top-left corner
                if matching_bottom_right == bottom_right:
                    # If it is, the current pair is valid and can be added to the matching
                    matching[top_left] = bottom_right
                else:
                    # If it is not, the current pair is invalid and there is no valid matching
                    return "syntax error"
            else:
                # If the bottom-right corner is not matched, the current pair is invalid and there is no valid matching
                return "syntax error"
        else:
            # If the top-left corner is not matched, check if the bottom-right corner is already matched
            if bottom_right in matching:
                # If it is, the current pair is valid and can be added to the matching
                matching[top_left] = bottom_right
            else:
                # If neither corner is matched, the current pair is valid and can be added to the matching
                matching[top_left] = bottom_right

    # If we reach this point, all pairs are valid and there is a valid matching
    return matching

