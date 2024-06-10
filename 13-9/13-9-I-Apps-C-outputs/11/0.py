
def get_cubes(tiles):
    # Initialize a list to store the cubes
    cubes = []
    
    # Iterate over the tiles
    for tile in tiles:
        # Check if the tile is already used in any of the cubes
        if tile not in cubes:
            # If not, add the tile to the list of cubes
            cubes.append(tile)
    
    # Return the number of cubes
    return len(cubes)

def main():
    # Read the number of tiles from stdin
    n = int(input())
    
    # Read the colors of the tiles from stdin
    colors = []
    for i in range(n):
        colors.append([int(i) for i in input().split()])
    
    # Call the function to get the number of cubes
    result = get_cubes(colors)
    
    # Print the result
    print(result)

if __name__ == '__main__':
    main()

