
def solve(board, target):
    # Initialize a set to store the positions of the blocks in the target board
    target_positions = set()
    for block in target:
        target_positions.add((block[0], block[1]))
    
    # Initialize a set to store the positions of the blocks in the current board
    current_positions = set()
    for row in range(len(board)):
        for col in range(len(board[0])):
            if board[row][col] == 'X':
                current_positions.add((row, col))
    
    # Initialize a queue to store the moves to be performed
    queue = []
    
    # Add the initial move to the queue
    queue.append(('<', 1))
    
    # Loop until the queue is empty
    while queue:
        # Get the move from the queue
        move = queue.pop(0)
        
        # Perform the move on the current board
        if move[0] == '<':
            # Slide the new block from the right edge of the board towards the left
            current_positions.add((move[1]-1, len(board[0])-1))
        elif move[0] == '>':
            # Slide the new block from the left edge of the board towards the right
            current_positions.add((move[1], 0))
        elif move[0] == '^':
            # Slide the new block from the bottom edge of the board upward
            current_positions.add((len(board)-1, move[1]))
        elif move[0] == 'v':
            # Slide the new block from the top edge of the board downward
            current_positions.add((0, move[1]))
        
        # Check if the current board matches the target board
        if current_positions == target_positions:
            # Return the moves if the current board matches the target board
            return queue
        
        # Add the new moves to the queue
        for row in range(len(board)):
            for col in range(len(board[0])):
                if (row, col) in current_positions:
                    # Add the moves for the block at the current position
                    if row > 0 and (row-1, col) not in current_positions:
                        queue.append(('<', row))
                    if col > 0 and (row, col-1) not in current_positions:
                        queue.append(('^', col))
                    if row < len(board)-1 and (row+1, col) not in current_positions:
                        queue.append('>', row)
                    if col < len(board[0])-1 and (row, col+1) not in current_positions:
                        queue.append('v', col)
    
    # Return "impossible" if the current board does not match the target board
    return "impossible"

def main():
    board = [
        ['.', '.', '.', '.'],
        ['.', 'X', '.', '.'],
        ['.', '.', '.', '.'],
        ['.', '.', '.', '.'],
    ]
    target = [
        (1, 1),
        (1, 2),
        (2, 2),
        (2, 3),
        (3, 3),
        (3, 4),
    ]
    print(solve(board, target))

if __name__ == '__main__':
    main()

