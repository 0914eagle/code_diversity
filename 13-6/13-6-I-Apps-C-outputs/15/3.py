
def solve(R, C, K, grid, scores):
    # Initialize the maximum score to 0
    max_score = 0
    
    # Loop through each possible combination of conveyor belt directions
    for r in range(2**R):
        # Convert the binary representation of r to a list of 0s and 1s
        directions = [int(x) for x in bin(r)[2:].zfill(R)]
        
        # Initialize the current score to 0
        current_score = 0
        
        # Loop through each row of the grid
        for i in range(R):
            # Loop through each column of the grid
            for j in range(C):
                # If the current cell is a conveyor belt, set its direction based on the ith bit of r
                if grid[i][j] == '?':
                    grid[i][j] = 'R' if directions[i] == 1 else 'L'
                
                # If the current cell is an obstacle, the game ends
                if grid[i][j] == 'X':
                    break
                
                # If the current cell is a point cell, add its score to the current score
                if grid[i][j] == '.':
                    current_score += scores[j]
                    
                # If the current cell is a point cell and it is in the last row, add its score to the maximum score
                if grid[i][j] == '.' and i == R-1:
                    max_score = max(max_score, current_score)
                    
    # Return the maximum score
    return max_score

