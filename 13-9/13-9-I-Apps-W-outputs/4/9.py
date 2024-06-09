
def split_strip(n, s, l, a):
    # Sort the array in ascending order
    a.sort()
    # Initialize the minimum number of pieces to be returned
    min_pieces = 0
    # Initialize the current piece
    current_piece = []
    # Iterate through the array
    for i in range(n):
        # If the current piece is empty, add the current number to the piece
        if not current_piece:
            current_piece.append(a[i])
        # If the current piece is not empty and the current number is within the range of the piece, add the current number to the piece
        elif a[i] - current_piece[0] <= s:
            current_piece.append(a[i])
        # If the current piece is not empty and the current number is not within the range of the piece, add the current piece to the pieces and start a new piece
        else:
            min_pieces += 1
            current_piece = [a[i]]
    # Add the last piece to the pieces
    min_pieces += 1
    return min_pieces

