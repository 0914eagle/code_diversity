
def solve(N):
    # Initialize the number of pieces to 64
    num_pieces = 64
    # Loop through each cut
    for i in range(N):
        # Calculate the number of pieces that will be created by the cut
        num_pieces += 2
        # Subtract 1 from the number of pieces to account for the fact that the cut will remove one piece
        num_pieces -= 1
    # Return the largest number of pieces that can be created
    return num_pieces

