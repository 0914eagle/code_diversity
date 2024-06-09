
def solve(n, m, island):
    # Initialize the variables
    visited = set()
    queue = [(1, 1)]
    steps = 0

    # Loop through the queue
    while queue:
        # Get the current cell
        current_row, current_col = queue.pop(0)

        # Check if the current cell is the treasure cell
        if current_row == n and current_col == m:
            return steps

        # Check if the current cell has already been visited
        if (current_row, current_col) in visited:
            continue

        # Mark the current cell as visited
        visited.add((current_row, current_col))

        # Get the neighbors of the current cell
        neighbors = get_neighbors(current_row, current_col, n, m, island)

        # Add the neighbors to the queue
        queue.extend(neighbors)

        # Increment the step count
        steps += 1

    # If the queue is empty, return -1
    return -1

def get_neighbors(current_row, current_col, n, m, island):
    # Initialize the neighbors list
    neighbors = []

    # Check if the current cell has a neighbor in the next row
    if current_row + 1 <= n:
        neighbors.append((current_row + 1, current_col))

    # Check if the current cell has a neighbor in the next column
    if current_col + 1 <= m:
        neighbors.append((current_row, current_col + 1))

    # Return the neighbors list
    return neighbors

