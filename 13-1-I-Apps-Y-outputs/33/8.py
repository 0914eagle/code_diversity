
def solve(board):
    # Initialize the minimum number of steps to reach (1, 1) as -1
    min_steps = -1
    # Initialize the current position of the knight as the position of 'K'
    current_position = []
    # Loop through each row of the board
    for i in range(len(board)):
        # Loop through each column of the board
        for j in range(len(board[i])):
            # If the current cell is 'K', set the current position to (i, j)
            if board[i][j] == 'K':
                current_position = [i, j]
    # If the current position is not (1, 1), continue searching
    if current_position != [1, 1]:
        # Initialize a queue to store the positions to be visited
        queue = [[current_position[0], current_position[1]]]
        # Initialize a set to store the visited positions
        visited = set()
        # Loop until the queue is empty
        while queue:
            # Get the current position from the queue
            current_position = queue.pop(0)
            # If the current position is (1, 1), set the minimum number of steps to the current step count and break
            if current_position == [1, 1]:
                min_steps = len(queue)
                break
            # Loop through the valid moves of the knight
            for move in [(2, 1), (2, -1), (1, 2), (1, -2), (-1, 2), (-1, -2), (-2, 1), (-2, -1)]:
                # Get the new position by adding the current position and the move
                new_position = [current_position[0] + move[0], current_position[1] + move[1]]
                # If the new position is within the bounds of the board and has not been visited, add it to the queue and mark it as visited
                if 0 < new_position[0] <= len(board) and 0 < new_position[1] <= len(board[0]) and new_position not in visited and board[new_position[0] - 1][new_position[1] - 1] != '#':
                    queue.append(new_position)
                    visited.add(new_position)
    # Return the minimum number of steps
    return min_steps

