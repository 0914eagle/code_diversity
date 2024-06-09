
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
    
    # Iterate over each tile type
    for i in range(n):
        # Get the current tile type
        tile = tiles[2 * i] + tiles[2 * i + 1]
        
        # Check if the current tile type is already in the set
        if tile in unique_tiles:
            return "NO"
        
        # Add the current tile type to the set
        unique_tiles.add(tile)
    
    # Check if the set size is equal to the number of tile types
    if len(unique_tiles) != n:
        return "NO"
    
    # Check if the square is symmetric
    for i in range(m):
        for j in range(i + 1, m):
            if tiles[2 * i] != tiles[2 * j]:
                return "NO"
    
    # If all checks pass, return "YES"
    return "YES"

