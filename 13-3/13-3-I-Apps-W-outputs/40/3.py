
def get_max_lighted_squares(grid):
    # Initialize a dictionary to store the number of lighted squares for each position
    lighted_squares = {}

    # Loop through each position in the grid
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            # If the current position is not an obstacle
            if grid[i][j] == ".":
                # Get the number of lighted squares for this position
                num_lighted_squares = get_num_lighted_squares(grid, i, j)
                # Update the dictionary with the number of lighted squares for this position
                lighted_squares[(i, j)] = num_lighted_squares

    # Return the maximum number of lighted squares
    return max(lighted_squares.values())

# Function to get the number of lighted squares for a given position
def get_num_lighted_squares(grid, i, j):
    # Initialize a set to store the positions of the lighted squares
    lighted_squares = set()

    # Loop through each direction (up, down, left, and right)
    for direction in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
        # Initialize the current position as the starting position
        current_position = (i, j)
        # Loop until the current position is an obstacle or it reaches the border of the grid
        while current_position in lighted_squares or current_position[0] < 0 or current_position[0] >= len(grid) or current_position[1] < 0 or current_position[1] >= len(grid[0]):
            # If the current position is not an obstacle, add it to the set of lighted squares
            if grid[current_position[0]][current_position[1]] == ".":
                lighted_squares.add(current_position)
            # Update the current position by moving in the current direction
            current_position = (current_position[0] + direction[0], current_position[1] + direction[1])

    # Return the number of lighted squares
    return len(lighted_squares)

