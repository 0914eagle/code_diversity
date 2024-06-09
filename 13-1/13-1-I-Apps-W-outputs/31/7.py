
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
    
    # If the queue is empty and no solution is found, return "NO"
    return "NO"

def get_moves(grid):
    # Get the empty cell coordinates
    empty_row, empty_col = get_empty_cell(grid)
    
    # Get the possible moves for the empty cell
    moves = []
    if empty_row > 0:
        moves.append(swap_cells(grid, empty_row, empty_col, empty_row - 1, empty_col))
    if empty_row < 2:
        moves.append(swap_cells(grid, empty_row, empty_col, empty_row + 1, empty_col))
    if empty_col > 0:
        moves.append(swap_cells(grid, empty_row, empty_col, empty_row, empty_col - 1))
    if empty_col < 2:
        moves.append(swap_cells(grid, empty_row, empty_col, empty_row, empty_col + 1))
    
    return moves

def get_empty_cell(grid):
    for row in range(2):
        for col in range(2):
            if grid[row][col] == "X":
                return row, col
    return -1, -1

def swap_cells(grid, row1, col1, row2, col2):
    grid[row1][col1], grid[row2][col2] = grid[row2][col2], grid[row1][col1]
    return grid

if __name__ == '__main__':
    bessie_grid = [input().split() for _ in range(2)]
    elsie_grid = [input().split() for _ in range(2)]
    print(f1(bessie_grid, elsie_grid))

