
def solve(N, K, P, rooks):
    # Initialize a 2D array to store the attacked fields
    attacked = [[0] * N for _ in range(N)]

    # Loop through each rook and its power
    for r, c, x in rooks:
        # Loop through each field in the row and column of the rook
        for i in range(1, N+1):
            # If the field is not the rook's own field, add the rook's power to the attacked field
            if i != r and i != c:
                attacked[r-1][i-1] += x
                attacked[i-1][c-1] += x

    # Loop through each move
    for _ in range(P):
        # Loop through each rook and its new position
        for r1, c1, r2, c2 in moves:
            # Subtract the rook's power from the attacked field it left
            attacked[r1-1][c1-1] -= rooks[r1-1][c1-1]
            attacked[r2-1][c2-1] -= rooks[r1-1][c1-1]
            # Add the rook's power to the attacked field it moved to
            attacked[r2-1][c2-1] += rooks[r1-1][c1-1]

        # Print the total number of attacked fields after each move
        print(sum(sum(row) for row in attacked))

    return attacked

