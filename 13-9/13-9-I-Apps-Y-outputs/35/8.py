
def solve(N):
    # Initialize a list to store the positions of the cuts
    cuts = []

    # Iterate from 1 to N
    for i in range(1, N + 1):
        # Append the current position to the list of cuts
        cuts.append(i)

    # Return the length of the list of cuts, which is the largest number of pieces Slavko's chessboard can crash into
    return len(cuts)

