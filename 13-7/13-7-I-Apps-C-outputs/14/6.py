
def get_worst_case_moves(state):
    # Initialize variables
    num_rows, num_cols = len(state), len(state[0])
    num_moves = 0
    visited = set()
    queue = [(0, 0)]

    # Breadth-first search to find the shortest path to a point
    while queue:
        row, col = queue.pop(0)
        visited.add((row, col))
        num_moves += 1

        # Check if the current position is a point
        if state[row][col] == '*':
            return num_moves

        # Add neighbors to the queue
        for r, c in [(row-1, col), (row+1, col), (row, col-1), (row, col+1)]:
            if 0 <= r < num_rows and 0 <= c < num_cols and (r, c) not in visited and state[r][c] != '*':
                queue.append((r, c))

    # If no point is found, return the number of moves made
    return num_moves

