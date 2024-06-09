
def solve(N, grid):
    # Initialize the number of moves as 0
    num_moves = 0

    # Loop through each row of the grid
    for i in range(N):
        # Loop through each column of the grid
        for j in range(N):
            # Check if the current cell is a dot
            if grid[i][j] == "*":
                # Check if the dot is connected to the top dot
                if i > 0 and grid[i-1][j] == "|":
                    # Increment the number of moves
                    num_moves += 1
                # Check if the dot is connected to the left dot
                if j > 0 and grid[i][j-1] == "-":
                    # Increment the number of moves
                    num_moves += 1

    # Return the number of moves
    return num_moves

