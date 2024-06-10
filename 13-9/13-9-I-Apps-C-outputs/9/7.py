
def get_max_score(grid, conveyor_belts, points):
    # Initialize the maximum score to 0
    max_score = 0
    
    # Loop through each possible direction for the conveyor belts
    for right_direction in [True, False]:
        for left_direction in [True, False]:
            # Set the directions for the conveyor belts
            conveyor_belts[0] = ('R' if right_direction else 'L')
            conveyor_belts[1] = ('R' if left_direction else 'L')
            
            # Initialize the current score to 0
            current_score = 0
            
            # Loop through each row of the grid
            for row in range(len(grid)):
                # Loop through each column of the current row
                for col in range(len(grid[row])):
                    # If the current cell is not an obstacle
                    if grid[row][col] != 'X':
                        # If the current cell is a conveyor belt
                        if grid[row][col] in ['R', 'L']:
                            # Send the ball to the left or right based on the direction of the conveyor belt
                            col += 1 if grid[row][col] == 'R' else -1
                        
                        # If the current cell is a cell with points
                        if grid[row][col] in ['R', 'L'] or grid[row][col] == '.':
                            # Add the points to the current score
                            current_score += points[col]
                        
                        # If the ball goes out of bounds or lands on an obstacle
                        if col < 0 or col >= len(grid[row]) or grid[row][col] == 'X':
                            # Break out of the loop
                            break
            
            # If the current score is greater than the maximum score
            if current_score > max_score:
                # Update the maximum score
                max_score = current_score
    
    # Return the maximum score
    return max_score

def main():
    # Read the input
    R, C, K = map(int, input().split())
    grid = [input() for _ in range(R)]
    conveyor_belts = [None] * K
    points = list(map(int, input().split()))
    
    # Get the maximum score
    max_score = get_max_score(grid, conveyor_belts, points)
    
    # Print the maximum score
    print(max_score)

if __name__ == '__main__':
    main()

