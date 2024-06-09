
def sabotage_chessboard(N):
    # Initialize the number of pieces as 64
    num_pieces = 64
    # Loop through the number of cuts
    for i in range(N):
        # Decrement the number of pieces by 1
        num_pieces -= 1
        # If the number of pieces is even, decrement it by 1 again
        if num_pieces % 2 == 0:
            num_pieces -= 1
    # Return the number of pieces
    return num_pieces

