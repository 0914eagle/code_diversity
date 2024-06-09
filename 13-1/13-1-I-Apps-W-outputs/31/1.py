
def is_bffl(bessie_puzzle, elsie_puzzle):
    # Initialize a queue to store the states of the puzzles
    queue = [(bessie_puzzle, elsie_puzzle)]
    
    # Initialize a set to keep track of the visited states
    visited = set()
    
    # Loop until the queue is empty
    while queue:
        # Dequeue a state from the queue
        bessie_puzzle, elsie_puzzle = queue.pop(0)
        
        # If the states are the same, return True
        if bessie_puzzle == elsie_puzzle:
            return True
        
        # If the state has already been visited, skip it
        if (bessie_puzzle, elsie_puzzle) in visited:
            continue
        
        # Add the state to the visited set
        visited.add((bessie_puzzle, elsie_puzzle))
        
        # Get the possible moves for both puzzles
        bessie_moves = get_moves(bessie_puzzle)
        elsie_moves = get_moves(elsie_puzzle)
        
        # Add the moves to the queue
        for move in bessie_moves:
            queue.append((move, elsie_puzzle))
        for move in elsie_moves:
            queue.append((bessie_puzzle, move))
    
    # If the queue is empty and the states are not the same, return False
    return False

def get_moves(puzzle):
    # Get the empty cell coordinates
    empty_row, empty_col = get_empty_cell(puzzle)
    
    # Get the possible moves for the puzzle
    moves = []
    if empty_row > 0:
        moves.append(swap_rows(puzzle, empty_row, empty_row - 1))
    if empty_row < 1:
        moves.append(swap_rows(puzzle, empty_row, empty_row + 1))
    if empty_col > 0:
        moves.append(swap_cols(puzzle, empty_col, empty_col - 1))
    if empty_col < 1:
        moves.append(swap_cols(puzzle, empty_col, empty_col + 1))
    
    return moves

def swap_rows(puzzle, row1, row2):
    return [row[:] for row in puzzle]

def swap_cols(puzzle, col1, col2):
    return [[puzzle[row][col1] for row in range(2)] for col in range(2)]

def get_empty_cell(puzzle):
    for row in range(2):
        for col in range(2):
            if puzzle[row][col] == 'X':
                return row, col
    return None, None

if __name__ == '__main__':
    bessie_puzzle = [input().split() for _ in range(2)]
    elsie_puzzle = [input().split() for _ in range(2)]
    print("YES") if is_bffl(bessie_puzzle, elsie_puzzle) else print("NO")

