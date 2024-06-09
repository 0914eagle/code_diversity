
def can_construct_square(n, m, tiles):
    # Check if the input is valid
    if n < 1 or n > 100:
        return "NO"
    if m < 1 or m > 100:
        return "NO"
    if len(tiles) != 2 * n:
        return "NO"

    # Initialize a set to store the unique tiles
    unique_tiles = set()

    # Iterate over the tiles and add them to the set
    for i in range(n):
        for j in range(i, n):
            if tiles[2 * i] != tiles[2 * j] or tiles[2 * i + 1] != tiles[2 * j + 1]:
                return "NO"
            unique_tiles.add((tiles[2 * i], tiles[2 * i + 1]))

    # Check if the square can be constructed
    if len(unique_tiles) == n:
        return "YES"
    else:
        return "NO"

