
def solve(R, C, K, grid, scores):
    # Initialize the maximum score to 0
    max_score = 0
    
    # Loop through all possible combinations of conveyor belt directions
    for r in range(2**R):
        # Convert the binary representation of r to a list of 0s and 1s
        directions = [int(x) for x in bin(r)[2:].zfill(R)]
        
        # Initialize the current score to 0
        current_score = 0
        
        # Loop through each row of the grid
        for i in range(R):
            # Loop through each column of the grid
            for j in range(C):
                # If the current cell is a conveyor belt and its direction has not been set, set it to the current direction
                if grid[i][j] == '?' and directions[i] != -1:
                    grid[i][j] = 'R' if directions[i] == 0 else 'L'
                
                # If the current cell is a cell with points, add its score to the current score
                if grid[i][j] == '.':
                    current_score += scores[j]
        
        # Add the current score to the maximum score if it is greater than the previous maximum score
        max_score = max(max_score, current_score)
    
    # Return the maximum score
    return max_score

