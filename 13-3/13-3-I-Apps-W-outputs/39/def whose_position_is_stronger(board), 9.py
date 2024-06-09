
def whose_position_is_stronger(board):
    white_pieces = {'Q': 9, 'R': 5, 'B': 3, 'N': 3, 'P': 1}
    black_pieces = {'q': 9, 'r': 5, 'b': 3, 'n': 3, 'p': 1}
    white_weight = 0
    black_weight = 0

    for row in board:
        for piece in row:
            if piece in white_pieces:
                white_weight += white_pieces[piece]
            elif piece in black_pieces:
                black_weight += black_pieces[piece.lower()]

    if white_weight > black_weight:
        return "White"
    elif white_weight < black_weight:
        return "Black"
    else:
        return "Draw"

