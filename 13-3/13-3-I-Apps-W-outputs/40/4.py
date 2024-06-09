
def get_max_lighted_squares(grid):
    # Initialize the maximum number of lighted squares
    max_lighted_squares = 0
    
    # Loop through each row of the grid
    for row in range(len(grid)):
        # Loop through each column of the grid
        for col in range(len(grid[0])):
            # Check if the current square is not an obstacle
            if grid[row][col] == ".":
                # Count the number of lighted squares in all four directions
                num_lighted_squares = count_lighted_squares(grid, row, col)
                # Update the maximum number of lighted squares
                max_lighted_squares = max(max_lighted_squares, num_lighted_squares)
    
    # Return the maximum number of lighted squares
    return max_lighted_squares

# Count the number of lighted squares in all four directions
def count_lighted_squares(grid, row, col):
    # Initialize the number of lighted squares
    num_lighted_squares = 0
    
    # Loop through each direction
    for direction in ["up", "down", "left", "right"]:
        # Count the number of lighted squares in the current direction
        num_lighted_squares += count_lighted_squares_in_direction(grid, row, col, direction)
    
    # Return the number of lighted squares
    return num_lighted_squares

# Count the number of lighted squares in a specific direction
def count_lighted_squares_in_direction(grid, row, col, direction):
    # Initialize the number of lighted squares
    num_lighted_squares = 0
    
    # Loop through the squares in the current direction
    while True:
        # Check if the current square is not an obstacle
        if grid[row][col] == ".":
            # Increment the number of lighted squares
            num_lighted_squares += 1
        
        # Move to the next square in the current direction
        if direction == "up":
            row -= 1
        elif direction == "down":
            row += 1
        elif direction == "left":
            col -= 1
        else:
            col += 1
        
        # Check if the current square is out of bounds or an obstacle
        if row < 0 or col < 0 or row == len(grid) or col == len(grid[0]) or grid[row][col] == "#":
            break
    
    # Return the number of lighted squares
    return num_lighted_squares

# Test the function with a sample grid
grid = [
    "###..#..",
    ".....#..",
    "....#...",
    "##.#...."
]
print(get_max_lighted_squares(grid)) # should print 8

