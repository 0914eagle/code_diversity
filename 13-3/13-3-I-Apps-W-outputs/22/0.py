
def solve(H, W, K, S):
    # Initialize the number of cuts to 0
    cuts = 0

    # Loop through each row
    for i in range(H):
        # Initialize the number of white squares in the current row to 0
        num_white = 0

        # Loop through each column in the current row
        for j in range(W):
            # If the current square is white, increment the number of white squares
            if S[i][j] == "0":
                num_white += 1

            # If the number of white squares is greater than or equal to K, we need to cut
            if num_white >= K:
                # Increment the number of cuts
                cuts += 1

                # Reset the number of white squares to 0
                num_white = 0

    # Return the number of cuts
    return cuts

