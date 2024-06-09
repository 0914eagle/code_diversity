
def solve(board):
    # Initialize the minimum number of steps to reach (1, 1) as -1
    min_steps = -1
    # Initialize the current position of the knight as the position of 'K'
    curr_pos = [i for i, char in enumerate(board[0]) if char == 'K'][0], 0
    # Initialize a set to store the positions of the blocked cells
    blocked_cells = set()
    # Iterate over the board
    for i, row in enumerate(board):
        for j, char in enumerate(row):
            # If the current character is '#', add the position to the set of blocked cells
            if char == '#':
                blocked_cells.add((i, j))
    # Initialize a queue to store the positions of the cells to be visited
    queue = [(curr_pos[0], curr_pos[1], 0)]
    # Initialize a set to store the positions of the visited cells
    visited = set()
    # Loop until the queue is empty
    while queue:
        # Get the current position from the queue
        curr_pos = queue.pop(0)
        # If the current position is (1, 1), set the minimum number of steps to the current step count and break
        if curr_pos[0] == 1 and curr_pos[1] == 1:
            min_steps = curr_pos[2]
            break
        # If the current position is not in the set of blocked cells and not in the set of visited cells, add it to the queue
        if curr_pos not in blocked_cells and curr_pos not in visited:
            queue.append((curr_pos[0] + 2, curr_pos[1] + 1, curr_pos[2] + 1))
            queue.append((curr_pos[0] + 2, curr_pos[1] - 1, curr_pos[2] + 1))
            queue.append((curr_pos[0] - 2, curr_pos[1] + 1, curr_pos[2] + 1))
            queue.append((curr_pos[0] - 2, curr_pos[1] - 1, curr_pos[2] + 1))
            queue.append((curr_pos[0] + 1, curr_pos[1] + 2, curr_pos[2] + 1))
            queue.append((curr_pos[0] + 1, curr_pos[1] - 2, curr_pos[2] + 1))
            queue.append((curr_pos[0] - 1, curr_pos[1] + 2, curr_pos[2] + 1))
            queue.append((curr_pos[0] - 1, curr_pos[1] - 2, curr_pos[2] + 1))
            visited.add(curr_pos)
    # Return the minimum number of steps
    return min_steps

