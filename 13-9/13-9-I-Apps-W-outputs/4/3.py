
def solve(n, s, l, a):
    # Sort the array in ascending order
    a.sort()
    # Initialize the minimum number of pieces to be returned
    min_pieces = 0
    # Initialize the current piece with the first element of the array
    current_piece = [a[0]]
    # Iterate over the rest of the array
    for i in range(1, n):
        # If the current piece has less than l elements, add the current element to the piece
        if len(current_piece) < l:
            current_piece.append(a[i])
        # If the current piece has l elements and the difference between the maximum and minimum elements is less than or equal to s, add the current element to a new piece
        elif a[i] - current_piece[0] <= s:
            min_pieces += 1
            current_piece = [a[i]]
        # If the current piece has l elements and the difference between the maximum and minimum elements is greater than s, add the current element to the current piece
        else:
            current_piece.append(a[i])
    # If the last piece has less than l elements, return -1
    if len(current_piece) < l:
        return -1
    # Otherwise, return the minimum number of pieces
    return min_pieces + 1

