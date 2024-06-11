

def max_fill(grid, capacity):
    import math
    

    # Initialize variables
    m, n = len(grid), len(grid[0])
    visited = [[False for _ in range(n)] for _ in range(m)]
    queue = [(0, 0, 0)]
    steps = 0

    # Breadth-first search
    while queue:
        i, j, water = queue.pop(0)
        visited[i][j] = True

        # If we have reached the end, return the number of steps
        if i == m - 1 and j == n - 1:
            return steps

        # Add neighbors to the queue
        for di, dj in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
            ni, nj = i + di, j + dj
            if 0 <= ni < m and 0 <= nj < n and not visited[ni][nj] and grid[ni][nj] == 1:
                queue.append((ni, nj, water + 1))

        # If we have used up the capacity, backtrack
        if water == capacity:
            steps += 1

    # If we have reached the end, return the number of steps
    return steps


