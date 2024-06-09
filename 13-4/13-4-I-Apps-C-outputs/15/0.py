
def solve(N, K, P, rooks):
    # Initialize a 2D array to store the attacked fields
    attacked = [[0] * N for _ in range(N)]

    # Loop through each rook and its power
    for r, c, x in rooks:
        # Loop through each field in the row and column of the rook
        for i in range(N):
            # If the field is not the rook's own field, add the power to the attacked field
            if i != r:
                attacked[r][i] += x
            if i != c:
                attacked[i][c] += x

    # Loop through each move
    for _ in range(P):
        # Loop through each rook and its new position
        for r1, c1, r2, c2 in moves:
            # Subtract the power from the attacked field of the old position
            attacked[r1][c1] -= x
            # Add the power to the attacked field of the new position
            attacked[r2][c2] += x

    # Return the total number of attacked fields after P moves
    return sum(sum(row) for row in attacked)

