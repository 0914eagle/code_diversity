
def solve(board):
    # Initialize the minimum number of steps to -1
    min_steps = -1
    # Initialize the current position of the knight
    curr_pos = (len(board), len(board[0]))
    # Initialize a set to store the visited cells
    visited = set()
    # Initialize a queue to store the cells to be visited
    queue = [(curr_pos, 0)]
    # Loop until the queue is empty
    while queue:
        # Get the current cell and the number of steps
        curr_cell, steps = queue.pop(0)
        # If the current cell is (1, 1), return the number of steps
        if curr_cell == (1, 1):
            return steps
        # If the current cell is not visited, mark it as visited and add it to the visited set
        if curr_cell not in visited:
            visited.add(curr_cell)
            # Get the valid moves for the current cell
            valid_moves = get_valid_moves(board, curr_cell)
            # Loop through the valid moves
            for move in valid_moves:
                # If the move is not visited, add it to the queue with the number of steps incremented by 1
                if move not in visited:
                    queue.append((move, steps + 1))
    # If the queue is empty and the minimum number of steps is still -1, return -1
    return min_steps

# Function to get the valid moves for a given cell
def get_valid_moves(board, cell):
    # Get the row and column of the cell
    row, col = cell
    # Initialize a list to store the valid moves
    valid_moves = []
    # Loop through the possible moves
    for r in range(row - 2, row + 3):
        for c in range(col - 2, col + 3):
            # If the move is within the bounds of the board and not a blocked cell, add it to the list of valid moves
            if 0 < r <= len(board) and 0 < c <= len(board[0]) and board[r - 1][c - 1] != '#':
                valid_moves.append((r, c))
    return valid_moves

