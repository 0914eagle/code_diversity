
def is_possible(N, M, B, target_board):
    # Initialize the initial board with the given block
    initial_board = [[0] * M for _ in range(N)]
    initial_board[target_board[0][0] - 1][target_board[0][1] - 1] = 1
    
    # Initialize the set of blocks that have been added to the board
    added_blocks = set([(target_board[0][0], target_board[0][1])])
    
    # Loop through the remaining blocks in the target board
    for i in range(1, B):
        # Get the current block and its coordinates
        block = target_board[i]
        row = block[0]
        col = block[1]
        
        # Check if the current block has already been added to the board
        if (row, col) in added_blocks:
            continue
        
        # Check if the current block is connected to any of the added blocks
        connected = False
        for added_block in added_blocks:
            if are_connected(row, col, added_block[0], added_block[1], N, M):
                connected = True
                break
        
        # If the current block is not connected to any added blocks, the goal is impossible
        if not connected:
            return False
        
        # Add the current block to the board and the set of added blocks
        initial_board[row - 1][col - 1] = 1
        added_blocks.add((row, col))
    
    # If all blocks in the target board have been added and they form a tree, the goal is possible
    return True

def are_connected(row1, col1, row2, col2, N, M):
    # Check if the blocks are next to each other
    if abs(row1 - row2) + abs(col1 - col2) == 1:
        return True
    
    # Check if the blocks are on the same row or column
    if row1 == row2 or col1 == col2:
        return True
    
    # Check if the blocks are on the diagonals
    if abs(row1 - row2) == abs(col1 - col2):
        return True
    
    # If none of the above conditions are met, the blocks are not connected
    return False

def get_moves(N, M, B, target_board):
    # Initialize the moves list
    moves = []
    
    # Loop through the target board and add the moves to the list
    for i in range(B):
        block = target_board[i]
        row = block[0]
        col = block[1]
        
        # Add a move to the left edge of the board
        if col > 1:
            moves.append(('<', col))
        
        # Add a move to the right edge of the board
        if col < M:
            moves.append('>', col)
        
        # Add a move to the top edge of the board
        if row > 1:
            moves.append('^', row)
        
        # Add a move to the bottom edge of the board
        if row < N:
            moves.append('v', row)
    
    # Return the moves list
    return moves

if __name__ == '__main__':
    N, M, B = map(int, input().split())
    target_board = []
    for i in range(B):
        target_board.append(list(map(int, input().split())))
    
    if is_possible(N, M, B, target_board):
        print("possible")
        for move in get_moves(N, M, B, target_board):
            print(move[0], move[1])
    else:
        print("impossible")

