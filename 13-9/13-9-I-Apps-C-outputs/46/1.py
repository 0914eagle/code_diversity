
def solve(pieces):
    # Initialize the reconstructed map as an empty grid
    reconstructed_map = []
    
    # Loop through each piece and add it to the reconstructed map
    for piece in pieces:
        # Get the width and height of the piece
        width, height = piece[0], piece[1]
        
        # Add the piece to the reconstructed map
        reconstructed_map.append(piece[2:])
    
    # Return the reconstructed map
    return reconstructed_map

