
def f1(bessie_grid, elsie_grid):
    # Initialize a queue to store the states of the puzzles
    queue = [(bessie_grid, elsie_grid)]
    
    # Initialize a set to keep track of the visited states
    visited = set()
    
    # Loop until the queue is empty
    while queue:
        # Dequeue a state
        bessie_grid, elsie_grid = queue.pop(0)
        
        # If the states are the same, return "YES"
        if bessie_grid == elsie_grid:
            return "YES"
        
        # If the state has been visited before, skip it
        if (bessie_grid, elsie_grid) in visited:
            continue
        
        # Add the state to the visited set
        visited.add((bessie_grid, elsie_grid))
        
        # Get the possible moves for both puzzles
        bessie_moves = get_moves(bessie_grid)
        elsie_moves = get_moves(elsie_grid)
        
        # Add the new states to the queue
        for move in bessie_moves:
            queue.append((move, elsie_grid))
        for move in elsie_moves:
            queue.append((bessie_grid, move))
    
    # If the queue is empty and no matching state is found, return "NO"
    return "NO"

def get_moves(grid):
    # Get the indices of the empty cell
    empty_row, empty_col = [i for i, x in enumerate(grid) if x == "X"][0]
    
    # Get the indices of the non-empty cells
    non_empty_rows, non_empty_cols = [i for i, x in enumerate(grid) if x != "X"]
    
    # Get the possible moves for the puzzle
    moves = []
    for row in non_empty_rows:
        for col in non_empty_cols:
            # If the move is valid, add it to the list of moves
            if abs(row - empty_row) + abs(col - empty_col) == 1:
                moves.append(grid[:] + [grid[row][col]])
    
    return moves

if __name__ == '__main__':
    bessie_grid = ["AB", "XC"]
    elsie_grid = ["XB", "AC"]
    print(f1(bessie_grid, elsie_grid))

