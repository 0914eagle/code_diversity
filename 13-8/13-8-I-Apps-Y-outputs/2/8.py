
def dance_rating(grid):
    # Initialize variables
    rating = 0
    moves = []

    # Loop through the grid
    for i in range(len(grid)):
        # Check if the current row is a move
        if grid[i].count("$") > 0:
            # Add the move to the list of moves
            moves.append(i)

    # Return the number of moves
    return len(moves)

