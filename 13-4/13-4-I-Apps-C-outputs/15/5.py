
def solve(N, K, P, rooks):
    # Initialize a 2D array to store the attacked fields
    attacked = [[0] * N for _ in range(N)]

    # Iterate over each rook
    for r, c, x in rooks:
        # Get the row and column indices of the rook
        row, col = r - 1, c - 1
        # Update the attacked fields in the row and column
        for i in range(N):
            attacked[row][i] ^= x
            attacked[i][col] ^= x

    # Initialize a list to store the number of attacked fields after each move
    attacked_fields = []

    # Iterate over each move
    for _ in range(P):
        # Get the current number of attacked fields
        total_attacked = sum(sum(row) for row in attacked)
        # Add the current number of attacked fields to the list
        attacked_fields.append(total_attacked)
        # Update the attacked fields after the move
        for r1, c1, r2, c2 in moves:
            row1, col1 = r1 - 1, c1 - 1
            row2, col2 = r2 - 1, c2 - 1
            attacked[row1][col1] ^= x
            attacked[row2][col2] ^= x

    return attacked_fields

