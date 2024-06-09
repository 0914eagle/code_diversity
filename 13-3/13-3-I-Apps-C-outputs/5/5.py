
def longest_balanced_string(pieces):
    # Initialize a dictionary to store the length of the longest balanced string formed by concatenating each piece
    piece_lengths = {}
    # Initialize the longest balanced string length to 0
    longest_length = 0

    for piece in pieces:
        # Check if the piece is already in the dictionary
        if piece not in piece_lengths:
            # If not, calculate the length of the longest balanced string formed by concatenating the piece with all the other pieces
            piece_lengths[piece] = max(len(piece) + piece_lengths.get(piece[1:], 0), len(piece[1:]) + piece_lengths.get(piece[:-1], 0))
        # Update the longest balanced string length
        longest_length = max(longest_length, piece_lengths[piece])

    return longest_length

