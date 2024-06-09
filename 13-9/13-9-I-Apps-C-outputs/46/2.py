
def reconstruct_map(map_pieces):
    # Initialize a dictionary to store the map pieces and their dimensions
    pieces = {}
    for i, piece in enumerate(map_pieces):
        pieces[i] = (piece[0], piece[1], piece[2:])

    # Find the width and height of the reconstructed map
    width = max(piece[0] for piece in pieces.values())
    height = max(piece[1] for piece in pieces.values())

    # Initialize the reconstructed map with empty strings
    reconstructed_map = [["" for _ in range(width)] for _ in range(height)]

    # Fill in the reconstructed map with the map pieces
    for i, piece in pieces.items():
        for row in range(piece[1]):
            for col in range(piece[0]):
                reconstructed_map[row][col] += piece[2][row][col]

    # Return the reconstructed map and the indices of the map pieces
    return (width, height), ["".join(row) for row in reconstructed_map]

