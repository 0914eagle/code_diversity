
def can_construct_symmetric_square(n, m, tiles):
    # Check if the input is valid
    if n < 1 or n > 100:
        return "NO"
    if m < 1 or m > 100:
        return "NO"
    if len(tiles) != 2 * n:
        return "NO"

    # Initialize a set to store the unique tiles
    unique_tiles = set()

    # Iterate over each tile type
    for i in range(n):
        # Check if the tile is valid
        if len(tiles[2 * i]) != 2 or len(tiles[2 * i + 1]) != 2:
            return "NO"
        if not tiles[2 * i].isdigit() or not tiles[2 * i + 1].isdigit():
            return "NO"
        if int(tiles[2 * i]) < 1 or int(tiles[2 * i]) > 100:
            return "NO"
        if int(tiles[2 * i + 1]) < 1 or int(tiles[2 * i + 1]) > 100:
            return "NO"

        # Add the tile to the set of unique tiles
        unique_tiles.add((int(tiles[2 * i]), int(tiles[2 * i + 1])))

    # Check if the square can be constructed
    for i in range(m):
        for j in range(m):
            # Check if the tile at position (i, j) is valid
            if (i, j) not in unique_tiles:
                return "NO"

    # Check if the square is symmetric
    for i in range(m):
        for j in range(i):
            if (i, j) not in unique_tiles or (j, i) not in unique_tiles:
                return "NO"

    # If all conditions are met, return "YES"
    return "YES"

