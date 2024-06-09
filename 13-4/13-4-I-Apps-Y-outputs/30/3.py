
def solve_2048(grid, move):
    # Convert the grid to a list of lists
    grid = [list(map(int, row)) for row in grid.split()]
    # Get the number of rows and columns
    n = len(grid)
    # Define the directions
    directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    # Define the move function
    def move_tiles(grid, direction):
        # Loop through the rows
        for i in range(n):
            # Loop through the columns
            for j in range(n):
                # Check if the current tile is not zero
                if grid[i][j] != 0:
                    # Check if the tile can move in the current direction
                    if j + direction[1] < n and grid[i][j + direction[1]] == 0:
                        # Move the tile to the empty space
                        grid[i][j + direction[1]] = grid[i][j]
                        grid[i][j] = 0
                    elif i + direction[0] < n and grid[i + direction[0]][j] == 0:
                        # Move the tile to the empty space
                        grid[i + direction[0]][j] = grid[i][j]
                        grid[i][j] = 0
        return grid
    # Make the move
    grid = move_tiles(grid, directions[move])
    # Merge the tiles
    for i in range(n):
        for j in range(n):
            if grid[i][j] != 0 and grid[i][j] == grid[i][j + 1]:
                grid[i][j] *= 2
                grid[i][j + 1] = 0
            if grid[i][j] != 0 and grid[i][j] == grid[i + 1][j]:
                grid[i][j] *= 2
                grid[i + 1][j] = 0
    # Return the grid
    return grid

