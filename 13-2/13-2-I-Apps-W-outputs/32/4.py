
def solve(n, m, rooks):
    # Initialize a 2D array to store the board state
    board = [[0] * n for _ in range(n)]

    # Iterate through each rook and mark its row and column as attacked
    for i in range(m):
        x, y = rooks[i]
        board[x - 1][y - 1] = 1
        for j in range(n):
            if board[j][y - 1] == 0:
                board[j][y - 1] = 1
        for k in range(n):
            if board[x - 1][k] == 0:
                board[x - 1][k] = 1

    # Count the number of unattacked cells
    count = 0
    for i in range(n):
        for j in range(n):
            if board[i][j] == 0:
                count += 1

    return count

