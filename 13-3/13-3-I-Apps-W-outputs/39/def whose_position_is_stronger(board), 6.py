
def whose_position_is_stronger(board):
    white_pieces = ['Q', 'R', 'B', 'N', 'P']
    black_pieces = ['q', 'r', 'b', 'n', 'p']
    white_weight = 0
    black_weight = 0

    for row in board:
        for piece in row:
            if piece in white_pieces:
                white_weight += 1
            elif piece in black_pieces:
                black_weight += 1

    if white_weight > black_weight:
        return "White"
    elif white_weight < black_weight:
        return "Black"
    else:
        return "Draw"

