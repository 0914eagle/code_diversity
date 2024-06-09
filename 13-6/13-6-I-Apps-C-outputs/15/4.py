
def solve(R, C, K, grid, scores):
    # Initialize the maximum score to 0
    max_score = 0
    
    # Loop through all possible combinations of conveyor belt directions
    for i in range(2**(R*C)):
        # Convert the binary representation of the combination to a list of directions
        directions = []
        for j in range(R*C):
            if i & (1 << j):
                directions.append('R')
            else:
                directions.append('L')
        
        # Initialize the current score to 0
        current_score = 0
        
        # Loop through each part of the grid
        for k in range(K):
            # Loop through each row in the part
            for r in range(R):
                # Loop through each column in the part
                for c in range(C):
                    # If the current cell is a conveyor belt, set its direction based on the direction list
                    if grid[k][r][c] == '?':
                        grid[k][r][c] = directions[k*R*C + r*C + c]
                    
                    # If the current cell is an obstacle, the exam ends, so break out of the loops
                    if grid[k][r][c] == 'X':
                        break
                
                # If the current row is the last row, add the score to the current score
                if r == R-1:
                    current_score += scores[c]
                
                # If the current cell is an obstacle or the ball goes outside of the grid, the exam ends, so break out of the loops
                if grid[k][r][c] == 'X' or c == C:
                    break
            
            # If the exam ends, break out of the loops
            if grid[k][R-1][C-1] == 'X' or c == C:
                break
        
        # If the current score is greater than the maximum score, update the maximum score
        if current_score > max_score:
            max_score = current_score
    
    # Return the maximum score
    return max_score

