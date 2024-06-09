
def strip_split(n, s, l, a):
    # Sort the array in ascending order
    a.sort()
    # Initialize the number of pieces to 0
    pieces = 0
    # Initialize the current piece to be empty
    current_piece = []
    # Iterate through the array
    for i in range(n):
        # If the current piece is empty, add the current number to the piece
        if not current_piece:
            current_piece.append(a[i])
        # If the current piece is not empty and the current number is within the range of the piece, add the current number to the piece
        elif a[i] - current_piece[0] <= s and len(current_piece) + 1 >= l:
            current_piece.append(a[i])
        # If the current piece is not empty and the current number is not within the range of the piece, start a new piece
        else:
            pieces += 1
            current_piece = [a[i]]
    # Add the last piece
    pieces += 1
    return pieces

