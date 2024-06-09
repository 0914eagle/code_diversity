
def get_cube_colors(tile_colors):
    # Initialize a set to store the colors of the cube
    cube_colors = set()
    
    # Iterate over the tile colors
    for tile_color in tile_colors:
        # Add the colors of the tile to the set
        cube_colors.add(tile_color[0])
        cube_colors.add(tile_color[1])
        cube_colors.add(tile_color[2])
        cube_colors.add(tile_color[3])
    
    return cube_colors

def get_unique_cubes(tile_colors):
    # Initialize a set to store the unique cubes
    unique_cubes = set()
    
    # Iterate over the tile colors
    for tile_color in tile_colors:
        # Add the colors of the tile to the set
        unique_cubes.add(frozenset(tile_color))
    
    return len(unique_cubes)

def main():
    # Read the input from stdin
    num_tiles = int(input())
    tile_colors = []
    for _ in range(num_tiles):
        tile_colors.append(list(map(int, input().split())))
    
    # Get the colors of the cube
    cube_colors = get_cube_colors(tile_colors)
    
    # Get the number of unique cubes
    num_unique_cubes = get_unique_cubes(cube_colors)
    
    # Print the number of unique cubes
    print(num_unique_cubes)

if __name__ == '__main__':
    main()

