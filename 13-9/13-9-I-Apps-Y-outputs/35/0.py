
def solve(N):
    # Initialize a list to store the positions of the cuts
    cuts = []

    # Loop through the number of cuts Mirko can make
    for i in range(N):
        # Add the current cut position to the list of cuts
        cuts.append(i)

    # Sort the list of cuts in ascending order
    cuts.sort()

    # Initialize a variable to store the maximum number of pieces Slavko's chessboard can crash into
    max_pieces = 0

    # Loop through the list of cuts
    for i in range(len(cuts)):
        # Check if the current cut is a horizontal cut
        if cuts[i] % 8 == 0:
            # If it is a horizontal cut, add the number of pieces it can crash into to the maximum number of pieces
            max_pieces += 8
        # Check if the current cut is a vertical cut
        elif cuts[i] % 8 == 1:
            # If it is a vertical cut, add the number of pieces it can crash into to the maximum number of pieces
            max_pieces += 8
        # Check if the current cut is a diagonal cut
        elif cuts[i] % 8 == 2:
            # If it is a diagonal cut, add the number of pieces it can crash into to the maximum number of pieces
            max_pieces += 4

    # Return the maximum number of pieces Slavko's chessboard can crash into
    return max_pieces

