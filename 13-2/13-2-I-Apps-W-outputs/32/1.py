
def solve(n, m, positions):
    # Initialize a 2D array to store the board state
    board = [[0] * n for _ in range(n)]

    # Iterate through each position and mark the cells as under attack
    for i in range(m):
        x, y = positions[i]
        board[x - 1][y - 1] = 1

    # Count the number of cells that are not under attack
    count = 0
    for i in range(n):
        for j in range(n):
            if board[i][j] == 0:
                count += 1

    return count

