
def chess_spread(board):
    # Initialize the spread for both players to 0
    mirko_spread = 0
    slavko_spread = 0
    
    # Loop through each row of the board
    for i in range(len(board)):
        # Loop through each column of the current row
        for j in range(len(board[i])):
            # Check if the current field is occupied by Mirko's piece
            if board[i][j] == "M":
                # Increment the spread for Mirko's piece
                mirko_spread += 1
                # Check if the current field is occupied by Slavko's piece
            elif board[i][j] == "S":
                # Increment the spread for Slavko's piece
                slavko_spread += 1
    
    # Return the spread for both players
    return mirko_spread, slavko_spread

