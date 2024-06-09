
def solve(grid):
    # Convert the grid to a list of lists
    grid = [list(row) for row in grid.split('\n')]
    # Initialize the rating variable
    rating = 0
    # Iterate through the grid
    for i in range(len(grid)):
        # Check if the current row is blank
        if all(char == '_' for char in grid[i]):
            # If it is, increment the rating
            rating += 1
    # Return the rating
    return rating

