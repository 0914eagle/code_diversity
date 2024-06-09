
def solve(chessboard):
    # Initialize variables
    white_pieces = []
    black_pieces = []
    piece_map = {
        "K": "K",
        "Q": "Q",
        "R": "R",
        "B": "B",
        "N": "N",
        "P": "P"
    }

    # Iterate over the chessboard
    for i, row in enumerate(chessboard):
        for j, piece in enumerate(row):
            # Check if the piece is a white or black piece
            if piece.isupper():
                # Get the piece type and position
                piece_type = piece_map[piece]
                position = f"{j+1}{8-i}"

                # Add the piece to the appropriate list
                if piece.islower():
                    black_pieces.append(f"{piece_type}{position}")
                else:
                    white_pieces.append(f"{piece_type}{position}")

    # Sort the pieces lists
    white_pieces.sort()
    black_pieces.sort(reverse=True)

    # Return the formatted output
    return f"White: {', '.join(white_pieces)}\nBlack: {', '.join(black_pieces)}"

