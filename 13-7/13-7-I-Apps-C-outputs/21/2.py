
def get_spread(board):
    # Initialize the spread for Mirko and Slavko as 0
    mirko_spread, slavko_spread = 0, 0

    # Loop through each row of the board
    for i in range(len(board)):
        # Loop through each column of the board
        for j in range(len(board[0])):
            # Check if the current field is empty
            if board[i][j] == ".":
                continue

            # Get the current piece and its position
            piece = board[i][j]
            position = (i, j)

            # If the current piece is Mirko's, calculate its spread
            if piece == "M":
                # Loop through all the adjacent fields
                for x in range(i-1, i+2):
                    for y in range(j-1, j+2):
                        # Check if the adjacent field is empty or has a Slavko's piece
                        if x >= 0 and x < len(board) and y >= 0 and y < len(board[0]) and (board[x][y] == "." or board[x][y] == "S"):
                            # Calculate the distance between the current piece and the adjacent field
                            distance = abs(position[0] - x) + abs(position[1] - y)
                            # Update the spread for Mirko
                            mirko_spread += distance

            # If the current piece is Slavko's, calculate its spread
            if piece == "S":
                # Loop through all the adjacent fields
                for x in range(i-1, i+2):
                    for y in range(j-1, j+2):
                        # Check if the adjacent field is empty or has a Mirko's piece
                        if x >= 0 and x < len(board) and y >= 0 and y < len(board[0]) and (board[x][y] == "." or board[x][y] == "M"):
                            # Calculate the distance between the current piece and the adjacent field
                            distance = abs(position[0] - x) + abs(position[1] - y)
                            # Update the spread for Slavko
                            slavko_spread += distance

    # Return the spread for Mirko and Slavko
    return mirko_spread, slavko_spread

