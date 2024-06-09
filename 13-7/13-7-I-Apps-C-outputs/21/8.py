
def calculate_spread(board):
    # Initialize the spread for Mirko and Slavko to 0
    mirko_spread = 0
    slavko_spread = 0
    
    # Loop through each row of the board
    for i in range(len(board)):
        # Loop through each column of the board
        for j in range(len(board[i])):
            # If the current field is Mirko's piece, update the spread for Mirko
            if board[i][j] == "M":
                mirko_spread += 1
            # If the current field is Slavko's piece, update the spread for Slavko
            elif board[i][j] == "S":
                slavko_spread += 1
    
    # Return the spread for Mirko and Slavko
    return mirko_spread, slavko_spread

