
def solve(n, m, island):
    # Initialize the variables
    visited = set()
    queue = [(1, 1)]
    steps = 0

    # Loop through the queue
    while queue:
        # Get the current cell
        curr_row, curr_col = queue.pop(0)

        # Check if the current cell is the treasure cell
        if curr_row == n and curr_col == m:
            return steps

        # Check if the current cell has already been visited
        if (curr_row, curr_col) in visited:
            continue

        # Mark the current cell as visited
        visited.add((curr_row, curr_col))

        # Get the neighbors of the current cell
        neighbors = [(curr_row + 1, curr_col), (curr_row, curr_col + 1)]

        # Filter out the neighbors that are out of bounds or have impassable forests
        neighbors = [neighbor for neighbor in neighbors if 0 <= neighbor[0] <= n and 0 <= neighbor[1] <= m and island[neighbor[0] - 1][neighbor[1] - 1] != "#"]

        # Add the neighbors to the queue
        queue.extend(neighbors)

        # Increment the step count
        steps += 1

    # If the queue is empty, return -1
    return -1

