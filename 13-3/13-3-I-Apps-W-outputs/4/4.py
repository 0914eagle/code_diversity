
def count_bishocks(board):
    # Initialize a set to store the positions of the bishocks
    bishocks = set()
    # Iterate through the board
    for i in range(len(board)):
        for j in range(len(board[0])):
            # Check if the current position is empty
            if board[i][j] == "0":
                # Check if the current position is adjacent to a pawn
                if i > 0 and board[i-1][j] == "X":
                    continue
                if j > 0 and board[i][j-1] == "X":
                    continue
                if i < len(board)-1 and board[i+1][j] == "X":
                    continue
                if j < len(board[0])-1 and board[i][j+1] == "X":
                    continue
                # If the current position is empty and not adjacent to a pawn, add it to the set of bishocks
                bishocks.add((i, j))
    # Return the number of bishocks
    return len(bishocks)

def main():
    board = [
        [0, 0, 0, 0],
        [0, 0, 0, 0],
        [0, 0, 0, 0],
        [0, 0, 0, 0]
    ]
    print(count_bishocks(board))

if __name__ == '__main__':
    main()

