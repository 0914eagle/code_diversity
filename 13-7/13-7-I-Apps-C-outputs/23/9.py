
def is_possible(initial_board, target_board):
    # Initialize a set to store the positions of the blocks in the initial board
    initial_blocks = set()
    for row in initial_board:
        for col in row:
            if col == "X":
                initial_blocks.add((row, col))
    
    # Initialize a set to store the positions of the blocks in the target board
    target_blocks = set()
    for row in target_board:
        for col in row:
            if col == "X":
                target_blocks.add((row, col))
    
    # If the number of blocks in the initial board is not equal to the number of blocks in the target board, return "impossible"
    if len(initial_blocks) != len(target_blocks):
        return "impossible"
    
    # Initialize a set to store the moves that need to be performed
    moves = set()
    
    # Loop through each block in the initial board
    for block in initial_blocks:
        # If the block is not in the target board, return "impossible"
        if block not in target_blocks:
            return "impossible"
        # If the block is in the target board, find the shortest path from the block to any other block in the target board
        path = find_path(block, target_blocks)
        # If the path is not found, return "impossible"
        if not path:
            return "impossible"
        # Add the moves to the set of moves that need to be performed
        moves.update(path)
    
    # If all the blocks are in their target positions, return "possible" and the moves that need to be performed
    return "possible", moves

def find_path(block, target_blocks):
    # Initialize a set to store the positions of the blocks that have been visited
    visited = set()
    # Initialize a queue to store the positions of the blocks that need to be visited
    queue = [block]
    # Loop until the queue is empty
    while queue:
        # Get the current block from the queue
        current_block = queue.pop(0)
        # If the current block is not in the target board, return False
        if current_block not in target_blocks:
            return False
        # If the current block is in the target board and has not been visited, mark it as visited and add it to the set of visited blocks
        if current_block not in visited:
            visited.add(current_block)
        # Add the neighbors of the current block to the queue
        for neighbor in get_neighbors(current_block):
            queue.append(neighbor)
    # If all the blocks have been visited, return the set of moves that need to be performed
    return visited

def get_neighbors(block):
    # Get the row and column of the block
    row, col = block
    # Initialize a list to store the neighbors of the block
    neighbors = []
    # If the block is not on the edge of the board, add the neighboring blocks to the list of neighbors
    if row > 1:
        neighbors.append((row-1, col))
    if row < N:
        neighbors.append((row+1, col))
    if col > 1:
        neighbors.append((row, col-1))
    if col < M:
        neighbors.append((row, col+1))
    return neighbors

if __name__ == '__main__':
    N, M, B = map(int, input().split())
    initial_board = [input() for _ in range(N)]
    target_board = [input() for _ in range(N)]
    print(is_possible(initial_board, target_board))

