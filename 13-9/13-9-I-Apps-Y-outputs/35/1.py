
def cut_chessboard(N):
    # Initialize the number of pieces to be crashed into as 0
    pieces = 0
    
    # Loop through each possible cut
    for i in range(1, N+1):
        # Check if the current cut is valid
        if i % 2 == 0:
            # If the current cut is valid, increment the number of pieces to be crashed into
            pieces += 1
    
    # Return the largest number of pieces that can be crashed into
    return pieces

