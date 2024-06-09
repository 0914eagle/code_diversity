
def solve(R, C, board):
    # Initialize the spread for Mirko and Slavko to 0
    mirko_spread, slavko_spread = 0, 0

    # Loop through each row and column
    for i in range(R):
        for j in range(C):
            # If the current field is Mirko's piece, calculate its spread
            if board[i][j] == "M":
                # Calculate the spread for Mirko's piece
                mirko_spread += calculate_spread(board, i, j, "M")
            # If the current field is Slavko's piece, calculate its spread
            elif board[i][j] == "S":
                # Calculate the spread for Slavko's piece
                slavko_spread += calculate_spread(board, i, j, "S")

    # Return the spread for Mirko and Slavko
    return mirko_spread, slavko_spread

# Calculate the spread for a piece
def calculate_spread(board, i, j, piece):
    # Initialize the spread to 0
    spread = 0

    # Loop through all the neighbors of the current field
    for x in range(i-1, i+2):
        for y in range(j-1, j+2):
            # If the neighbor is outside the board, continue
            if x < 0 or x >= R or y < 0 or y >= C:
                continue
            # If the neighbor is empty, continue
            if board[x][y] == ".":
                continue
            # If the neighbor is the same piece, continue
            if board[x][y] == piece:
                continue
            # Calculate the distance between the current piece and the neighbor
            distance = abs(i-x) + abs(j-y)
            # Add the distance to the spread
            spread += distance

    # Return the spread
    return spread

# Test the solve function
R, C = map(int, input().split())
board = [input() for _ in range(R)]
print(solve(R, C, board))

