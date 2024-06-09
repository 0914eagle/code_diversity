
def can_construct_symmetric_square(n, m, tiles):
    # Check if the input is valid
    if n < 1 or n > 100:
        return "NO"
    if m < 1 or m > 100:
        return "NO"
    if len(tiles) != 2 * n:
        return "NO"

    # Initialize a set to store the unique tile numbers
    unique_tiles = set()

    # Iterate over the tiles and check if they are valid
    for i in range(n):
        top_left, top_right = tiles[2 * i]
        bottom_left, bottom_right = tiles[2 * i + 1]
        if top_left < 1 or top_left > 100:
            return "NO"
        if top_right < 1 or top_right > 100:
            return "NO"
        if bottom_left < 1 or bottom_left > 100:
            return "NO"
        if bottom_right < 1 or bottom_right > 100:
            return "NO"
        unique_tiles.add(top_left)
        unique_tiles.add(top_right)
        unique_tiles.add(bottom_left)
        unique_tiles.add(bottom_right)

    # Check if the number of unique tiles is equal to the number of tiles
    if len(unique_tiles) != n:
        return "NO"

    # Check if the square can be constructed
    for i in range(m):
        for j in range(m):
            # Check if the current cell is covered by a tile
            if i == j:
                continue
            top_left = tiles[2 * (i // 2)][0]
            top_right = tiles[2 * (i // 2) + 1][1]
            bottom_left = tiles[2 * (j // 2)][0]
            bottom_right = tiles[2 * (j // 2) + 1][1]
            if top_left != bottom_right or top_right != bottom_left:
                return "NO"

    return "YES"

