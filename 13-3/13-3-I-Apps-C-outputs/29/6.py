
def solve(n, m, p, board):
    # Initialize a list to store the moves
    moves = []

    # Loop through each row
    for i in range(n):
        # Loop through each column
        for j in range(m):
            # If the current square is not already filled with the winning number, add it to the moves list
            if board[i][j] != p:
                moves.append(board[i][j])

    # If all squares are filled with the winning number, return the moves list
    if len(moves) == p * m * n:
        return moves

    # If no winning sequence exists, return -1
    return -1

