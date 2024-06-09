
def solve(grid):
    # Initialize the maximum score to 0
    max_score = 0
    # Loop through each row of the grid
    for i in range(len(grid)):
        # Loop through each column of the grid
        for j in range(len(grid[0])):
            # If the current square is white and not at the starting or ending square
            if grid[i][j] == "." and (i, j) != (0, 0) and (i, j) != (len(grid) - 1, len(grid[0]) - 1):
                # Change the color of the current square to black
                grid[i][j] = "#"
                # Update the maximum score
                max_score += 1
    # Return the maximum score
    return max_score

