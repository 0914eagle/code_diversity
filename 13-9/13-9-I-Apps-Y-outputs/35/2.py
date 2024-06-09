
def solve(N):
    # Initialize the number of pieces to 64
    num_pieces = 64
    # Loop through the number of cuts
    for i in range(N):
        # Decrease the number of pieces by 1
        num_pieces -= 1
        # If the number of pieces is divisible by 8, decrease it by 7
        if num_pieces % 8 == 0:
            num_pieces -= 7
    # Return the number of pieces
    return num_pieces

