
def solve_2048(grid, move):
    # Convert the grid to a list of lists
    grid = [list(map(int, row)) for row in grid.split()]
    # Get the number of rows and columns
    n = len(grid)
    # Define the possible moves
    moves = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    # Get the move index
    move = moves[move]
    # Initialize the new grid
    new_grid = [[0] * n for _ in range(n)]
    # Loop through the rows and columns
    for i in range(n):
        for j in range(n):
            # Get the current cell value
            value = grid[i][j]
            # Check if the cell is not empty
            if value != 0:
                # Get the new row and column indices
                new_i = i + move[0]
                new_j = j + move[1]
                # Check if the new cell is empty
                if new_grid[new_i][new_j] == 0:
                    # Move the cell to the new location
                    new_grid[new_i][new_j] = value
                else:
                    # Merge the cells
                    new_grid[new_i][new_j] += value
                    value = 0
            # Set the current cell value to zero
            grid[i][j] = value
    # Return the new grid
    return new_grid

