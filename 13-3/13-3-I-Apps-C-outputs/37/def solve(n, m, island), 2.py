
def solve(n, m, island):
    # Initialize variables
    visited = set()
    queue = [(1, 1)]
    steps = 0

    # Loop through the queue
    while queue:
        # Get the current cell
        row, col = queue.pop(0)

        # Check if the current cell is the treasure cell
        if row == n and col == m:
            return steps

        # Check if the current cell has already been visited
        if (row, col) in visited:
            continue

        # Mark the current cell as visited
        visited.add((row, col))

        # Add the neighboring cells to the queue
        if row + 1 <= n and island[row + 1][col] != "#":
            queue.append((row + 1, col))
        if col + 1 <= m and island[row][col + 1] != "#":
            queue.append((row, col + 1))

        # Increment the step count
        steps += 1

    # If the queue is empty, it means that Vasya cannot reach the treasure
    return -1

