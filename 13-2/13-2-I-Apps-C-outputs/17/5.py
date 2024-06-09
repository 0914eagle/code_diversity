
def get_maximum_score(grid):
    # Initialize the maximum score to 0
    max_score = 0
    
    # Loop through each part of the grid
    for part in grid:
        # Initialize the current score to 0
        current_score = 0
        
        # Loop through each row in the part
        for row in part:
            # If the current row is the last row, add the score to the current score
            if row == "R":
                current_score += 1
        
        # Add the current score to the maximum score
        max_score += current_score
    
    # Return the maximum score
    return max_score

