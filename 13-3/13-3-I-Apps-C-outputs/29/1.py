
def solve(n, m, p, board):
    # Initialize a list to store the moves
    moves = []
    
    # Loop through each row and column
    for i in range(n):
        for j in range(m):
            # If the current square is not already filled with p, add 1 to it
            if board[i][j] != p:
                board[i][j] += 1
                moves.append(board[i][j])
            # If the current square is filled with p, wrap around to 1
            else:
                board[i][j] = 1
                moves.append(board[i][j])
    
    # Check if all squares are filled with p
    if all(all(row) for row in board):
        return moves
    else:
        return -1

