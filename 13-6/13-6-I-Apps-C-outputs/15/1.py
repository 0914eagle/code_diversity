
def solve(R, C, K, grid, scores):
    # Initialize the maximum score to 0
    max_score = 0
    
    # Loop through each possible direction for the conveyor belts
    for direction in ["R", "L"]:
        # Set the direction for the first row
        grid[0] = grid[0].replace("?", direction)
        
        # Initialize the current score to 0
        current_score = 0
        
        # Initialize the current position to (0, 0)
        current_position = (0, 0)
        
        # Loop through each row in the grid
        for i in range(R):
            # Loop through each cell in the current row
            for j in range(C):
                # If the cell is empty, move the ball to the next cell
                if grid[i][j] == ".":
                    current_position = (current_position[0], current_position[1] + 1)
                
                # If the cell is an obstacle, end the game
                elif grid[i][j] == "X":
                    break
                
                # If the cell is a conveyor belt, move the ball according to the direction
                elif grid[i][j] == "R" or grid[i][j] == "L":
                    if grid[i][j] == direction:
                        current_position = (current_position[0], current_position[1] + 1)
                    else:
                        current_position = (current_position[0], current_position[1] - 1)
                
                # If the cell is a point, add the score to the current score
                elif grid[i][j].isdigit():
                    current_score += int(grid[i][j])
                    
                # If the ball goes outside of the grid or hits an obstacle, end the game
                if current_position[0] < 0 or current_position[0] >= R or current_position[1] < 0 or current_position[1] >= C or grid[current_position[0]][current_position[1]] == "X":
                    break
                    
            # If the ball goes outside of the grid or hits an obstacle, end the game
            if current_position[0] < 0 or current_position[0] >= R or current_position[1] < 0 or current_position[1] >= C or grid[current_position[0]][current_position[1]] == "X":
                break
                
        # If the current score is higher than the maximum score, update the maximum score
        if current_score > max_score:
            max_score = current_score
    
    # Return the maximum score
    return max_score

