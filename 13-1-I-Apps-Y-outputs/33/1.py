
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
            # Add the current position to the visited set
            visited.add(str(current_position[0]) + "," + str(current_position[1]))
            # Get the valid positions for the knight to move to from the current position
            valid_positions = get_valid_positions(current_position[0], current_position[1])
            # Loop through each valid position
            for position in valid_positions:
                # If the valid position is not in the visited set and is not a blocked cell, add it to the queue
                if str(position[0]) + "," + str(position[1]) not in visited and board[position[0]][position[1]] != '#':
                    queue.append(position)
    # Return the minimum number of steps
    return min_steps

# Function to get the valid positions for the knight to move to from a given position
def get_valid_positions(row, col):
    valid_positions = []
    for i in range(row - 2, row + 3):
        for j in range(col - 2, col + 3):
            if i >= 1 and i <= len(board) and j >= 1 and j <= len(board[0]) and (i != row or j != col):
                valid_positions.append([i, j])
    return valid_positions

# Test the solve function with a sample board
board = [
    ['.', '.', '.', '.', '.'],
    ['.', '.', '.', '.', '.'],
    ['.', '.', '.', '.', '.'],
    ['.', '.', '.', '.', 'K'],
    ['.', '.', '.', '.', '.']
]
print(solve(board))

