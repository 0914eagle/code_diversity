
def solve(n, corners):
    # Initialize an empty dictionary to store the matching between top-left and bottom-right corners
    matching = {}
    
    # Iterate over the corner pairs
    for i in range(n):
        # Get the top-left and bottom-right corners for the current pair
        top_left, bottom_right = corners[i]
        
        # Check if the top-left corner is already matched
        if top_left in matching:
            # If it is matched, check if the bottom-right corner is compatible with the matched top-left corner
            if matching[top_left] != bottom_right:
                # If they are not compatible, return "syntax error"
                return "syntax error"
        else:
            # If the top-left corner is not matched, check if the bottom-right corner is already matched
            if bottom_right in matching:
                # If it is matched, return "syntax error"
                return "syntax error"
            else:
                # If neither corner is matched, match them together
                matching[top_left] = bottom_right
    
    # If we reach this point, all corners have been matched successfully
    return matching

