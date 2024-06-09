
def get_worst_case_moves(state):
    # Initialize variables
    num_rows, num_cols = len(state), len(state[0])
    num_moves = 0
    visited = set()
    queue = [(0, 0)]

    # Breadth-first search to find the worst-case number of moves
    while queue:
        row, col = queue.pop(0)
        visited.add((row, col))
        num_moves += 1

        # Check if the current cell is a dot
        if state[row][col] == "*":
            # Check if the current cell is connected to the edge of the grid
            if row == 0 or row == num_rows - 1 or col == 0 or col == num_cols - 1:
                return num_moves

            # Add adjacent cells to the queue
            for r, c in [(row-1, col), (row+1, col), (row, col-1), (row, col+1)]:
                if 0 <= r < num_rows and 0 <= c < num_cols and (r, c) not in visited:
                    queue.append((r, c))

    return num_moves

