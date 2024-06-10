
def get_spread(board):
    # Initialize the spread for both players to 0
    mirko_spread, slavko_spread = 0, 0
    
    # Loop through each row and column of the board
    for i in range(len(board)):
        for j in range(len(board[0])):
            # If the current cell is Mirko's piece, update his spread
            if board[i][j] == "M":
                mirko_spread += 1
            # If the current cell is Slavko's piece, update his spread
            elif board[i][j] == "S":
                slavko_spread += 1
    
    # Return the spread for both players
    return mirko_spread, slavko_spread

def main():
    # Read the input
    R, C = map(int, input().split())
    board = [input() for _ in range(R)]
    
    # Call the get_spread function to get the spread for both players
    mirko_spread, slavko_spread = get_spread(board)
    
    # Print the output
    print(mirko_spread, slavko_spread)

if __name__ == '__main__':
    main()

