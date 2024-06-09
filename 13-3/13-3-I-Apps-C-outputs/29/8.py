
def solve(n, m, p, board):
    # Initialize a list to store the moves
    moves = []

    # Loop through each row
    for i in range(n):
        # Loop through each column
        for j in range(m):
            # If the current square is not the prime number, skip it
            if board[i][j] != p:
                # Add the current square to the moves list
                moves.append(board[i][j])
                # Update the current square to the next number in the row and column
                board[i][j] = (board[i][j] + 1) % p

    # If all squares show the prime number, return the moves list
    if all(board[i][j] == p for i in range(n) for j in range(m)):
        return moves
    else:
        # If no winning sequence exists, return -1
        return -1

