
def can_construct_symmetric_square(n, m, tiles):
    # Check if the number of tiles is valid
    if len(tiles) != n:
        return "NO"

    # Check if the square size is valid
    if m % 2 == 0 or m > 100:
        return "NO"

    # Initialize a set to store the tiles that have been used
    used_tiles = set()

    # Iterate through the tiles and check if they can be used to construct the square
    for tile in tiles:
        # Check if the tile has already been used
        if tile in used_tiles:
            return "NO"

        # Check if the tile is valid
        if tile[0] > m or tile[1] > m:
            return "NO"

        # Check if the tile is symmetric
        if tile[0] != tile[1]:
            return "NO"

        # Add the tile to the set of used tiles
        used_tiles.add(tile)

    # Check if all tiles have been used
    if len(used_tiles) != n:
        return "NO"

    # Check if the square is symmetric
    for i in range(m):
        for j in range(i+1, m):
            if tiles[i][0] != tiles[j][1] or tiles[i][1] != tiles[j][0]:
                return "NO"

    # If all checks pass, return "YES"
    return "YES"

