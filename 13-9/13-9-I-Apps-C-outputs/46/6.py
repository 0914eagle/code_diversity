
def reconstruct_map(map_pieces):
    # Initialize a dictionary to store the map pieces
    pieces = {}

    # Loop through each map piece
    for i, piece in enumerate(map_pieces):
        # Get the width and height of the piece
        w, h = piece[0], piece[1]

        # Add the piece to the dictionary with its index as the key
        pieces[i+1] = piece[2:]

    # Initialize the width and height of the reconstructed map
    w, h = 0, 0

    # Loop through each piece and update the width and height of the reconstructed map
    for piece in pieces.values():
        w = max(w, len(piece[0]))
        h += len(piece)

    # Initialize the reconstructed map with a 2D list of zeros
    reconstructed_map = [[0] * w for _ in range(h)]

    # Loop through each piece and add it to the reconstructed map
    for i, piece in enumerate(pieces.values(), 1):
        # Get the width and height of the piece
        w, h = len(piece[0]), len(piece)

        # Loop through each row of the piece
        for j in range(h):
            # Loop through each column of the piece
            for k in range(w):
                # Get the value of the current square
                value = piece[j][k]

                # Update the reconstructed map with the value
                reconstructed_map[j+i-1][k+i-1] = value

    # Return the width and height of the reconstructed map
    return w, h

