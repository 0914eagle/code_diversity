
def is_possible(initial_board, target_board):
    # Initialize a set to store the positions of the blocks in the target board
    target_positions = set()
    for block in target_board:
        target_positions.add(block)
    
    # Initialize a queue to store the positions of the blocks to be moved
    queue = [initial_board[0]]
    
    # Loop until the queue is empty
    while queue:
        # Dequeue a block from the queue
        block = queue.pop(0)
        
        # If the block is in the target board, remove it from the target positions set
        if block in target_positions:
            target_positions.remove(block)
        
        # If the target positions set is empty, return True
        if not target_positions:
            return True
        
        # Get the neighbors of the block
        neighbors = get_neighbors(block, initial_board)
        
        # Add the neighbors to the queue if they are not in the target positions set
        for neighbor in neighbors:
            if neighbor not in target_positions:
                queue.append(neighbor)
    
    # If the queue is empty and the target positions set is not empty, return False
    return False

def get_neighbors(block, board):
    # Get the row and column of the block
    row, col = block
    
    # Get the neighbors of the block
    neighbors = []
    if row > 0:
        neighbors.append((row-1, col))
    if row < len(board)-1:
        neighbors.append((row+1, col))
    if col > 0:
        neighbors.append((row, col-1))
    if col < len(board[0])-1:
        neighbors.append((row, col+1))
    
    return neighbors

def main():
    # Read the input
    N, M, B = map(int, input().split())
    target_board = []
    for _ in range(B):
        r, c = map(int, input().split())
        target_board.append((r-1, c-1))
    
    # Initialize the initial board
    initial_board = []
    for _ in range(N):
        initial_board.append([])
    
    # Add the block at the second row and third column
    initial_board[1].append(2)
    
    # Determine if it is possible to make the initial board become exactly the same as the target board
    if is_possible(initial_board, target_board):
        print("possible")
    else:
        print("impossible")

if __name__ == '__main__':
    main()

