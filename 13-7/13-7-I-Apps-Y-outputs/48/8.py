
def can_construct_symmetric_square(n, m, tile_types):
    # Check if the input is valid
    if n < 1 or n > 100:
        return "NO"
    if m < 1 or m > 100:
        return "NO"
    if len(tile_types) != 2 * n:
        return "NO"

    # Initialize a set to store the unique tile types
    unique_tiles = set()

    # Iterate over the tile types and add them to the set
    for i in range(n):
        top_left, top_right = tile_types[2 * i]
        bottom_left, bottom_right = tile_types[2 * i + 1]
        if top_left < 1 or top_left > 100:
            return "NO"
        if top_right < 1 or top_right > 100:
            return "NO"
        if bottom_left < 1 or bottom_left > 100:
            return "NO"
        if bottom_right < 1 or bottom_right > 100:
            return "NO"
        unique_tiles.add((top_left, top_right, bottom_left, bottom_right))

    # Check if the square can be constructed
    if len(unique_tiles) < m:
        return "NO"

    return "YES"

