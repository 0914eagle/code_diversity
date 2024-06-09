
def cut_chessboard(N):
    # Initialize the number of pieces as 64 (since there are 64 pieces in a standard chessboard)
    num_pieces = 64
    # Loop through each cut
    for i in range(N):
        # Decrease the number of pieces by 4 (since each cut will remove 4 pieces)
        num_pieces -= 4
        # If the number of pieces becomes negative, break the loop
        if num_pieces < 0:
            break
    # Return the largest number of pieces that can be removed (i.e. the initial number of pieces - the number of pieces after the last cut)
    return 64 - num_pieces

