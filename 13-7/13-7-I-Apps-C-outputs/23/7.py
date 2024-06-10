
def is_possible(board_size, target_board):
    # Initialize a set to store the positions of the blocks in the target board
    target_positions = set()
    for block in target_board:
        target_positions.add(tuple(block))
    
    # Initialize a set to store the positions of the blocks in the current board
    current_positions = set()
    current_positions.add((1, 1))
    
    # Initialize a queue to store the moves to be performed
    moves = []
    
    # Loop until the target positions and current positions are the same
    while target_positions != current_positions:
        # Get the current position with the minimum distance to the target positions
        current_position = min(current_positions, key=lambda pos: len(target_positions - {pos}))
        
        # Get the moves that can be performed from the current position
        moves_from_current_position = get_moves_from_position(current_position, board_size)
        
        # Filter the moves that are not in the target positions
        filtered_moves = [move for move in moves_from_current_position if tuple(move[1]) in target_positions]
        
        # If there are no moves that can be performed, return "impossible"
        if not filtered_moves:
            return "impossible"
        
        # Add the moves to the queue
        moves.extend(filtered_moves)
        
        # Update the current positions
        current_positions.update([tuple(move[1]) for move in filtered_moves])
    
    # If the target positions and current positions are the same, return "possible" and the moves
    return "possible", moves

def get_moves_from_position(position, board_size):
    # Get the row and column of the current position
    row, col = position
    
    # Initialize a list to store the moves
    moves = []
    
    # Add moves from the current position
    if row > 1:
        moves.append(("^", [row-1, col]))
    if row < board_size:
        moves.append(("v", [row+1, col]))
    if col > 1:
        moves.append(("<", [row, col-1]))
    if col < board_size:
        moves.append((">", [row, col+1]))
    
    return moves

def main():
    board_size, target_board = map(int, input().split())
    target_board = [list(map(int, input().split())) for _ in range(target_board)]
    result = is_possible(board_size, target_board)
    if result == "impossible":
        print("impossible")
    else:
        print("possible")
        for move in result[1]:
            print(move[0], move[1])

if __name__ == '__main__':
    main()

