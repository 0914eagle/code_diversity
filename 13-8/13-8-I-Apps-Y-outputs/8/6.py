
def solve(board):
    white_pieces = []
    black_pieces = []
    for i, row in enumerate(board):
        for j, piece in enumerate(row):
            if piece.isupper():
                white_pieces.append((piece, i+1, j+1))
            elif piece.islower():
                black_pieces.append((piece, i+1, j+1))
    white_pieces.sort(key=lambda x: (x[0], x[1], x[2]))
    black_pieces.sort(key=lambda x: (x[0], x[1], x[2]), reverse=True)
    white_pieces = [piece[0] + str(piece[1]) + chr(piece[2] + 96) for piece in white_pieces]
    black_pieces = [piece[0] + str(piece[1]) + chr(piece[2] + 96) for piece in black_pieces]
    return "White: " + ",".join(white_pieces) + "\nBlack: " + ",".join(black_pieces)

