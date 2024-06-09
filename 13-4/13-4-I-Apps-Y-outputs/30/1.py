
def solve_2048(grid, direction):
    # Convert the grid to a list of lists
    grid = [list(map(int, row)) for row in grid.split()]

    # Define the directions
    directions = {
        0: (0, 1),
        1: (1, 0),
        2: (0, -1),
        3: (-1, 0)
    }

    # Get the current direction
    dx, dy = directions[direction]

    # Initialize the new grid with the same values as the original grid
    new_grid = [[grid[i][j] for j in range(4)] for i in range(4)]

    # Loop through the grid and move the tiles
    for i in range(4):
        for j in range(4):
            # Check if the current tile is not zero
            if grid[i][j] != 0:
                # Get the current tile's position
                x, y = i, j

                # Loop until the tile reaches the edge of the grid or merges with another tile
                while x >= 0 and x < 4 and y >= 0 and y < 4 and new_grid[x][y] == 0:
                    # Move the tile in the current direction
                    x += dx
                    y += dy

                    # Check if the tile has reached the edge of the grid
                    if x < 0 or x > 3 or y < 0 or y > 3:
                        break

                    # Check if the tile has merged with another tile
                    if new_grid[x][y] == grid[i][j]:
                        new_grid[x][y] *= 2
                        break

                    # Move the tile to its new position
                    new_grid[x][y] = grid[i][j]

    # Return the new grid
    return new_grid

