
def solve(n, m, p, board):
    # Initialize a list to store the moves
    moves = []
    
    # Loop through each row
    for i in range(n):
        # Loop through each column
        for j in range(m):
            # If the current square is not filled, skip it
            if board[i][j] == 0:
                continue
            # If the current square is filled, add it to the moves list
            moves.append(board[i][j])
            # Update the board by adding 1 to all squares in the same row and column as the current square
            for k in range(n):
                for l in range(m):
                    if k == i or l == j:
                        board[k][l] = (board[k][l] + 1) % p
    
    # If all squares are filled, return the moves list
    if all(all(board[i]) for i in range(n)):
        return moves
    # Otherwise, return -1
    return -1

