
def get_cube_colors(tile_colors):
    # Initialize a set to store the colors of the cube
    cube_colors = set()
    
    # Iterate over the tiles and their colors
    for tile_color in tile_colors:
        # Add the color of the tile to the set of cube colors
        cube_colors.add(tile_color)
    
    # Return the set of cube colors
    return cube_colors

def get_cube_configurations(cube_colors):
    # Initialize a set to store the configurations of the cube
    cube_configurations = set()
    
    # Iterate over the colors of the cube
    for color in cube_colors:
        # Get the tile colors for the current color
        tile_colors = [color]
        
        # Iterate over the other colors of the cube
        for other_color in cube_colors:
            # If the current color is not the same as the other color
            if color != other_color:
                # Add the other color to the tile colors
                tile_colors.append(other_color)
        
        # Add the tile colors to the set of cube configurations
        cube_configurations.add(tuple(tile_colors))
    
    # Return the set of cube configurations
    return cube_configurations

def count_cubes(tile_colors):
    # Get the colors of the cube
    cube_colors = get_cube_colors(tile_colors)
    
    # Get the configurations of the cube
    cube_configurations = get_cube_configurations(cube_colors)
    
    # Return the number of cube configurations
    return len(cube_configurations)

if __name__ == '__main__':
    # Read the number of tiles from standard input
    n = int(input())
    
    # Initialize a list to store the colors of the tiles
    tile_colors = []
    
    # Iterate over the tiles
    for i in range(n):
        # Read the colors of the current tile from standard input
        colors = [int(x) for x in input().split()]
        
        # Add the colors of the current tile to the list of tile colors
        tile_colors.append(colors)
    
    # Count the number of cubes that can be constructed
    count = count_cubes(tile_colors)
    
    # Print the number of cubes
    print(count)

