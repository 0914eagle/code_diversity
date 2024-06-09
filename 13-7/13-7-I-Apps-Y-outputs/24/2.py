
def solve(grid):
    # Initialize variables
    m, n = len(grid), len(grid[0])
    visited = [[False] * n for _ in range(m)]
    queue = [(0, 0, 0)]

    # Loop through the grid
    while queue:
        row, col, ladder_length = queue.pop(0)

        # If we have reached the last row and column, return the ladder length
        if row == m - 1 and col == n - 1:
            return ladder_length

        # Check all possible moves from the current position
        for dr, dc in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
            r, c = row + dr, col + dc

            # If the new position is valid and not visited yet, add it to the queue
            if 0 <= r < m and 0 <= c < n and not visited[r][c]:
                visited[r][c] = True
                queue.append((r, c, max(ladder_length, grid[r][c])))

    # If we reach this point, no path exists
    return -1

