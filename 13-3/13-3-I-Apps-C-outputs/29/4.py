
def solve(n, m, p, board):
    # Initialize a list to store the moves
    moves = []
    
    # Loop through each row and column of the board
    for i in range(n):
        for j in range(m):
            # If the current square is not already filled with the winning number, add it to the moves list
            if board[i][j] != p:
                moves.append(board[i][j])
    
    # If all squares are filled with the winning number, return the moves list
    if len(moves) == n*m:
        return moves
    else:
        return -1

