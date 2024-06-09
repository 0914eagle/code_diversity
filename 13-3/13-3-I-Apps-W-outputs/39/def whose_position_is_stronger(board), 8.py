
def whose_position_is_stronger(board):
    # Initialize the weights of the pieces
    piece_weights = {
        'Q': 9,
        'R': 5,
        'B': 3,
        'N': 3,
        'P': 1,
        'K': 0
    }

    # Initialize the total weight of the white and black pieces
    white_weight = 0
    black_weight = 0

    # Iterate over the board
    for row in board:
        for piece in row:
            # Check if the piece is uppercase (white) or lowercase (black)
            if piece.isupper():
                white_weight += piece_weights[piece]
            else:
                black_weight += piece_weights[piece.lower()]

    # Return "White", "Black", or "Draw" depending on the weights
    if white_weight > black_weight:
        return "White"
    elif white_weight < black_weight:
        return "Black"
    else:
        return "Draw"

