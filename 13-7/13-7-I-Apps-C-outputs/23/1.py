
def is_possible(N, M, B, target_board):
    # Initialize the initial board
    initial_board = [["." for _ in range(M)] for _ in range(N)]
    initial_board[1][1] = "X"

    # Initialize the moves list
    moves = []

    # Loop through the target board
    for block in target_board:
        # Get the row and column of the block
        row, col = block

        # Check if the block is already in the initial board
        if initial_board[row][col] == "X":
            continue

        # Check if the block is at the edge of the board
        if row == 1 or row == N or col == 1 or col == M:
            # Add a new block to the initial board
            initial_board[row][col] = "X"
            # Add the move to the moves list
            moves.append((row, col))
        else:
            # Check if the block is connected to any existing block
            for r in range(row-1, row+2):
                for c in range(col-1, col+2):
                    if initial_board[r][c] == "X":
                        # Add a new block to the initial board
                        initial_board[row][col] = "X"
                        # Add the move to the moves list
                        moves.append((row, col))
                        break

    # Check if the initial board is the same as the target board
    for i in range(N):
        for j in range(M):
            if initial_board[i][j] != target_board[i][j]:
                return False

    # Return the moves list
    return moves

def main():
    N, M, B = map(int, input().split())
    target_board = []
    for _ in range(B):
        row, col = map(int, input().split())
        target_board.append((row, col))
    moves = is_possible(N, M, B, target_board)
    if moves:
        print("possible")
        for move in moves:
            print(move[0], move[1])
    else:
        print("impossible")

if __name__ == '__main__':
    main()

