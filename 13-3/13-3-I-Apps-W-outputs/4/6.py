
def count_bishwocks(board):
    # Initialize a set to store the positions of the bishwocks
    bishwocks = set()
    # Iterate through the board
    for i in range(len(board)):
        for j in range(len(board[0])):
            # Check if the current position is empty and not occupied by a pawn
            if board[i][j] == "0" and (i == 0 or board[i-1][j] == "0") and (j == 0 or board[i][j-1] == "0"):
                # Add the current position to the set of bishwocks
                bishwocks.add((i, j))
    # Return the number of bishwocks
    return len(bishwocks)

def main():
    board = [
        [0, 0, 0, 0],
        [0, 0, 0, 0],
        [0, 0, 0, 0],
        [0, 0, 0, 0]
    ]
    print(count_bishwocks(board))

if __name__ == '__main__':
    main()

