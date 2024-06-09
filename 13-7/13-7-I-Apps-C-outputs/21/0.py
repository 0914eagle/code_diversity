
def get_spread(board):
    # Initialize the spread for Mirko and Slavko to 0
    mirko_spread, slavko_spread = 0, 0

    # Loop through each row of the board
    for i in range(len(board)):
        # Loop through each column of the board
        for j in range(len(board[i])):
            # Check if the current position is occupied by Mirko's piece
            if board[i][j] == "M":
                # Increment the spread for Mirko's piece
                mirko_spread += 1
                # Check if the current position is also occupied by Slavko's piece
                if board[i][j] == "S":
                    # Increment the spread for Slavko's piece
                    slavko_spread += 1

    # Return the spread for Mirko and Slavko
    return mirko_spread, slavko_spread

