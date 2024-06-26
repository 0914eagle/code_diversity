
def get_maximum_score(grid):
    
    # Initialize the maximum score to 0
    max_score = 0
    
    # Iterate over each part of the grid
    for part in grid:
        # Initialize the current score to 0
        current_score = 0
        
        # Iterate over each row in the part
        for row in part:
            # If the current row is the last row, add the score to the current score
            if row == "R" or row == "L":
                current_score += 1
            # If the current row is an obstacle, break the loop
            elif row == "X":
                break
        
        # If the current score is greater than the maximum score, update the maximum score
        if current_score > max_score:
            max_score = current_score
    
    # Return the maximum score
    return max_score

