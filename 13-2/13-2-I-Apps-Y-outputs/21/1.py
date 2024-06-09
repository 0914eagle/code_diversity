
def get_largest_piece(n, h, v):
    # Calculate the volume of each piece
    piece1 = (n-h) * (n-v) * 4
    piece2 = h * (n-v) * 4
    piece3 = (n-h) * v * 4
    piece4 = h * v * 4

    # Return the largest piece
    return max(piece1, piece2, piece3, piece4)

