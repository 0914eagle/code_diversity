
def solve(board):
    # Initialize the spread for Mirko and Slavko as 0
    mirko_spread, slavko_spread = 0, 0

    # Loop through each row of the board
    for i in range(len(board)):
        # Loop through each column of the board
        for j in range(len(board[0])):
            # If the current cell is Mirko's piece, calculate its spread
            if board[i][j] == "M":
                # Calculate the spread for Mirko's piece
                mirko_spread += calculate_spread(board, i, j, "M")
            # If the current cell is Slavko's piece, calculate its spread
            elif board[i][j] == "S":
                # Calculate the spread for Slavko's piece
                slavko_spread += calculate_spread(board, i, j, "S")

    # Return the spread for Mirko and Slavko
    return mirko_spread, slavko_spread

# Calculate the spread for a given piece
def calculate_spread(board, i, j, piece):
    # Initialize the spread for the piece as 0
    spread = 0

    # Loop through all the neighboring cells
    for x in range(i-1, i+2):
        for y in range(j-1, j+2):
            # If the current cell is empty or has the same piece, skip it
            if board[x][y] == "." or board[x][y] == piece:
                continue
            # Calculate the distance between the current cell and the piece
            distance = abs(i-x) + abs(j-y)
            # Add the distance to the spread
            spread += distance

    # Return the spread for the piece
    return spread

# Main function for testing
def main():
    # Read the input board
    board = []
    for _ in range(int(input())):
        board.append(input())

    # Solve the problem
    mirko_spread, slavko_spread = solve(board)

    # Print the output
    print(mirko_spread, slavko_spread)

if __name__ == "__main__":
    main()

