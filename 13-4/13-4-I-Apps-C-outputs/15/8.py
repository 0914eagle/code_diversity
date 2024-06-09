
def solve(N, K, P, rooks, moves):
    # Initialize a 2D array to store the attacked fields
    attacked = [[0] * N for _ in range(N)]

    # Loop through each move
    for move in moves:
        # Get the current and next positions of the rook
        current_row, current_col, next_row, next_col = move

        # Update the attacked fields for the current position
        attacked[current_row][current_col] = 0

        # Update the attacked fields for the next position
        attacked[next_row][next_col] = 1

    # Return the total number of attacked fields after P moves
    return sum(sum(row) for row in attacked)

