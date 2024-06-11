

def max_fill(grid, capacity):
    import math
    

    # Initialize variables
    m, n = len(grid), len(grid[0])
    visited = [[False for _ in range(n)] for _ in range(m)]
    queue = []
    result = 0

    # BFS to find the shortest path to fill the grid
    for i in range(m):
        for j in range(n):
            if grid[i][j] == 1 and not visited[i][j]:
                queue.append((i, j))
                visited[i][j] = True
                while queue:
                    i, j = queue.pop(0)
                    for dx, dy in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                        x, y = i + dx, j + dy
                        if 0 <= x < m and 0 <= y < n and grid[x][y] == 1 and not visited[x][y]:
                            queue.append((x, y))
                            visited[x][y] = True

    # Calculate the number of times we need to lower the buckets
    for i in range(m):
        for j in range(n):
            if grid[i][j] == 1:
                result += 1

    return result

