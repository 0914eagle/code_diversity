
def solve(board):
    # Initialize the minimum number of steps to reach (1, 1) as -1
    min_steps = -1
    # Initialize the current position of the knight as the position of 'K'
    curr_pos = [i for i, char in enumerate(board[0]) if char == 'K'][0], 0
    # Initialize a set to store the positions that have been visited
    visited = set()
    # Initialize a queue to store the positions to be visited
    queue = [(curr_pos[0], curr_pos[1])]
    # Loop until the queue is empty
    while queue:
        # Get the current position from the queue
        curr_pos = queue.pop(0)
        # If the current position is (1, 1), break the loop
        if curr_pos == (1, 1):
            break
        # Add the current position to the set of visited positions
        visited.add(curr_pos)
        # Get the valid moves for the current position
        valid_moves = get_valid_moves(board, curr_pos)
        # Loop through the valid moves
        for move in valid_moves:
            # If the move is not in the set of visited positions, add it to the queue
            if move not in visited:
                queue.append(move)
                # Update the minimum number of steps if the move is closer to (1, 1)
                if min_steps == -1 or abs(move[0] - 1) + abs(move[1] - 1) < min_steps:
                    min_steps = abs(move[0] - 1) + abs(move[1] - 1)
    # Return the minimum number of steps
    return min_steps

# Function to get the valid moves for a given position
def get_valid_moves(board, pos):
    # Get the row and column of the position
    row, col = pos
    # Get the length of the board
    n = len(board)
    # Initialize a list to store the valid moves
    valid_moves = []
    # Loop through the eight possible moves
    for i in range(8):
        # Get the row and column of the move
        move_row, move_col = row + (i // 2 - 1), col + (i % 2 - 1)
        # If the move is within the bounds of the board and not a blocked cell, add it to the list of valid moves
        if 0 <= move_row < n and 0 <= move_col < n and board[move_row][move_col] != '#':
            valid_moves.append((move_row, move_col))
    # Return the list of valid moves
    return valid_moves

if __name__ == '__main__':
    board = [
        list("...."),
        list("...."),
        list("...."),
        list("...K")
    ]
    print(solve(board))

