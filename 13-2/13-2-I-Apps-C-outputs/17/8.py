
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
                # If the cell is not an obstacle and the ball is not outside of the grid
                if grid[i][j] != "X" and i != R and j != C:
                    # Move the ball to the next cell based on the conveyor belts
                    move_ball(grid, i, j)
                    
                    # If the ball is in the last row of a part
                    if i == R-1:
                        # Add the score for the current cell to the current score
                        current_score += scores[j]
                        
                        # Break out of the loop if the ball goes through 10^20 cells
                        if current_score > 10**20:
                            break
                        
        # Update the maximum score if the current score is higher
        max_score = max(max_score, current_score)
    
    # Return the maximum score
    return max_score

def set_conveyor_belts(grid, direction):
    # Loop through each row in the grid
    for i in range(len(grid)):
        # Loop through each cell in the row
        for j in range(len(grid[i])):
            # If the cell is a conveyor belt and it is not yet set
            if grid[i][j] == "?" and direction != "?":
                # Set the direction of the conveyor belt
                grid[i][j] = direction

def move_ball(grid, i, j):
    # If the ball is in the last row of a part
    if i == R-1:
        # Break out of the loop
        break
    
    # If the cell is not an obstacle and the ball is not outside of the grid
    if grid[i+1][j] != "X" and i+1 != R and j != C:
        # Move the ball to the next cell
        i += 1
    # If the cell is an obstacle or the ball is outside of the grid
    else:
        # Break out of the loop
        break

grid = [
    [".", ".", ".", ".", "."],
    [".", "X", ".", ".", "."],
    [".", ".", ".", ".", "."],
    [".", ".", ".", ".", "."],
    [".", ".", ".", ".", "."]
]
scores = [100, 100, 7, 100, 8]
print(solve(5, 5, 2, grid, scores))

