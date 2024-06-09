
def solve(R, C, K, grid, scores):
    # Initialize the maximum score to 0
    max_score = 0
    
    # Loop through each possible direction for the conveyor belts
    for direction in ["R", "L"]:
        # Set the direction for the conveyor belts
        set_conveyor_belts(grid, direction)
        
        # Initialize the current score to 0
        current_score = 0
        
        # Loop through each column in the grid
        for col in range(C):
            # Drop the ball from the current column
            ball_position = drop_ball(grid, col)
            
            # If the ball falls through the grid or hits an obstacle, break the loop
            if ball_position == -1:
                break
            
            # If the ball lands on a cell with a score, add the score to the current score
            if grid[ball_position[0]][ball_position[1]] != ".":
                current_score += int(grid[ball_position[0]][ball_position[1]])
            
            # Update the grid with the new position of the ball
            grid[ball_position[0]][ball_position[1]] = "."
        
        # If the current score is higher than the maximum score, update the maximum score
        if current_score > max_score:
            max_score = current_score
    
    # Return the maximum score
    return max_score

def set_conveyor_belts(grid, direction):
    # Loop through each row in the grid
    for row in range(len(grid)):
        # Loop through each column in the grid
        for col in range(len(grid[0])):
            # If the cell is a conveyor belt and it has not been set, set it to the given direction
            if grid[row][col] == "?" and grid[row][col-1] != "X":
                grid[row][col] = direction

def drop_ball(grid, col):
    # Initialize the ball's position to the starting column
    ball_position = (0, col)
    
    # Loop through each row in the grid
    for row in range(len(grid)):
        # If the cell is an obstacle, break the loop
        if grid[row][ball_position[1]] == "X":
            break
        
        # If the cell is a conveyor belt, move the ball accordingly
        if grid[row][ball_position[1]] == "R":
            ball_position = (row, ball_position[1] - 1)
        elif grid[row][ball_position[1]] == "L":
            ball_position = (row, ball_position[1] + 1)
        
        # If the ball falls through the grid or hits an obstacle, break the loop
        if ball_position[0] == len(grid) or grid[ball_position[0]][ball_position[1]] == "X":
            break
    
    # Return the ball's position
    return ball_position

