
def get_spread(board):
    # Initialize the spread for both players to 0
    mirko_spread, slavko_spread = 0, 0

    # Loop through each row and column of the board
    for i in range(len(board)):
        for j in range(len(board[0])):
            # If the current cell is occupied by Mirko's piece, calculate its spread
            if board[i][j] == "M":
                # Calculate the spread for Mirko's piece by looping through all adjacent cells
                for x in range(i-1, i+2):
                    for y in range(j-1, j+2):
                        # If the adjacent cell is empty or occupied by Slavko's piece, increase the spread
                        if x >= 0 and x < len(board) and y >= 0 and y < len(board[0]) and (board[x][y] == "." or board[x][y] == "S"):
                            mirko_spread += 1

            # If the current cell is occupied by Slavko's piece, calculate its spread
            if board[i][j] == "S":
                # Calculate the spread for Slavko's piece by looping through all adjacent cells
                for x in range(i-1, i+2):
                    for y in range(j-1, j+2):
                        # If the adjacent cell is empty or occupied by Mirko's piece, increase the spread
                        if x >= 0 and x < len(board) and y >= 0 and y < len(board[0]) and (board[x][y] == "." or board[x][y] == "M"):
                            slavko_spread += 1

    # Return the spread for both players
    return mirko_spread, slavko_spread

def read_input():
    # Read the number of rows and columns from the first line of input
    rows, cols = map(int, input().split())

    # Initialize the board with empty cells
    board = [["." for _ in range(cols)] for _ in range(rows)]

    # Read the board from the remaining lines of input
    for i in range(rows):
        board[i] = list(input())

    # Return the board
    return board

def main():
    # Read the board from input
    board = read_input()

    # Calculate the spread for both players
    mirko_spread, slavko_spread = get_spread(board)

    # Print the spread for both players
    print(mirko_spread, slavko_spread)

if __name__ == '__main__':
    main()

