
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
        # Read the move
        r1, c1, r2, c2 = input().split()
        r1, c1, r2, c2 = int(r1), int(c1), int(r2), int(c2)

        # Update the attacked fields
        attacked[r1-1][c1-1] -= 1
        attacked[r2-1][c2-1] += 1

    # Count the number of attacked fields
    result = 0
    for row in attacked:
        result += sum(row)

    return result

