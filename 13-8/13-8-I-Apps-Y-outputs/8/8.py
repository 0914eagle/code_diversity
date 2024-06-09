
def solve_chess_notation(chessboard):
    # Initialize an empty list to store the pieces of each player
    white_pieces = []
    black_pieces = []

    # Iterate over the rows of the chessboard
    for row in chessboard:
        # Iterate over the columns of the row
        for col in row:
            # Check if the current position has a piece
            if col != ":":
                # Add the piece to the appropriate list
                if col.islower():
                    black_pieces.append(col)
                else:
                    white_pieces.append(col)

    # Sort the pieces of each player by their position
    white_pieces.sort(key=lambda x: (x[1], x[0]))
    black_pieces.sort(key=lambda x: (x[1], x[0]), reverse=True)

    # Join the pieces into a comma-separated string
    white_notation = ",".join(white_pieces)
    black_notation = ",".join(black_pieces)

    # Return the final output
    return f"White: {white_notation}\nBlack: {black_notation}"

