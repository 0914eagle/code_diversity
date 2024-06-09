
def solve_treasure_hunt(map_pieces):
    # Initialize a dictionary to store the map pieces and their corresponding indices
    map_pieces_dict = {i: map_piece for i, map_piece in enumerate(map_pieces, 1)}
    
    # Initialize a list to store the reconstructed map
    reconstructed_map = []
    
    # Iterate through the map pieces and reconstruct the map
    for i in range(1, len(map_pieces) + 1):
        # Get the current map piece and its index
        map_piece = map_pieces_dict[i]
        index = i
        
        # Check if the current map piece has already been used
        if map_piece in reconstructed_map:
            # If the map piece has already been used, rotate it until it can be placed correctly
            while map_piece in reconstructed_map:
                map_piece = rotate_map_piece(map_piece)
        
        # Add the map piece to the reconstructed map
        reconstructed_map.append(map_piece)
        
        # Update the dictionary to reflect the used map piece
        map_pieces_dict[i] = map_piece
    
    # Get the width and height of the reconstructed map
    width = len(reconstructed_map[0])
    height = len(reconstructed_map)
    
    # Create a list to store the indices of the map pieces in the reconstructed map
    map_piece_indices = []
    
    # Iterate through the reconstructed map and get the indices of the map pieces
    for i in range(height):
        for j in range(width):
            map_piece_indices.append(map_pieces_dict.index(reconstructed_map[i][j]) + 1)
    
    # Return the width, height, and indices of the map pieces in the reconstructed map
    return width, height, map_piece_indices

# Rotate a map piece by 90 degrees
def rotate_map_piece(map_piece):
    return [list(row) for row in zip(*map_piece[::-1])]

