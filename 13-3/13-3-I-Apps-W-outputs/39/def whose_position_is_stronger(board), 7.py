
def whose_position_is_stronger(board):
    white_pieces = ['Q', 'R', 'B', 'N', 'P']
    black_pieces = ['q', 'r', 'b', 'n', 'p']
    piece_weights = {
        'Q': 9,
        'R': 5,
        'B': 3,
        'N': 3,
        'P': 1,
        'K': 0
    }
    white_weight = 0
    black_weight = 0
    for row in board:
        for piece in row:
            if piece in white_pieces:
                white_weight += piece_weights[piece]
            elif piece in black_pieces:
                black_weight += piece_weights[piece]
    if white_weight > black_weight:
        return "White"
    elif white_weight < black_weight:
        return "Black"
    else:
        return "Draw"

