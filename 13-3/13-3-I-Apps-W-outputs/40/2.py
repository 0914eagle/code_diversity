
def get_max_lighted_squares(grid):
    # Initialize the maximum number of lighted squares
    max_lighted_squares = 0
    
    # Loop through each square in the grid
    for row in range(len(grid)):
        for col in range(len(grid[0])):
            # Check if the current square is not an obstacle
            if grid[row][col] == '.':
                # Count the number of lighted squares in all four directions
                num_lighted_squares = count_lighted_squares(grid, row, col)
                
                # Update the maximum number of lighted squares
                max_lighted_squares = max(max_lighted_squares, num_lighted_squares)
    
    return max_lighted_squares

# Count the number of lighted squares in all four directions
def count_lighted_squares(grid, row, col):
    # Initialize the number of lighted squares
    num_lighted_squares = 0
    
    # Loop through each direction
    for direction in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
        # Initialize the current row and column
        curr_row = row
        curr_col = col
        
        # Loop until an obstacle or border is reached
        while 0 <= curr_row < len(grid) and 0 <= curr_col < len(grid[0]) and grid[curr_row][curr_col] == '.':
            # Increment the number of lighted squares
            num_lighted_squares += 1
            
            # Update the current row and column
            curr_row += direction[0]
            curr_col += direction[1]
    
    return num_lighted_squares

# Test the function with the sample input
grid = [
    '#..#..',
    '.....#',
    '....#.',
    '#.#...'
]
print(get_max_lighted_squares(grid)) # should print 8

