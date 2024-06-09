
def solve(A, B):
    # Calculate the minimum number of pieces needed to distribute evenly to A guests
    min_pieces_A = A
    while min_pieces_A % A != 0:
        min_pieces_A += 1

    # Calculate the minimum number of pieces needed to distribute evenly to B guests
    min_pieces_B = B
    while min_pieces_B % B != 0:
        min_pieces_B += 1

    # Return the maximum of the two minimum numbers
    return max(min_pieces_A, min_pieces_B)

