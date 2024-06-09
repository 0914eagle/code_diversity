
def solve_2048(grid, move):
    # Convert the grid to a list of lists
    grid = [list(map(int, row)) for row in grid.split()]
    # Get the number of rows and columns
    n = len(grid)
    # Define the possible moves
    moves = {0: "left", 1: "up", 2: "right", 3: "down"}
    # Get the move as a string
    move = moves[move]
    # Initialize the new grid
    new_grid = [[0] * n for _ in range(n)]
    # Loop through the rows
    for i in range(n):
        # Loop through the columns
        for j in range(n):
            # Get the current cell value
            value = grid[i][j]
            # If the cell is not empty
            if value != 0:
                # Get the new row and column indices
                new_i, new_j = i, j
                # If the move is "left"
                if move == "left":
                    # Move the cell to the left as far as possible
                    while new_j > 0 and grid[i][new_j - 1] == 0:
                        new_j -= 1
                # If the move is "up"
                elif move == "up":
                    # Move the cell up as far as possible
                    while new_i > 0 and grid[new_i - 1][j] == 0:
                        new_i -= 1
                # If the move is "right"
                elif move == "right":
                    # Move the cell to the right as far as possible
                    while new_j < n - 1 and grid[i][new_j + 1] == 0:
                        new_j += 1
                # If the move is "down"
                elif move == "down":
                    # Move the cell down as far as possible
                    while new_i < n - 1 and grid[new_i + 1][j] == 0:
                        new_i += 1
                # If the new cell is not empty
                if grid[new_i][new_j] != 0:
                    # Merge the cells
                    value += grid[new_i][new_j]
                    # Set the new cell value to the merged value
                    grid[new_i][new_j] = value
                    # Set the current cell value to 0
                    grid[i][j] = 0
                # If the new cell is empty
                else:
                    # Set the new cell value to the current cell value
                    grid[new_i][new_j] = value
                    # Set the current cell value to 0
                    grid[i][j] = 0
    # Return the new grid
    return grid

