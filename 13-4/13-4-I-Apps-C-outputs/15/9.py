
def solve(N, K, P, rooks):
    # Initialize a 2D array to represent the board
    board = [[0] * N for _ in range(N)]

    # Place the rooks on the board
    for r, c, x in rooks:
        board[r-1][c-1] = x

    # Initialize a set to keep track of the attacked fields
    attacked_fields = set()

    # Iterate through each move
    for _ in range(P):
        # Update the attacked fields for each rook
        for r in range(N):
            for c in range(N):
                # Get the power of the rook at the current field
                power = board[r][c]

                # If the power is not zero, add the field to the attacked fields set
                if power != 0:
                    attacked_fields.add((r, c))

        # Print the number of attacked fields
        print(len(attacked_fields))

        # Read the next move
        r1, c1, r2, c2 = map(int, input().split())

        # Move the rook and update the board
        board[r1-1][c1-1] = board[r2-1][c2-1]
        board[r2-1][c2-1] = 0

    return attacked_fields

