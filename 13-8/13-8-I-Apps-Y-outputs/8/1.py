
def chess_notation(board):
    # Initialize empty lists to store the positions of white and black pieces
    white_pieces = []
    black_pieces = []
    
    # Loop through the board and extract the positions of the pieces
    for i, row in enumerate(board):
        for j, piece in enumerate(row):
            # Check if the piece is a white piece
            if piece.isupper():
                # Add the piece to the list of white pieces
                white_pieces.append(piece + str(8 - i) + chr(j + 97))
            # Check if the piece is a black piece
            elif piece.islower():
                # Add the piece to the list of black pieces
                black_pieces.append(piece + str(i + 1) + chr(j + 97))
    
    # Sort the lists of white and black pieces
    white_pieces.sort()
    black_pieces.sort(reverse=True)
    
    # Return the notation for the white and black pieces
    return "White: " + ",".join(white_pieces) + "\nBlack: " + ",".join(black_pieces)

