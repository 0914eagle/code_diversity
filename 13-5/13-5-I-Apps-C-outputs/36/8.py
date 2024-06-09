
def get_cubes(tiles):
    # Initialize a set to store the unique cubes
    unique_cubes = set()
    
    # Iterate over the tiles
    for tile in tiles:
        # Get the colors of the current tile
        colors = tile[1:]
        
        # Iterate over the four directions of the tile
        for direction in range(4):
            # Rotate the tile to the current direction
            rotated_colors = [colors[i] for i in range(4) if i != direction]
            rotated_colors.append(colors[direction])
            
            # Add the rotated tile to the set of unique cubes
            unique_cubes.add(tuple(rotated_colors))
    
    # Return the number of unique cubes
    return len(unique_cubes)

def main():
    # Read the input from stdin
    N = int(input())
    tiles = []
    for _ in range(N):
        tiles.append(list(map(int, input().split())))
    
    # Call the function to get the number of unique cubes
    result = get_cubes(tiles)
    
    # Print the result
    print(result)

if __name__ == '__main__':
    main()

