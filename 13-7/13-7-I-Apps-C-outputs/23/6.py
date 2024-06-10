
def is_possible(board, target_board):
    # Initialize a set to store the positions of the blocks in the target board
    target_positions = set()
    for block in target_board:
        target_positions.add(str(block[0]) + str(block[1]))
    
    # Initialize a set to store the positions of the blocks in the current board
    current_positions = set()
    for block in board:
        current_positions.add(str(block[0]) + str(block[1]))
    
    # If the sets are not equal, the goal is not possible
    if target_positions != current_positions:
        return "impossible"
    
    # If the sets are equal, check if the blocks are in a tree structure
    for block in target_board:
        # Check if the block is connected to any other block in the target board
        if not any(str(block[0]) + str(block[1]) in target_positions for block in target_board if block != block):
            return "impossible"
    
    # If all blocks are connected and the current board is equal to the target board, the goal is possible
    return "possible"

def get_moves(board, target_board):
    # Initialize a list to store the moves
    moves = []
    
    # Loop through the blocks in the target board
    for block in target_board:
        # Check if the block is not in the current board
        if str(block[0]) + str(block[1]) not in current_positions:
            # Add the move to the list
            moves.append(str(block[0]) + str(block[1]))
    
    # Return the list of moves
    return moves

if __name__ == '__main__':
    # Read the input
    N, M, B = map(int, input().split())
    board = []
    for _ in range(B):
        r, c = map(int, input().split())
        board.append((r, c))
    
    # Call the function to check if the goal is possible
    result = is_possible(board, target_board)
    print(result)
    
    # If the goal is possible, call the function to get the moves
    if result == "possible":
        moves = get_moves(board, target_board)
        for move in moves:
            print(move)

