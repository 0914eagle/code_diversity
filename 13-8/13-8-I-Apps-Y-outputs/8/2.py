
def chess_notation(picture):
    # Initialize empty lists to store the white and black pieces
    white_pieces = []
    black_pieces = []
    
    # Iterate through the picture and extract the pieces
    for row in picture:
        for col in row:
            if col.isupper():
                # Uppercase letter indicates a white piece
                white_pieces.append(col)
            elif col.islower():
                # Lowercase letter indicates a black piece
                black_pieces.append(col)
    
    # Sort the pieces by their type and position
    white_pieces.sort(key=lambda x: (x.upper(), x.lower()))
    black_pieces.sort(key=lambda x: (x.upper(), x.lower()))
    
    # Convert the pieces to the chess notation
    white_notation = ",".join([piece.upper() + str(picture.index(piece) + 1) for piece in white_pieces])
    black_notation = ",".join([piece.upper() + str(8 - picture.index(piece)) for piece in black_pieces])
    
    return "White: " + white_notation + "\nBlack: " + black_notation

