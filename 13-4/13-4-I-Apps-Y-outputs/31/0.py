
def eight_queens_puzzle(n, positions):
    # Initialize a 2D array to represent the chessboard
    board = [[0 for _ in range(n)] for _ in range(n)]

    # Place the queens on the board
    for i in range(n):
        board[positions[i][0]][positions[i][1]] = 1

    # Check if any two queens attack each other
    for i in range(n):
        for j in range(i+1, n):
            if board[positions[i][0]][positions[j][1]] == 1 or board[positions[j][0]][positions[i][1]] == 1:
                return "INCORRECT"

    return "CORRECT"

