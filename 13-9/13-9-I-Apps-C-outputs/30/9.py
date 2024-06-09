
def is_valid_move(grid, row, col):
    # Check if the move is valid by checking if the space is empty and if the organ is within the bounds of the grid
    return grid[row][col] == "E" and 0 <= row < len(grid) and 0 <= col < len(grid[0])

def get_moves(grid):
    # Initialize the moves list
    moves = []
    
    # Loop through each row of the grid
    for row in range(len(grid)):
        # Loop through each column of the current row
        for col in range(len(grid[0])):
            # Check if the current space is empty
            if grid[row][col] == "E":
                # Check if the current space is on the leftmost, rightmost, or centermost column
                if col == 0 or col == len(grid[0]) - 1 or col == len(grid[0]) // 2:
                    # Check if the space above the current space is empty
                    if is_valid_move(grid, row - 1, col):
                        moves.append("u")
                    # Check if the space below the current space is empty
                    if is_valid_move(grid, row + 1, col):
                        moves.append("d")
                # Check if the space to the left of the current space is empty
                if is_valid_move(grid, row, col - 1):
                    moves.append("l")
                # Check if the space to the right of the current space is empty
                if is_valid_move(grid, row, col + 1):
                    moves.append("r")
    
    return moves

def get_shortcuts(grid):
    # Initialize the shortcuts dictionary
    shortcuts = {}
    
    # Loop through each row of the grid
    for row in range(len(grid)):
        # Loop through each column of the current row
        for col in range(len(grid[0])):
            # Check if the current space is empty
            if grid[row][col] == "E":
                # Check if the current space is on the leftmost, rightmost, or centermost column
                if col == 0 or col == len(grid[0]) - 1 or col == len(grid[0]) // 2:
                    # Check if the space above the current space is empty
                    if is_valid_move(grid, row - 1, col):
                        shortcuts["I"] = "lldll"
                    # Check if the space below the current space is empty
                    if is_valid_move(grid, row + 1, col):
                        shortcuts["D"] = "R"
                # Check if the space to the left of the current space is empty
                if is_valid_move(grid, row, col - 1):
                    shortcuts["S"] = "rr"
                # Check if the space to the right of the current space is empty
                if is_valid_move(grid, row, col + 1):
                    shortcuts["R"] = "SrS"
    
    return shortcuts

def solve(grid):
    # Get the moves
    moves = get_moves(grid)
    
    # Get the shortcuts
    shortcuts = get_shortcuts(grid)
    
    # Initialize the solution
    solution = ""
    
    # Loop through each move
    for move in moves:
        # Check if the move is a shortcut
        if move in shortcuts:
            # Add the shortcut to the solution
            solution += move + " " + shortcuts[move] + " "
        # If the move is not a shortcut, add it to the solution
        else:
            solution += move + " "
    
    return solution.strip()

