
def solve(H, W, K, S):
    # Initialize the number of cuts to 0
    cuts = 0

    # Loop through each row
    for i in range(H):
        # Get the number of white squares in the current row
        num_white = S[i].count(0)

        # If the number of white squares is greater than K, we need to cut
        if num_white > K:
            # Increment the number of cuts
            cuts += 1

    # Return the number of cuts
    return cuts

