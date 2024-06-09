
def rate_dance(grid):
    # Initialize variables
    rating = 0
    moves = 0

    # Iterate through the grid
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            # Check if the current position is blank
            if grid[i][j] == "_":
                # Increment the moves count
                moves += 1
            # Check if the current position is the last position in the grid
            if j == len(grid[0]) - 1:
                # Increment the rating by the number of moves
                rating += moves
                # Reset the moves count
                moves = 0

    return rating

