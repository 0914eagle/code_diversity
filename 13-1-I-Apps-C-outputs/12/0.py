
def solve(n, corners):
    # Initialize an empty dictionary to store the matching between top-left and bottom-right corners
    match = {}
    
    # Iterate over the corner pairs
    for i in range(n):
        # Get the top-left and bottom-right corners for the current pair
        top_left, bottom_right = corners[i]
        
        # Check if the top-left corner is already matched
        if top_left in match:
            # If it is matched, check if the bottom-right corner is the matching top-left corner
            if match[top_left] == bottom_right:
                # If it is, remove the matching from the dictionary
                del match[top_left]
            else:
                # If it is not, the input is invalid and we return "syntax error"
                return "syntax error"
        else:
            # If the top-left corner is not matched, add it to the dictionary with the bottom-right corner as its value
            match[top_left] = bottom_right
    
    # Check if all corners are matched
    if len(match) == n:
        # If they are, return the matching as the output
        return match
    else:
        # If they are not, the input is invalid and we return "syntax error"
        return "syntax error"

