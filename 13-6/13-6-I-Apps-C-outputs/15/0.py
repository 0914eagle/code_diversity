
def solve(R, C, K, grid, scores):
    # Initialize the maximum score to 0
    max_score = 0
    
    # Loop through all possible directions for the conveyor belts
    for direction in ['R', 'L']:
        # Set the direction for the conveyor belts
        set_conveyor_belts(grid, direction)
        
        # Initialize the current score to 0
        current_score = 0
        
        # Initialize the current position of the ball to (0, 0)
        current_position = (0, 0)
        
        # Loop through all possible positions of the ball
        for i in range(10**20):
            # Check if the ball has fallen through the grid or hit an obstacle
            if current_position[0] >= R or current_position[1] >= C or grid[current_position[0]][current_position[1]] == 'X':
                break
            
            # Check if the ball has reached the last row of a part
            if current_position[0] == R - 1:
                # Add the score for the current position to the current score
                current_score += scores[current_position[1]]
                
                # Break out of the loop if the current score is greater than the maximum score
                if current_score > max_score:
                    max_score = current_score
                    break
                
                # Reset the current position to (0, 0) and continue the loop
                current_position = (0, 0)
                continue
            
            # Move the ball to the next position based on the conveyor belt direction
            if direction == 'R':
                current_position = (current_position[0], current_position[1] + 1)
            else:
                current_position = (current_position[0], current_position[1] - 1)
    
    # Return the maximum score
    return max_score

def set_conveyor_belts(grid, direction):
    # Loop through all rows of the grid
    for i in range(len(grid)):
        # Loop through all columns of the grid
        for j in range(len(grid[0])):
            # Check if the current cell is a conveyor belt and not yet set
            if grid[i][j] == '?' and direction == 'R':
                # Set the conveyor belt to right
                grid[i][j] = 'R'
            elif grid[i][j] == '?' and direction == 'L':
                # Set the conveyor belt to left
                grid[i][j] = 'L'

