
def solve(N, K, P, rooks, moves):
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
    for r1, c1, r2, c2 in moves:
        # Subtract the power of the rook that is moving from the attacked fields it sees
        attacked[r1-1][c1-1] -= rooks[r1-1][c1-1]
        attacked[r2-1][c2-1] -= rooks[r1-1][c1-1]
        # Add the power of the rook that is moving to the attacked fields it sees
        attacked[r2-1][c2-1] += rooks[r1-1][c1-1]

        # Print the total number of attacked fields after the move
        print(sum(sum(row) for row in attacked))

    return attacked

