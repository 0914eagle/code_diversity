
def get_cube_count(tiles):
    # Initialize a set to store the unique cubes
    unique_cubes = set()
    
    # Iterate over each possible combination of tiles
    for tile_combination in itertools.combinations(tiles, 6):
        # Check if the current combination forms a valid cube
        if is_valid_cube(tile_combination):
            # Add the cube to the set of unique cubes
            unique_cubes.add(frozenset(tile_combination))
    
    # Return the number of unique cubes
    return len(unique_cubes)

def is_valid_cube(tile_combination):
    # Initialize a set to store the colors of the cube
    cube_colors = set()
    
    # Iterate over each tile in the combination
    for tile in tile_combination:
        # Get the colors of the current tile
        tile_colors = get_tile_colors(tile)
        
        # Check if the current tile forms a valid corner of the cube
        if not is_valid_corner(tile_colors):
            return False
        
        # Add the colors of the current tile to the set of cube colors
        cube_colors.update(tile_colors)
    
    # Check if the cube has 6 unique colors
    if len(cube_colors) != 6:
        return False
    
    # Check if the cube is a valid cube
    if not is_valid_cube_orientation(tile_combination):
        return False
    
    # If all conditions are met, the cube is valid
    return True

def get_tile_colors(tile):
    # Get the colors of the current tile
    tile_colors = [tile[0], tile[1], tile[2], tile[3]]
    
    # Return the colors of the current tile
    return tile_colors

def is_valid_corner(tile_colors):
    # Check if the current tile forms a valid corner of the cube
    if len(tile_colors) != 4:
        return False
    
    # Check if the colors of the current tile are all unique
    if len(set(tile_colors)) != 4:
        return False
    
    # If all conditions are met, the current tile forms a valid corner of the cube
    return True

def is_valid_cube_orientation(tile_combination):
    # Initialize a set to store the orientations of the cube
    cube_orientations = set()
    
    # Iterate over each tile in the combination
    for tile in tile_combination:
        # Get the orientation of the current tile
        tile_orientation = get_tile_orientation(tile)
        
        # Add the orientation of the current tile to the set of cube orientations
        cube_orientations.add(tile_orientation)
    
    # Check if the cube has 6 unique orientations
    if len(cube_orientations) != 6:
        return False
    
    # If all conditions are met, the cube has 6 unique orientations
    return True

def get_tile_orientation(tile):
    # Get the orientation of the current tile
    tile_orientation = [tile[0], tile[1], tile[2], tile[3]]
    
    # Return the orientation of the current tile
    return tile_orientation

if __name__ == '__main__':
    # Read the input from stdin
    num_tiles = int(input())
    tiles = []
    for _ in range(num_tiles):
        tiles.append(list(map(int, input().split())))
    
    # Get the number of unique cubes that can be constructed
    cube_count = get_cube_count(tiles)
    
    # Print the number of unique cubes
    print(cube_count)

