
def is_valid_move(grid, row, col):
    # Check if the move is valid
    if row < 0 or row >= len(grid) or col < 0 or col >= len(grid[0]):
        return False
    if grid[row][col] == "E":
        return True
    return False

def get_moves(grid):
    # Initialize the list of moves
    moves = []
    
    # Loop through the grid and find the empty space
    for row in range(len(grid)):
        for col in range(len(grid[0])):
            if grid[row][col] == "E":
                # Found the empty space, now find the organs around it
                for r in range(row-1, row+2):
                    for c in range(col-1, col+2):
                        if is_valid_move(grid, r, c) and grid[r][c] != "E":
                            # Add the move to the list of moves
                            moves.append((r, c))
    
    return moves

def solve(grid):
    # Get the list of moves
    moves = get_moves(grid)
    
    # Check if there are any moves
    if len(moves) == 0:
        return "SURGERY FAILED"
    
    # Sort the moves by row and column
    moves = sorted(moves, key=lambda x: (x[0], x[1]))
    
    # Initialize the sequence of moves
    seq = ""
    
    # Loop through the moves and add them to the sequence
    for move in moves:
        row, col = move
        if row == 0:
            seq += "u"
        elif row == len(grid) - 1:
            seq += "d"
        elif col == 0:
            seq += "l"
        else:
            seq += "r"
    
    return "SURGERY COMPLETE\n" + seq

