
def can_construct_square(n, m, tiles):
    # Check if the input is valid
    if n < 1 or n > 100:
        return "NO"
    if m < 1 or m > 100:
        return "NO"
    if len(tiles) != 2 * n:
        return "NO"

    # Initialize a 2D array to store the tiles
    tile_array = [[0] * m for _ in range(m)]

    # Iterate through the tiles and place them in the array
    for i in range(n):
        for j in range(n):
            tile = tiles[i * 2][j * 2]
            if tile_array[i][j] != 0:
                return "NO"
            tile_array[i][j] = tile

    # Check if the array is symmetric
    for i in range(m):
        for j in range(i + 1, m):
            if tile_array[i][j] != tile_array[j][i]:
                return "NO"

    # Check if the array is filled
    for i in range(m):
        for j in range(m):
            if tile_array[i][j] == 0:
                return "NO"

    return "YES"

