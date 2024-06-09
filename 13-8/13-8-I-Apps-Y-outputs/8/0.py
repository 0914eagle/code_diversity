
def solve(chess_board):
    white_pieces = []
    black_pieces = []

    for i, row in enumerate(chess_board):
        for j, piece in enumerate(row):
            if piece.isupper():
                white_pieces.append((piece, i + 1, j + 1))
            elif piece.islower():
                black_pieces.append((piece, i + 1, j + 1))

    white_pieces.sort(key=lambda x: (x[0], x[1], x[2]))
    black_pieces.sort(key=lambda x: (x[0], x[1], x[2]), reverse=True)

    white_notation = ",".join([f"{piece}{row}{col}" for piece, row, col in white_pieces])
    black_notation = ",".join([f"{piece}{row}{col}" for piece, row, col in black_pieces])

    return f"White: {white_notation}\nBlack: {black_notation}"

