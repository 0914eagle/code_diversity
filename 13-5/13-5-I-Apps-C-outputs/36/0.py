
def get_cube_colors(tile_colors):
    # Initialize a set to store the colors of the cube
    cube_colors = set()
    
    # Iterate over the tiles
    for tile_color in tile_colors:
        # Add the colors of the tile to the set
        cube_colors.update(tile_color)
    
    return cube_colors

def get_cube_configurations(tile_colors):
    # Initialize a set to store the configurations of the cube
    cube_configurations = set()
    
    # Iterate over the tiles
    for tile_color in tile_colors:
        # Add the configurations of the tile to the set
        cube_configurations.update(get_tile_configurations(tile_color))
    
    return cube_configurations

def get_tile_configurations(tile_color):
    # Initialize a list to store the configurations of the tile
    tile_configurations = []
    
    # Iterate over the four directions of the tile
    for direction in range(4):
        # Add the configuration of the tile in the current direction to the list
        tile_configurations.append(get_tile_configuration(tile_color, direction))
    
    return tile_configurations

def get_tile_configuration(tile_color, direction):
    # Initialize a list to store the configuration of the tile
    tile_configuration = []
    
    # Iterate over the four corners of the tile
    for corner in range(4):
        # Add the color of the corner to the list
        tile_configuration.append(tile_color[corner])
    
    # Rotate the list of colors by the given direction
    tile_configuration = tile_configuration[direction:] + tile_configuration[:direction]
    
    return tile_configuration

def count_different_cubes(tile_colors):
    # Get the colors of the cube
    cube_colors = get_cube_colors(tile_colors)
    
    # Get the configurations of the cube
    cube_configurations = get_cube_configurations(tile_colors)
    
    # Initialize a counter for the number of different cubes
    different_cubes = 0
    
    # Iterate over the configurations of the cube
    for cube_configuration in cube_configurations:
        # Initialize a flag to indicate if the cube is different
        is_different = True
        
        # Iterate over the colors of the cube
        for color in cube_configuration:
            # If the color is not in the set of cube colors, set the flag to False
            if color not in cube_colors:
                is_different = False
                break
        
        # If the cube is different, increment the counter
        if is_different:
            different_cubes += 1
    
    return different_cubes

if __name__ == '__main__':
    # Read the number of tiles from stdin
    n = int(input())
    
    # Read the colors of the tiles from stdin
    tile_colors = []
    for _ in range(n):
        tile_colors.append(list(map(int, input().split())))
    
    # Count the number of different cubes that can be constructed
    different_cubes = count_different_cubes(tile_colors)
    
    # Print the number of different cubes
    print(different_cubes)

