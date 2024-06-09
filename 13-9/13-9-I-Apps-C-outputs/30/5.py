
def is_valid_move(grid, row, col, direction):
    # Check if the move is valid
    if direction == "u":
        if row == 0:
            return False
        if grid[row - 1][col] != "E":
            return False
    elif direction == "d":
        if row == len(grid) - 1:
            return False
        if grid[row + 1][col] != "E":
            return False
    elif direction == "l":
        if col == 0:
            return False
        if grid[row][col - 1] != "E":
            return False
    elif direction == "r":
        if col == len(grid[0]) - 1:
            return False
        if grid[row][col + 1] != "E":
            return False
    return True

def make_move(grid, row, col, direction):
    # Make the move and return the new grid
    if direction == "u":
        grid[row - 1][col], grid[row][col] = grid[row][col], grid[row - 1][col]
    elif direction == "d":
        grid[row + 1][col], grid[row][col] = grid[row][col], grid[row + 1][col]
    elif direction == "l":
        grid[row][col - 1], grid[row][col] = grid[row][col], grid[row][col - 1]
    elif direction == "r":
        grid[row][col + 1], grid[row][col] = grid[row][col], grid[row][col + 1]
    return grid

def get_shortcuts(grid):
    # Get the shortcuts from the grid
    shortcuts = {}
    for row in grid:
        for col, char in enumerate(row):
            if char.isupper():
                shortcuts[char] = row[col + 1:]
                break
    return shortcuts

def get_moves(grid, row, col, direction):
    # Get the moves for the current position
    moves = []
    if is_valid_move(grid, row, col, direction):
        moves.append(direction)
    return moves

def solve(grid):
    # Solve the problem
    shortcuts = get_shortcuts(grid)
    moves = []
    for row in range(len(grid)):
        for col in range(len(grid[0])):
            if grid[row][col].isupper():
                moves.extend(get_moves(grid, row, col, shortcuts[grid[row][col]]))
    return " ".join(moves)

