
import itertools

def get_cubes(tiles):
    
    # Initialize a list to store the cubes
    cubes = []
    
    # Iterate over the tiles
    for tile in tiles:
        # Get the colors of the current tile
        colors = [tile[0], tile[1], tile[2], tile[3]]
        
        # Iterate over the possible rotations of the current tile
        for rotation in itertools.permutations(colors):
            # Check if the current rotation is already in the list of cubes
            if rotation not in cubes:
                # If not, add it to the list of cubes
                cubes.append(rotation)
    
    # Return the number of different cubes
    return len(cubes)

def main():
    # Read the input from stdin
    tiles = []
    for _ in range(int(input())):
        tiles.append(list(map(int, input().split())))
    
    # Call the get_cubes function to get the number of different cubes
    cubes = get_cubes(tiles)
    
    # Print the number of cubes
    print(cubes)

if __name__ == '__main__':
    main()

