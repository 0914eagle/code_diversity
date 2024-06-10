
def get_cube_colors(tiles):
    # Initialize a set to store the colors of the cube
    cube_colors = set()
    
    # Iterate over the tiles
    for tile in tiles:
        # Get the colors of the current tile
        colors = [tile[0], tile[1], tile[2], tile[3]]
        
        # Add the colors to the set
        cube_colors.add(tuple(colors))
    
    return cube_colors

def get_cube_combinations(tiles):
    # Initialize a set to store the combinations of the cube
    cube_combinations = set()
    
    # Iterate over the tiles
    for tile in tiles:
        # Get the colors of the current tile
        colors = [tile[0], tile[1], tile[2], tile[3]]
        
        # Iterate over the possible rotations of the tile
        for rotation in range(4):
            # Get the rotated colors of the current tile
            rotated_colors = [colors[(rotation + i) % 4] for i in range(4)]
            
            # Add the rotated colors to the set
            cube_combinations.add(tuple(rotated_colors))
    
    return cube_combinations

def get_number_of_cubes(tiles):
    # Get the colors of the cube
    cube_colors = get_cube_colors(tiles)
    
    # Get the combinations of the cube
    cube_combinations = get_cube_combinations(tiles)
    
    # Return the number of unique combinations
    return len(cube_combinations)

if __name__ == '__main__':
    # Get the number of tiles
    n = int(input())
    
    # Initialize a list to store the tiles
    tiles = []
    
    # Iterate over the tiles
    for i in range(n):
        # Get the colors of the current tile
        colors = [int(j) for j in input().split()]
        
        # Add the colors to the list
        tiles.append(colors)
    
    # Get the number of cubes
    number_of_cubes = get_number_of_cubes(tiles)
    
    # Print the number of cubes
    print(number_of_cubes)

