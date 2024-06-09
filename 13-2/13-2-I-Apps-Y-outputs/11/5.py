
def solve(A, B):
    # Calculate the minimum number of pieces needed to distribute evenly among A guests
    min_pieces_A = A
    while min_pieces_A * A % B != 0:
        min_pieces_A += 1

    # Calculate the minimum number of pieces needed to distribute evenly among B guests
    min_pieces_B = B
    while min_pieces_B * B % A != 0:
        min_pieces_B += 1

    # Return the maximum of the two minimum numbers
    return max(min_pieces_A, min_pieces_B)

