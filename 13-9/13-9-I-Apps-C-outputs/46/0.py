
def solve_treasure_map(map_pieces):
    # Initialize the reconstructed map as an empty list
    reconstructed_map = []
    
    # Iterate over the map pieces
    for piece in map_pieces:
        # Get the width and height of the current piece
        width, height = piece[0], piece[1]
        
        # Iterate over the rows of the current piece
        for i in range(height):
            # Add the current row to the reconstructed map
            reconstructed_map.append(piece[2 + i])
    
    # Return the reconstructed map
    return reconstructed_map

