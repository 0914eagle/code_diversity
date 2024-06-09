
def solve(R, C, K, grid, scores):
    # Initialize the maximum score to 0
    max_score = 0
    
    # Loop through each possible direction for the conveyor belts
    for direction in ["R", "L"]:
        # Set the direction for the conveyor belts
        set_conveyor_belts(grid, direction)
        
        # Initialize the current score to 0
        current_score = 0
        
        # Loop through each cell in the grid
        for i in range(R):
            for j in range(C):
                # If the cell is an obstacle, the exam ends
                if grid[i][j] == "X":
                    break
                
                # If the cell is a point, add the score to the current score
                if grid[i][j].isdigit():
                    current_score += int(grid[i][j])
                    
                # If the cell is a conveyor belt, move the ball in that direction
                if grid[i][j] == "R" or grid[i][j] == "L":
                    move_ball(i, j, grid)
                    
        # If the current score is greater than the maximum score, update the maximum score
        if current_score > max_score:
            max_score = current_score
    
    # Return the maximum score
    return max_score

# Set the direction for the conveyor belts
def set_conveyor_belts(grid, direction):
    # Loop through each row in the grid
    for i in range(len(grid)):
        # Loop through each cell in the row
        for j in range(len(grid[i])):
            # If the cell is a question mark, set the direction
            if grid[i][j] == "?":
                grid[i][j] = direction

# Move the ball in a certain direction
def move_ball(i, j, grid):
    # If the ball is in the last row, the exam ends
    if i == len(grid) - 1:
        return
    
    # If the cell is a conveyor belt, move the ball in that direction
    if grid[i][j] == "R":
        j += 1
    elif grid[i][j] == "L":
        j -= 1
    
    # If the ball is sent outside of the grid or to an obstacle, the exam ends
    if j < 0 or j >= len(grid[i]) or grid[i][j] == "X":
        return
    
    # Update the ball's position
    grid[i][j] = "B"


