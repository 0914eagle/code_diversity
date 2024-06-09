
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
        top_left, top_right = tiles[2*i]
        bottom_left, bottom_right = tiles[2*i+1]
        unique_tiles.add((top_left, top_right, bottom_left, bottom_right))
    
    # Check if the square can be constructed
    if len(unique_tiles) == 1:
        return "YES"
    else:
        return "NO"

