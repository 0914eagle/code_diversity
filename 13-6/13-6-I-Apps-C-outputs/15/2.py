
def solve(R, C, K, grid, scores):
    # Initialize the maximum score to 0
    max_score = 0
    
    # Loop through each possible direction for the conveyor belt
    for direction in ['R', 'L']:
        # Set the conveyor belt in the first row to the current direction
        grid[0] = [direction] * C
        
        # Loop through each possible column for the initial position of the ball
        for col in range(C):
            # Set the initial position of the ball to the current column
            ball_pos = (0, col)
            
            # Initialize the current score to 0
            current_score = 0
            
            # Loop through each row of the grid
            for row in range(1, R):
                # If the current cell is empty, move the ball down one row
                if grid[row][col] == '.':
                    ball_pos = (row, col)
                
                # If the current cell is an obstacle, end the game
                elif grid[row][col] == 'X':
                    break
                
                # If the current cell is a conveyor belt, move the ball to the left or right based on the direction of the belt
                elif grid[row][col] == 'R':
                    ball_pos = (row, col + 1)
                elif grid[row][col] == 'L':
                    ball_pos = (row, col - 1)
                
                # If the ball has fallen off the grid or landed on an obstacle, end the game
                if ball_pos[0] == R or grid[ball_pos[0]][ball_pos[1]] == 'X':
                    break
                
                # If the ball has landed on a cell with a score, add the score to the current score
                if grid[ball_pos[0]][ball_pos[1]] == '.':
                    current_score += scores[ball_pos[1]]
                    
            # If the game has not ended and the current score is higher than the maximum score, update the maximum score
            if ball_pos[0] < R and grid[ball_pos[0]][ball_pos[1]] != 'X' and current_score > max_score:
                max_score = current_score
    
    # Return the maximum score
    return max_score

