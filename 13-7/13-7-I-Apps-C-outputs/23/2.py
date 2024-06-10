
def is_possible(N, M, B, target_board):
    # Initialize the current board with the initial board configuration
    current_board = [[0] * M for _ in range(N)]
    current_board[1][1] = 1

    # Initialize the list of moves
    moves = []

    # Loop through each block in the target board
    for r, c in target_board:
        # If the block is already in the current board, skip it
        if current_board[r][c] == 1:
            continue

        # Find the closest block in the current board to the target block
        closest_block = find_closest_block(current_board, r, c)

        # If there is no closest block, the target board is not possible
        if closest_block is None:
            return "impossible"

        # Add the new block to the current board
        current_board[r][c] = 1

        # Add the move to slide the new block to the moves list
        moves.append((closest_block[0], closest_block[1], r, c))

    # If we reach this point, the target board is possible
    return "possible", moves

def find_closest_block(board, r, c):
    # Find the closest block in the current board to the target block
    for i in range(r):
        for j in range(c):
            if board[i][j] == 1:
                return i, j
    return None

def main():
    N, M, B = map(int, input().split())
    target_board = []
    for _ in range(B):
        r, c = map(int, input().split())
        target_board.append((r, c))
    result = is_possible(N, M, B, target_board)
    if result == "impossible":
        print("impossible")
    else:
        print("possible")
        for move in result[1]:
            print(move[0], move[1], move[2], move[3])

if __name__ == '__main__':
    main()

