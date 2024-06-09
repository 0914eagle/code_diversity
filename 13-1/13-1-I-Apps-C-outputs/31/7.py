
def get_maximum_score(grid):
    
    # Initialize the maximum score to 0
    max_score = 0
    
    # Iterate through each part of the grid
    for part in grid:
        # Initialize the current score to 0
        current_score = 0
        
        # Iterate through each row of the part
        for row in part:
            # Iterate through each cell in the row
            for cell in row:
                # If the cell is a cell with points, add its score to the current score
                if cell == "X":
                    current_score += 100
                # If the cell is a conveyor belt, set its direction to right or left based on the current score
                elif cell == "?":
                    if current_score % 2 == 0:
                        cell = "R"
                    else:
                        cell = "L"
                # If the cell is an obstacle, the exam ends, so break the loop
                elif cell == "X":
                    break
            # If the ball falls through the last row of the part, add the current score to the maximum score and break the loop
            if row == part[-1]:
                max_score += current_score
                break
    
    # Return the maximum score
    return max_score

