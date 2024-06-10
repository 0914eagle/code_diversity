
def sliding_blocks(N, M, B, blocks):
    # Initialize the board
    board = [[0] * M for _ in range(N)]
    board[blocks[0][0] - 1][blocks[0][1] - 1] = 1

    # Initialize the moves
    moves = []

    # Loop through the blocks
    for i in range(1, B):
        # Get the current block
        block = blocks[i]

        # Find the block to the left
        for j in range(block[1] - 1, 0, -1):
            if board[block[0] - 1][j - 1] == 1:
                moves.append((">", block[0]))
                break
        else:
            moves.append(("<", block[0]))

        # Find the block to the right
        for j in range(block[1] + 1, M + 1):
            if board[block[0] - 1][j - 1] == 1:
                moves.append(("<", block[0])
                break
        else:
            moves.append((">", block[0]))

        # Find the block above
        for j in range(block[0] - 1, 0, -1):
            if board[j - 1][block[1] - 1] == 1:
                moves.append(("^", block[1]))
                break
        else:
            moves.append(("v", block[1]))

        # Find the block below
        for j in range(block[0] + 1, N + 1):
            if board[j - 1][block[1] - 1] == 1:
                moves.append(("v", block[1]))
                break
        else:
            moves.append(("^", block[1]))

        # Make the move
        board[block[0] - 1][block[1] - 1] = 1

    # Check if the board is solved
    if board == blocks:
        return "possible\n" + "\n".join(moves)
    else:
        return "impossible"

if __name__ == '__main__':
    N, M, B = map(int, input().split())
    blocks = []
    for _ in range(B):
        blocks.append(list(map(int, input().split())))
    print(sliding_blocks(N, M, B, blocks))

