
def get_spread(board):
    # Initialize the spread for both players to 0
    mirko_spread = 0
    slavko_spread = 0
    
    # Loop through each row of the board
    for row in board:
        # Loop through each column of the current row
        for col in range(len(row)):
            # If the current field is occupied by Mirko's piece, calculate its spread
            if row[col] == "M":
                # Calculate the spread by summing the distances to all other pieces
                mirko_spread += sum(abs(row_idx - row) + abs(col_idx - col) for row_idx, col_idx in enumerate(row) if row_idx != col_idx and row_idx != row and col_idx != col)
            # If the current field is occupied by Slavko's piece, calculate its spread
            elif row[col] == "S":
                # Calculate the spread by summing the distances to all other pieces
                slavko_spread += sum(abs(row_idx - row) + abs(col_idx - col) for row_idx, col_idx in enumerate(row) if row_idx != col_idx and row_idx != row and col_idx != col)
    
    # Return the spread for both players
    return mirko_spread, slavko_spread

