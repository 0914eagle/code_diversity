
def can_construct_square(n, m, tiles):
    # Check if the input is valid
    if n < 1 or n > 100:
        return "NO"
    if m < 1 or m > 100:
        return "NO"
    if len(tiles) != 2 * n:
        return "NO"

    # Initialize a set to store the unique tile configurations
    unique_configs = set()

    # Iterate over each tile type
    for i in range(n):
        # Get the current tile type
        tile_type = tiles[2 * i] + tiles[2 * i + 1]

        # Check if the tile type is already in the set
        if tile_type in unique_configs:
            return "NO"

        # Add the tile type to the set
        unique_configs.add(tile_type)

    # Check if the number of unique tile configurations is equal to the number of tile types
    if len(unique_configs) != n:
        return "NO"

    # Check if the square is symmetric
    for i in range(m):
        for j in range(i + 1, m):
            if tiles[2 * i] != tiles[2 * j]:
                return "NO"

    # Check if the square is a perfect square
    if m % 2 == 0:
        return "NO"

    # If all checks pass, return "YES"
    return "YES"

