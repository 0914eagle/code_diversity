
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
                if grid[i][j] != "X" and i != -1 and j != -1:
                    # Add the score for the current cell to the current score
                    current_score += scores[j]
                
                # If the cell is an obstacle or the ball is outside of the grid, the exam ends
                else:
                    break
                
        # If the current score is greater than the maximum score, update the maximum score
        if current_score > max_score:
            max_score = current_score
    
    # Return the maximum score
    return max_score

def set_conveyor_belts(grid, direction):
    # Loop through each row in the grid
    for i in range(len(grid)):
        # Loop through each cell in the row
        for j in range(len(grid[i])):
            # If the cell is a conveyor belt and it has not been set, set its direction
            if grid[i][j] == "?" and grid[i][j-1] != "X":
                grid[i][j] = direction

def main():
    # Read the input
    R, C, K = map(int, input().split())
    grid = [input() for _ in range(R)]
    scores = list(map(int, input().split()))
    
    # Solve the problem
    max_score = solve(R, C, K, grid, scores)
    
    # Print the output
    print(max_score)

if __name__ == "__main__":
    main()

