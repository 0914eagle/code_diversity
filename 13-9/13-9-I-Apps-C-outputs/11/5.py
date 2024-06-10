
def get_cube_count(tiles):
    # Initialize a set to store the unique cubes
    unique_cubes = set()
    
    # Iterate over each tile
    for tile in tiles:
        # Get the tile's number and colors
        number = tile[0]
        colors = tile[1:]
        
        # Iterate over each color combination
        for color_combination in itertools.permutations(colors, 4):
            # Create a cube with the current tile and color combination
            cube = [number, color_combination]
            
            # Add the cube to the set of unique cubes
            unique_cubes.add(tuple(cube))
    
    # Return the number of unique cubes
    return len(unique_cubes)

def main():
    # Read the input from stdin
    tiles = []
    for line in sys.stdin:
        tiles.append(list(map(int, line.strip().split())))
    
    # Call the function to get the number of unique cubes
    cube_count = get_cube_count(tiles)
    
    # Print the result
    print(cube_count)

if __name__ == '__main__':
    main()

