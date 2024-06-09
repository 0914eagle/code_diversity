
def solve(n, corners):
    # Initialize an empty dictionary to store the matching between top-left and bottom-right corners
    matches = {}
    
    # Iterate over the corner pairs
    for i in range(n):
        # Get the top-left and bottom-right corners for the current pair
        top_left, bottom_right = corners[i]
        
        # Check if the top-left corner is already matched
        if top_left in matches:
            # If it is matched, check if the bottom-right corner is the matching top-left corner
            if matches[top_left] == bottom_right:
                # If it is, remove the matching from the dictionary
                del matches[top_left]
            else:
                # If it is not, the input is invalid and we return "syntax error"
                return "syntax error"
        else:
            # If the top-left corner is not matched, add it to the dictionary with the bottom-right corner as its value
            matches[top_left] = bottom_right
    
    # If we reach this point, all corners have been matched, so we return the matching as a list of integers
    return [matches[top_left] for top_left in sorted(matches)]

