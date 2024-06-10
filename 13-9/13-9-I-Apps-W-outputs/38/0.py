
def get_min_chessboard_size(n):
    # Initialize the minimum chessboard size as 1
    m = 1
    # Loop until we find a valid placement
    while True:
        # Check if we can place n pieces on a mxm chessboard
        if can_place_n_pieces(n, m):
            # If we can, return the m
            return m
        # If we can't, increment the m and try again
        m += 1

def can_place_n_pieces(n, m):
    # Initialize a set to store the placed pieces
    placed_pieces = set()
    # Loop through the n pieces
    for i in range(1, n + 1):
        # Get the row and column for the current piece
        r, c = get_piece_position(i, m)
        # Check if the piece is already placed
        if (r, c) in placed_pieces:
            # If it is, return False
            return False
        # Add the piece to the set of placed pieces
        placed_pieces.add((r, c))
    # If we reach here, all pieces are placed successfully
    return True

def get_piece_position(i, m):
    # Get the row and column for the current piece
    r = i % m
    c = i // m
    # Return the row and column
    return r, c

if __name__ == '__main__':
    n = int(input())
    print(get_min_chessboard_size(n))
    for i in range(1, n + 1):
        r, c = get_piece_position(i, m)
        print(r, c)

