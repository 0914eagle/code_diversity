
def get_max_lighted_squares(grid):
    # Initialize the maximum number of lighted squares
    max_lighted_squares = 0

    # Loop through each row of the grid
    for i in range(len(grid)):
        # Loop through each column of the grid
        for j in range(len(grid[0])):
            # Check if the current square is not an obstacle
            if grid[i][j] == ".":
                # Count the number of lighted squares in all four directions
                num_lighted_squares = count_lighted_squares(grid, i, j)

                # Update the maximum number of lighted squares
                max_lighted_squares = max(max_lighted_squares, num_lighted_squares)

    # Return the maximum number of lighted squares
    return max_lighted_squares

# Count the number of lighted squares in all four directions
def count_lighted_squares(grid, i, j):
    # Initialize the number of lighted squares
    num_lighted_squares = 0

    # Loop through each direction
    for direction in ["up", "down", "left", "right"]:
        # Count the number of lighted squares in the current direction
        num_lighted_squares += count_lighted_squares_in_direction(grid, i, j, direction)

    # Return the number of lighted squares
    return num_lighted_squares

# Count the number of lighted squares in a specific direction
def count_lighted_squares_in_direction(grid, i, j, direction):
    # Initialize the number of lighted squares
    num_lighted_squares = 0

    # Loop through the grid in the current direction
    while True:
        # Check if the current square is not an obstacle
        if grid[i][j] == ".":
            # Increment the number of lighted squares
            num_lighted_squares += 1

        # Check if the current square is the starting square
        if i == i_start and j == j_start:
            # Break out of the loop
            break

        # Update the current square's coordinates based on the direction
        if direction == "up":
            i -= 1
        elif direction == "down":
            i += 1
        elif direction == "left":
            j -= 1
        elif direction == "right":
            j += 1

    # Return the number of lighted squares
    return num_lighted_squares

# Test the function
grid = [
    ["#", ".", ".", ".", ".", "."],
    [".", ".", ".", ".", ".", "."],
    [".", ".", ".", ".", ".", "."],
    [".", ".", ".", ".", ".", "."],
    [".", ".", ".", ".", ".", "."],
]
print(get_max_lighted_squares(grid))

