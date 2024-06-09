
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

        # Check if the current tile type is already present in the set
        if tile_type in unique_configs:
            return "NO"

        # Add the current tile type to the set
        unique_configs.add(tile_type)

    # If all tile types are unique, return "YES"
    return "YES"

