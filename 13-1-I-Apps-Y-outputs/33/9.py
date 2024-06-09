
def solve(board):
    # Initialize the minimum number of steps to reach (1, 1) as -1
    min_steps = -1
    # Initialize the current position of the knight as the position of 'K'
    curr_pos = [i for i, char in enumerate(board[0]) if char == 'K'][0], 0
    # Initialize a set to store the positions of the knight that have been visited
    visited = set()
    # Initialize a queue to store the positions of the knight that need to be visited
    queue = [(curr_pos[0], curr_pos[1])]
    # Loop until the queue is empty
    while queue:
        # Get the current position of the knight from the queue
        curr_pos = queue.pop(0)
        # If the current position is (1, 1), break the loop
        if curr_pos == (1, 1):
            break
        # Add the current position to the set of visited positions
        visited.add(curr_pos)
        # Get the valid positions that the knight can move to from the current position
        valid_pos = get_valid_positions(board, curr_pos)
        # Loop through the valid positions
        for pos in valid_pos:
            # If the position has not been visited, add it to the queue
            if pos not in visited:
                queue.append(pos)
                # If the position is (1, 1), set the minimum number of steps to the current number of steps
                if pos == (1, 1):
                    min_steps = len(queue)
    # Return the minimum number of steps
    return min_steps

# Function to get the valid positions that the knight can move to from a given position
def get_valid_positions(board, pos):
    # Get the row and column of the position
    row, col = pos
    # Get the size of the board
    size = len(board)
    # Initialize a list to store the valid positions
    valid_pos = []
    # Loop through the eight possible positions that the knight can move to
    for i in range(row - 2, row + 3):
        for j in range(col - 2, col + 3):
            # If the position is within the bounds of the board and not a '#', add it to the list of valid positions
            if 0 < i <= size and 0 < j <= size and board[i - 1][j - 1] != '#':
                valid_pos.append((i, j))
    # Return the list of valid positions
    return valid_pos

