
def solve(N):
    # Initialize the maximum number of pieces to 0
    max_pieces = 0
    # Loop through all possible combinations of horizontal and vertical cuts
    for i in range(N + 1):
        for j in range(N - i + 1):
            # Calculate the number of pieces that can be created with the current combination of cuts
            pieces = i * (N - i) + j * i
            # Update the maximum number of pieces if necessary
            max_pieces = max(max_pieces, pieces)
    # Return the maximum number of pieces that can be created
    return max_pieces

