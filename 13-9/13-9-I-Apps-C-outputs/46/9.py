
def solve(map_pieces):
    # Convert the map pieces to a 2D array of integers
    map_array = []
    for piece in map_pieces:
        map_array.append([int(x) for x in piece])
    
    # Find the width and height of the reconstructed map
    width = len(map_array[0])
    height = len(map_array)
    
    # Initialize the reconstructed map with all zeros
    reconstructed_map = [[0] * width for _ in range(height)]
    
    # Fill in the reconstructed map with the map pieces
    for i in range(len(map_array)):
        for j in range(len(map_array[0])):
            reconstructed_map[i][j] = map_array[i][j]
    
    # Return the reconstructed map and the indices of the map pieces
    return reconstructed_map, [i+1 for i in range(len(map_array))]

