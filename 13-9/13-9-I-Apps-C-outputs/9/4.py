
def get_maximum_score(R, C, K, grid, conveyor_belts, scores):
    # Initialize the maximum score to 0
    maximum_score = 0
    
    # Loop through each possible conveyor belt setting
    for conveyor_belt in range(4):
        # Set the conveyor belt for the first row
        set_conveyor_belt(conveyor_belt, 0, grid, conveyor_belts)
        
        # Loop through each possible column for the initial ball position
        for column in range(C):
            # Set the initial ball position
            set_ball_position(column, 0, grid)
            
            # Calculate the maximum score for this configuration
            score = calculate_maximum_score(R, C, K, grid, conveyor_belts, scores)
            
            # Update the maximum score if necessary
            if score > maximum_score:
                maximum_score = score
    
    # Return the maximum score
    return maximum_score

def set_conveyor_belt(conveyor_belt, row, grid, conveyor_belts):
    # Set the conveyor belt for the given row
    conveyor_belts[row] = conveyor_belt
    
    # Update the grid with the new conveyor belt setting
    for column in range(len(grid[0])):
        if grid[row][column] == '?':
            grid[row][column] = 'R' if conveyor_belt == 0 else 'L'

def set_ball_position(column, row, grid):
    # Set the ball position for the given column and row
    grid[row][column] = 'B'

def calculate_maximum_score(R, C, K, grid, conveyor_belts, scores):
    # Initialize the maximum score to 0
    maximum_score = 0
    
    # Loop through each part of the grid
    for part in range(K):
        # Loop through each row in the part
        for row in range(R+1):
            # If the ball lands on a point, add the score to the maximum score
            if grid[row][-1] == 'P':
                maximum_score += scores[row]
            
            # If the ball falls off the grid or lands on an obstacle, return the maximum score
            if row == R or grid[row][-1] == 'X':
                return maximum_score
            
            # If the ball lands on a conveyor belt, move it in the appropriate direction
            if grid[row][-1] == 'R':
                move_ball('L', grid)
            elif grid[row][-1] == 'L':
                move_ball('R', grid)
    
    # Return the maximum score
    return maximum_score

def move_ball(direction, grid):
    # Move the ball in the appropriate direction
    for row in range(len(grid)):
        if grid[row][-1] == 'B':
            if direction == 'L':
                grid[row][-1] = '.'
                grid[row][-2] = 'B'
            elif direction == 'R':
                grid[row][-1] = '.'
                grid[row][-2] = 'B'
            break

def main():
    # Read the input
    R, C, K = map(int, input().split())
    grid = [input() for _ in range(R)]
    conveyor_belts = [0] * R
    scores = list(map(int, input().split()))
    
    # Get the maximum score
    maximum_score = get_maximum_score(R, C, K, grid, conveyor_belts, scores)
    
    # Print the maximum score
    print(maximum_score)

if __name__ == '__main__':
    main()

