
def get_max_lighted_squares(grid):
    # Initialize a variable to store the maximum number of lighted squares
    max_lighted_squares = 0
    
    # Loop through each row of the grid
    for i in range(len(grid)):
        # Loop through each column of the current row
        for j in range(len(grid[i])):
            # If the current square is not an obstacle
            if grid[i][j] == '.':
                # Count the number of lighted squares in all four directions
                num_lighted_squares = count_lighted_squares(grid, i, j)
                # Update the maximum number of lighted squares if necessary
                max_lighted_squares = max(max_lighted_squares, num_lighted_squares)
    
    # Return the maximum number of lighted squares
    return max_lighted_squares

# Count the number of lighted squares in all four directions
def count_lighted_squares(grid, i, j):
    # Initialize a variable to store the number of lighted squares
    num_lighted_squares = 0
    
    # Loop through each direction
    for direction in ['up', 'down', 'left', 'right']:
        # Count the number of lighted squares in the current direction
        num_lighted_squares += count_lighted_squares_in_direction(grid, i, j, direction)
    
    # Return the number of lighted squares
    return num_lighted_squares

# Count the number of lighted squares in a specific direction
def count_lighted_squares_in_direction(grid, i, j, direction):
    # Initialize a variable to store the number of lighted squares
    num_lighted_squares = 0
    
    # Loop through each square in the current direction
    while True:
        # If the current square is an obstacle or it is out of bounds, break the loop
        if grid[i][j] == '#' or i < 0 or j < 0 or i >= len(grid) or j >= len(grid[0]):
            break
        # If the current square is not an obstacle, increment the number of lighted squares
        if grid[i][j] == '.':
            num_lighted_squares += 1
        # Move to the next square in the current direction
        if direction == 'up':
            i -= 1
        elif direction == 'down':
            i += 1
        elif direction == 'left':
            j -= 1
        else:
            j += 1
    
    # Return the number of lighted squares
    return num_lighted_squares

# Test the function with a sample grid
grid = [
    '#..#..',
    '.....#',
    '....#.',
    '#.#...'
]
print(get_max_lighted_squares(grid)) # should print 8

