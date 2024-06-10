
def get_cube_configuration(tiles):
    # Initialize a dictionary to store the cube configurations
    cube_configurations = {}
    
    # Iterate over the tiles
    for tile in tiles:
        # Get the tile number and the colors of the corners
        tile_number = tile[0]
        corner_colors = tile[1:]
        
        # Check if the tile number is already in the dictionary
        if tile_number in cube_configurations:
            # If it is, add the colors of the current tile to the existing configuration
            cube_configurations[tile_number].extend(corner_colors)
        else:
            # If it's not, create a new configuration with the colors of the current tile
            cube_configurations[tile_number] = corner_colors
    
    # Return the number of unique cube configurations
    return len(set(frozenset(configuration.items()) for configuration in cube_configurations.values()))

def main():
    # Read the number of tiles from standard input
    num_tiles = int(input())
    
    # Initialize an empty list to store the tiles
    tiles = []
    
    # Read the colors of the corners for each tile from standard input
    for _ in range(num_tiles):
        tile_info = input().split()
        tile_number = int(tile_info[0])
        corner_colors = [int(color) for color in tile_info[1:]]
        tiles.append([tile_number, *corner_colors])
    
    # Call the get_cube_configuration function to get the number of unique cube configurations
    num_cube_configurations = get_cube_configuration(tiles)
    
    # Print the number of unique cube configurations
    print(num_cube_configurations)

if __name__ == '__main__':
    main()

