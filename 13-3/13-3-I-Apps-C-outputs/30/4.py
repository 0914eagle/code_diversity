
def solve(n, corners):
    # Initialize an empty dictionary to store the matching between top-left and bottom-right corners
    match = {}
    
    # Iterate through the list of corners
    for i in range(n):
        # Get the current top-left and bottom-right corners
        top_left, bottom_right = corners[i]
        
        # Check if the top-left corner is already matched
        if top_left in match:
            # If it is, check if the bottom-right corner matches the matched top-left corner
            if match[top_left] == bottom_right:
                # If it does, remove the match from the dictionary
                match.pop(top_left)
            else:
                # If it doesn't, the input is invalid and we return "syntax error"
                return "syntax error"
        else:
            # If the top-left corner is not matched, add it to the dictionary with its bottom-right corner
            match[top_left] = bottom_right
    
    # Check if all corners are matched
    if len(match) == n:
        # If they are, return the matching in the required format
        return [match[top_left] for top_left in sorted(match)]
    else:
        # If they are not, the input is invalid and we return "syntax error"
        return "syntax error"

