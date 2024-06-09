
def f1(N):
    # Initialize a list to store the positions of the cuts
    cuts = []

    # Iterate through the given number of cuts
    for i in range(N):
        # Add the current cut position to the list of cuts
        cuts.append(i)

    # Sort the list of cuts in ascending order
    cuts.sort()

    # Initialize a variable to store the maximum number of pieces that can be broken
    max_pieces = 0

    # Iterate through the list of cuts
    for i in range(len(cuts)):
        # Check if the current cut is within the bounds of the chessboard
        if cuts[i] >= 0 and cuts[i] < 8:
            # Increment the maximum number of pieces that can be broken
            max_pieces += 1

    # Return the maximum number of pieces that can be broken
    return max_pieces

