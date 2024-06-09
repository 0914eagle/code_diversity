
def split_strip(n, s, l, a):
    # Sort the array in ascending order
    a.sort()
    # Initialize the number of pieces to 0
    pieces = 0
    # Initialize the current piece to be empty
    current_piece = []
    # Loop through the array
    for i in range(n):
        # If the current piece is empty, add the first number to it
        if not current_piece:
            current_piece.append(a[i])
        # If the current piece is not empty and the difference between the current number and the last number in the piece is less than or equal to s, add the current number to the piece
        elif a[i] - current_piece[-1] <= s:
            current_piece.append(a[i])
        # If the current piece is not empty and the difference between the current number and the last number in the piece is greater than s, start a new piece
        else:
            pieces += 1
            current_piece = [a[i]]
    # Add the last piece
    pieces += 1
    # If the length of the last piece is less than l, return -1 because no way to split the strip
    if len(current_piece) < l:
        return -1
    # Return the number of pieces
    return pieces

