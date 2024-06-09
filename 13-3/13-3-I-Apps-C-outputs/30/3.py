
def solve(n, corners):
    # Initialize an empty dictionary to store the matching between top-left and bottom-right corners
    matching = {}

    # Iterate through the list of corner pairs
    for i in range(n):
        # Get the top-left and bottom-right corners for the current pair
        top_left, bottom_right = corners[i]

        # Check if the top-left corner is already matched
        if top_left in matching:
            # If it is matched, check if the bottom-right corner is the matching top-left corner
            if matching[top_left] == bottom_right:
                # If it is, remove the matching from the dictionary
                del matching[top_left]
            else:
                # If it's not, the input is invalid and we return "syntax error"
                return "syntax error"
        else:
            # If the top-left corner is not matched, add it to the dictionary with the bottom-right corner as its value
            matching[top_left] = bottom_right

    # If we reach this point, all corners have been matched, so we return the matching as the output
    return matching

