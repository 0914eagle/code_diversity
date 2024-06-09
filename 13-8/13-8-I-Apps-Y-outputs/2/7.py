
def solve(grid):
    # Initialize variables
    N, M = len(grid), len(grid[0])
    moves = 0

    # Iterate over each column
    for j in range(M):
        # If the current column is blank, skip it
        if grid[0][j] == "_":
            continue
        # If the current column is not blank, check if the previous column is also not blank
        if j > 0 and grid[0][j-1] == "_":
            # If the previous column is blank, it means we have found a move
            moves += 1

    # Return the number of moves
    return moves

