
def solve(n, m, p, board):
    # Initialize a list to store the moves
    moves = []

    # Loop through each row
    for i in range(n):
        # Loop through each column
        for j in range(m):
            # If the current square is not equal to the prime number, add 1 to it
            if board[i][j] != p:
                board[i][j] += 1
            # If the current square is equal to the prime number, wrap around to 1
            else:
                board[i][j] = 1

            # Add the current square to the moves list
            moves.append(board[i][j])

    # If all squares show the prime number, return the moves list
    if all(square == p for row in board for square in row):
        return moves
    # Otherwise, return -1
    else:
        return -1

