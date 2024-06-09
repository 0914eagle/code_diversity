
def solve(board):
    white_pieces = []
    black_pieces = []
    
    for i, row in enumerate(board):
        for j, piece in enumerate(row):
            if piece.isupper():
                white_pieces.append(piece + chr(j + 97) + str(i + 1))
            elif piece.islower():
                black_pieces.append(piece + chr(j + 97) + str(i + 1))
    
    white_pieces.sort()
    black_pieces.sort(reverse=True)
    
    return "White: " + ",".join(white_pieces) + "\nBlack: " + ",".join(black_pieces)

