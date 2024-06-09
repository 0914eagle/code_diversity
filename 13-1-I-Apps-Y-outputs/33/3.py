
def solve(board):
    # Initialize the minimum number of steps to -1
    min_steps = -1
    # Initialize the current position of the knight
    current_position = (len(board), len(board[0]))
    # Initialize a set to store the visited cells
    visited = set()
    # Initialize a queue to store the cells to be visited
    queue = [(current_position, 0)]
    # Loop until the queue is empty
    while queue:
        # Get the current cell and the number of steps
        current_cell, steps = queue.pop(0)
        # If the current cell is (1, 1), return the number of steps
        if current_cell == (1, 1):
            return steps
        # If the current cell is not visited, mark it as visited and add it to the visited set
        if current_cell not in visited:
            visited.add(current_cell)
            # Get the valid moves for the current cell
            valid_moves = get_valid_moves(current_cell, board)
            # Loop through the valid moves
            for move in valid_moves:
                # If the move is not visited, add it to the queue with the number of steps incremented by 1
                if move not in visited:
                    queue.append((move, steps + 1))
    # If the queue is empty and the minimum number of steps is still -1, return -1
    return min_steps

# Function to get the valid moves for a given cell
def get_valid_moves(cell, board):
    # Get the row and column of the cell
    row, col = cell
    # Initialize a list to store the valid moves
    valid_moves = []
    # Loop through the eight possible moves
    for i in range(8):
        # Get the row and column of the move
        move_row = row + (i // 2 - 1)
        move_col = col + (i % 2 - 1)
        # If the move is within the bounds of the board and is not a blocked cell, add it to the list of valid moves
        if 0 < move_row <= len(board) and 0 < move_col <= len(board[0]) and board[move_row - 1][move_col - 1] != '#':
            valid_moves.append((move_row, move_col))
    # Return the list of valid moves
    return valid_moves

