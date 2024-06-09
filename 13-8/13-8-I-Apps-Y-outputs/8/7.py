
def solve(chessboard):
    # Initialize variables to keep track of the pieces and their positions
    white_pieces = []
    black_pieces = []
    white_king = None
    black_king = None

    # Iterate through the rows of the chessboard
    for i, row in enumerate(chessboard):
        # Iterate through the columns of the chessboard
        for j, column in enumerate(row):
            # Check if the current position is occupied by a piece
            if column.isalpha():
                # Check if the piece is white or black
                if column.isupper():
                    # Add the piece to the list of white pieces
                    white_pieces.append((i, j, column))
                    # Check if the piece is a king
                    if column == "K":
                        # Save the position of the white king
                        white_king = (i, j)
                else:
                    # Add the piece to the list of black pieces
                    black_pieces.append((i, j, column))
                    # Check if the piece is a king
                    if column == "k":
                        # Save the position of the black king
                        black_king = (i, j)

    # Sort the white pieces by their position
    white_pieces.sort(key=lambda x: x[0])
    white_pieces.sort(key=lambda x: x[1])

    # Sort the black pieces by their position
    black_pieces.sort(key=lambda x: x[0])
    black_pieces.sort(key=lambda x: x[1])

    # Create a list to store the description of the white pieces
    white_description = []
    # Create a list to store the description of the black pieces
    black_description = []

    # Iterate through the white pieces
    for piece in white_pieces:
        # Get the type of the piece
        piece_type = piece[2]
        # Get the position of the piece
        piece_position = piece[1] + 1
        # Add the piece to the description
        white_description.append(piece_type + str(piece_position))

    # Iterate through the black pieces
    for piece in black_pieces:
        # Get the type of the piece
        piece_type = piece[2]
        # Get the position of the piece
        piece_position = piece[1] + 1
        # Add the piece to the description
        black_description.append(piece_type + str(piece_position))

    # Add the white king to the description
    white_description.append("K" + str(white_king[1] + 1))
    # Add the black king to the description
    black_description.append("k" + str(black_king[1] + 1))

    # Return the description of the white and black pieces
    return "White: " + ",".join(white_description) + "\nBlack: " + ",".join(black_description)

