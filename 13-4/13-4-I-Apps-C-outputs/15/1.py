
def solve(N, K, P, rooks):
    # Initialize a 2D array to store the attacked fields
    attacked = [[0] * N for _ in range(N)]

    # Loop through each rook and its power
    for r, c, x in rooks:
        # Loop through each field in the row and column of the rook
        for i in range(N):
            # If the field is not the rook's own field, add the rook's power to the attacked field
            if i != r and i != c:
                attacked[r][i] += x
                attacked[i][c] += x

    # Loop through each move
    for _ in range(P):
        # Loop through each rook and its new position
        for r1, c1, r2, c2 in moves:
            # Subtract the rook's power from the attacked field it was on
            attacked[r1][c1] -= x
            # Add the rook's power to the attacked field it is moving to
            attacked[r2][c2] += x

    # Return the total number of attacked fields after all moves
    return sum(sum(row) for row in attacked)

