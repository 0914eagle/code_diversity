
def get_moves_before_score(state):
    # Initialize variables
    num_rows, num_cols = len(state), len(state[0])
    num_moves = 0
    visited = set()
    queue = [(0, 0)]

    # Loop through the state and find all possible moves
    while queue:
        row, col = queue.pop(0)
        visited.add((row, col))
        num_moves += 1

        # Check if the current position forms a unit square
        if row + 1 < num_rows and col + 1 < num_cols and state[row + 1][col] == '*' and state[row][col + 1] == '*':
            return num_moves

        # Add new positions to the queue
        for new_row, new_col in [(row - 1, col), (row + 1, col), (row, col - 1), (row, col + 1)]:
            if 0 <= new_row < num_rows and 0 <= new_col < num_cols and (new_row, new_col) not in visited and state[new_row][new_col] == '.':
                queue.append((new_row, new_col))

    # If no unit square is formed, return the number of moves
    return num_moves

