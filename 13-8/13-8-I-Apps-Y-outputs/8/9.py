
def solve(chess_board):
    # Initialize an empty list to store the positions of the pieces
    positions = []

    # Iterate over the rows of the chess board
    for i, row in enumerate(chess_board):
        # Iterate over the columns of the current row
        for j, piece in enumerate(row):
            # Check if the current piece is not a space
            if piece != " ":
                # Get the type of the piece and the position of the piece
                piece_type = piece.upper()
                piece_pos = (j + 1, 8 - i)

                # Add the piece to the list of positions
                positions.append((piece_type, piece_pos))

    # Sort the list of positions based on the piece type and position
    positions.sort(key=lambda x: (x[0], x[1]))

    # Initialize empty strings to store the output for white and black players
    white_output = ""
    black_output = ""

    # Iterate over the list of positions
    for piece_type, piece_pos in positions:
        # Check if the piece is a white piece
        if piece_type.isupper():
            # Add the piece to the white output
            white_output += piece_type
            white_output += str(piece_pos[0])
            white_output += str(piece_pos[1])
            white_output += ","
        # Check if the piece is a black piece
        else:
            # Add the piece to the black output
            black_output += piece_type
            black_output += str(piece_pos[0])
            black_output += str(piece_pos[1])
            black_output += ","

    # Return the output for white and black players
    return "White: " + white_output[:-1] + "\nBlack: " + black_output[:-1]

