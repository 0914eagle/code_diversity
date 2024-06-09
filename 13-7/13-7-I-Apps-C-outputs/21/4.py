
def get_spread(board):
    # Initialize the spread for Mirko and Slavko to 0
    mirko_spread = 0
    slavko_spread = 0
    
    # Loop through each row of the board
    for i in range(len(board)):
        # Loop through each column of the current row
        for j in range(len(board[i])):
            # If the current cell is Mirko's piece, increment his spread
            if board[i][j] == "M":
                mirko_spread += 1
            # If the current cell is Slavko's piece, increment his spread
            elif board[i][j] == "S":
                slavko_spread += 1
    
    # Return the spread for both players
    return mirko_spread, slavko_spread

