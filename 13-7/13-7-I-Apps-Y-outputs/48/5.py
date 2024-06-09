
def can_construct_square(n, m, tiles):
    # Check if the input is valid
    if n < 1 or n > 100:
        return "NO"
    if m < 1 or m > 100:
        return "NO"
    if len(tiles) != 2 * n:
        return "NO"

    # Initialize a 2D array to store the tiles
    grid = [[0 for _ in range(m)] for _ in range(m)]

    # Loop through each tile type
    for i in range(n):
        # Get the current tile type
        tile_type = tiles[2 * i]
        tile_rotated = tiles[2 * i + 1]

        # Check if the tile type is valid
        if tile_type[0] < 1 or tile_type[0] > 100:
            return "NO"
        if tile_type[1] < 1 or tile_type[1] > 100:
            return "NO"
        if tile_rotated[0] < 1 or tile_rotated[0] > 100:
            return "NO"
        if tile_rotated[1] < 1 or tile_rotated[1] > 100:
            return "NO"

        # Check if the tile type is already used
        if tile_type in grid or tile_rotated in grid:
            return "NO"

        # Add the tile type to the grid
        grid.append(tile_type)
        grid.append(tile_rotated)

    # Check if the grid is symmetric
    for i in range(m):
        for j in range(i + 1, m):
            if grid[i][j] != grid[j][i]:
                return "NO"

    # Check if the grid is filled
    for i in range(m):
        for j in range(m):
            if grid[i][j] == 0:
                return "NO"

    # If all checks pass, return "YES"
    return "YES"

