
def get_spread(board):
    # Initialize the spread for both players to 0
    mirko_spread = 0
    slavko_spread = 0

    # Loop through each row of the board
    for row in board:
        # Loop through each column of the current row
        for col in range(len(row)):
            # If the current cell is Mirko's piece, update their spread
            if row[col] == "M":
                mirko_spread += get_distance(board, row, col, "M")
            # If the current cell is Slavko's piece, update their spread
            elif row[col] == "S":
                slavko_spread += get_distance(board, row, col, "S")

    # Return the spread for both players
    return mirko_spread, slavko_spread

# Function to get the distance between a piece and all other pieces of the same player
def get_distance(board, row, col, player):
    # Initialize the distance to 0
    distance = 0

    # Loop through each row of the board
    for i in range(len(board)):
        # Loop through each column of the current row
        for j in range(len(board[i])):
            # If the current cell is empty or belongs to the other player, skip it
            if board[i][j] == "." or board[i][j] != player:
                continue
            # Calculate the distance between the current cell and the piece
            distance += abs(i - row) + abs(j - col)

    # Return the total distance
    return distance

