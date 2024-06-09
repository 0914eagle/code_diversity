
def solve(n, corners):
    # Initialize an empty dictionary to store the matching between top-left and bottom-right corners
    match = {}
    
    # Iterate over the input corners
    for i in range(n):
        # Get the current top-left and bottom-right corners
        top_left, bottom_right = corners[i]
        
        # Check if the current top-left corner is already matched
        if top_left in match:
            # If it is matched, check if the current bottom-right corner is compatible with the matched top-left corner
            if match[top_left] == bottom_right:
                # If they are compatible, continue to the next corner
                continue
            else:
                # If they are not compatible, return "syntax error"
                return "syntax error"
        else:
            # If the current top-left corner is not matched, check if the current bottom-right corner is already matched
            if bottom_right in match:
                # If it is matched, return "syntax error"
                return "syntax error"
            else:
                # If neither the current top-left nor bottom-right corner is matched, match them together
                match[top_left] = bottom_right
    
    # If all corners are matched, return the matching in the required format
    return [match[top_left] for top_left in sorted(match)]

