
def solve(map_pieces):
    # Convert the map pieces to a 2D array
    map_array = []
    for piece in map_pieces:
        map_array.append(list(piece))
    
    # Find the width and height of the reconstructed map
    width = len(map_array[0])
    height = len(map_array)
    
    # Initialize the reconstructed map with all 0s
    reconstructed_map = [[0] * width for _ in range(height)]
    
    # Loop through each piece and update the reconstructed map
    for i, piece in enumerate(map_array):
        for j, char in enumerate(piece):
            reconstructed_map[j][i] = char
    
    # Return the width and height of the reconstructed map, followed by the reconstructed map
    return width, height, reconstructed_map

