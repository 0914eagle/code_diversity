
def solve(R, C, K, grid, points):
    # Initialize the maximum score to 0
    max_score = 0
    
    # Loop through all possible combinations of conveyor belts
    for i in range(2**K):
        # Convert the binary representation of i to a list of 0s and 1s
        conveyor_belts = [int(x) for x in bin(i)[2:].zfill(K)]
        
        # Initialize the current score to 0
        current_score = 0
        
        # Loop through each row of the grid
        for r in range(R):
            # Loop through each column of the grid
            for c in range(C):
                # If the current cell is a conveyor belt and it has not been set, set it to the direction indicated by the current bit in the conveyor_belts list
                if grid[r][c] == '?' and conveyor_belts[r]:
                    grid[r][c] = 'R' if conveyor_belts[r] == 1 else 'L'
                
                # If the current cell is a point, add its score to the current score
                if grid[r][c] in '123456789':
                    current_score += int(grid[r][c])
                    
                # If the current cell is an obstacle, break out of the loop
                if grid[r][c] == 'X':
                    break
                    
        # If the current score is greater than the maximum score, update the maximum score
        if current_score > max_score:
            max_score = current_score
    
    # Return the maximum score
    return max_score

