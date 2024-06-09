
def solve(N, K, P, rooks, moves):
    # Initialize a 2D array to represent the chessboard
    board = [[0] * N for _ in range(N)]

    # Place the rooks on the board according to the input
    for r, c, x in rooks:
        board[r - 1][c - 1] = x

    # Loop through each move and calculate the number of attacked fields
    for move in moves:
        # Get the starting and ending positions of the rook
        start_r, start_c, end_r, end_c = move

        # Move the rook on the board
        board[end_r - 1][end_c - 1] = board[start_r - 1][start_c - 1]
        board[start_r - 1][start_c - 1] = 0

        # Calculate the number of attacked fields
        attacked_fields = 0
        for i in range(N):
            for j in range(N):
                if board[i][j] != 0:
                    attacked_fields += 1

        # Print the number of attacked fields
        print(attacked_fields)

    return

