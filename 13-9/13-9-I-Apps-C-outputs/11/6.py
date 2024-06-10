
def get_cube_count(tiles):
    # Initialize a set to store the unique cubes
    unique_cubes = set()
    
    # Iterate over all possible combinations of tiles
    for tile_1 in tiles:
        for tile_2 in tiles:
            for tile_3 in tiles:
                for tile_4 in tiles:
                    for tile_5 in tiles:
                        for tile_6 in tiles:
                            # Check if the cubes are valid
                            if is_valid_cube([tile_1, tile_2, tile_3, tile_4, tile_5, tile_6]):
                                # Add the cube to the set of unique cubes
                                unique_cubes.add(frozenset([tile_1, tile_2, tile_3, tile_4, tile_5, tile_6]))
    
    # Return the number of unique cubes
    return len(unique_cubes)

def is_valid_cube(tiles):
    # Check if all tiles have the same color at the top-left corner
    top_left_color = tiles[0][0]
    for tile in tiles:
        if tile[0] != top_left_color:
            return False
    
    # Check if all tiles have the same color at the top-right corner
    top_right_color = tiles[0][1]
    for tile in tiles:
        if tile[1] != top_right_color:
            return False
    
    # Check if all tiles have the same color at the bottom-left corner
    bottom_left_color = tiles[0][2]
    for tile in tiles:
        if tile[2] != bottom_left_color:
            return False
    
    # Check if all tiles have the same color at the bottom-right corner
    bottom_right_color = tiles[0][3]
    for tile in tiles:
        if tile[3] != bottom_right_color:
            return False
    
    # If all colors are the same, return True
    return True

if __name__ == '__main__':
    # Read the input from stdin
    N = int(input())
    tiles = []
    for _ in range(N):
        tiles.append(list(map(int, input().split())))
    
    # Call the function to get the number of unique cubes
    cube_count = get_cube_count(tiles)
    
    # Print the result
    print(cube_count)

