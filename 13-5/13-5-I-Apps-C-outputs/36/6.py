
def get_cube_colors(tile_colors):
    # Initialize a set to store the colors of the cube
    cube_colors = set()
    
    # Iterate over the tiles and their colors
    for tile_color in tile_colors:
        # Add the colors of the current tile to the set
        cube_colors.add(tile_color[0])
        cube_colors.add(tile_color[1])
        cube_colors.add(tile_color[2])
        cube_colors.add(tile_color[3])
    
    # Return the set of colors
    return cube_colors

def get_unique_cubes(tile_colors):
    # Initialize a set to store the unique cubes
    unique_cubes = set()
    
    # Iterate over the tile colors
    for tile_color in tile_colors:
        # Add the current tile color to the set of unique cubes
        unique_cubes.add(frozenset(tile_color))
    
    # Return the set of unique cubes
    return unique_cubes

def main():
    # Read the input from stdin
    N = int(input())
    tile_colors = []
    for _ in range(N):
        tile_colors.append(list(map(int, input().split())))
    
    # Get the colors of the cube
    cube_colors = get_cube_colors(tile_colors)
    
    # Get the unique cubes
    unique_cubes = get_unique_cubes(tile_colors)
    
    # Print the number of unique cubes
    print(len(unique_cubes))

if __name__ == '__main__':
    main()

