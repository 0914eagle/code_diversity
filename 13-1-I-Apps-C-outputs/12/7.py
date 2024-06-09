
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
            if matching_bottom_right in matching:
                # If it is, check if the matching top-left corner is the current top-left corner
                if matching[matching_bottom_right] == top_left:
                    # If it is, remove the matching for the current top-left and bottom-right corners
                    del matching[top_left]
                    del matching[matching_bottom_right]
                else:
                    # If it is not, the matching is invalid
                    return "syntax error"
            else:
                # If the bottom-right corner is not matched, the matching is invalid
                return "syntax error"
        else:
            # If the top-left corner is not matched, match it with the current bottom-right corner
            matching[top_left] = bottom_right

    # Check if all corners are matched
    if len(matching) == n:
        # If they are, return the matching
        return matching
    else:
        # If they are not, the matching is invalid
        return "syntax error"

