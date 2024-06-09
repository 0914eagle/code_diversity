
def n_queens(n, m, board):
    # Initialize variables
    queens = []
    ways = 0

    # Loop through each row
    for i in range(n):
        # Loop through each column
        for j in range(m):
            # If the current cell is not broken and there is no queen in the same row or diagonal, place a queen
            if board[i][j] == '.' and all(board[i][k] != 'Q' for k in range(m)) and all(board[p][j] != 'Q' for p in range(n)):
                queens.append((i, j))
                ways += 1
                break

    # Return the maximum number of queens and the number of ways to place them
    return len(queens), ways

