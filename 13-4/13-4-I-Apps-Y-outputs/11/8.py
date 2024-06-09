
def can_construct_square(n, m, tiles):
    # Check if the input is valid
    if n < 1 or n > 100:
        return "NO"
    if m < 1 or m > 100:
        return "NO"
    if len(tiles) != 2 * n:
        return "NO"

    # Initialize a set to store the tiles that have already been used
    used_tiles = set()

    # Loop through each tile type
    for i in range(n):
        # Get the current tile type
        tile = tiles[2 * i] + tiles[2 * i + 1]

        # Check if the tile has already been used
        if tile in used_tiles:
            return "NO"

        # Add the tile to the set of used tiles
        used_tiles.add(tile)

    # Check if the square can be constructed
    if len(used_tiles) == n:
        return "YES"
    else:
        return "NO"

