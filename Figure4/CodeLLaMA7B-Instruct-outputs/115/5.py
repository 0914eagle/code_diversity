

def max_fill(grid, capacity):
    import math
    

    # Initialize variables
    rows, cols = len(grid), len(grid[0])
    visited = [[False for _ in range(cols)] for _ in range(rows)]
    bucket_count = 0
    total_water = 0
    max_water = 0

    # BFS to find the maximum water that can be extracted
    queue = []
    for i in range(rows):
        for j in range(cols):
            if grid[i][j] == 1:
                queue.append((i, j))
                visited[i][j] = True
                bucket_count += 1
                total_water += 1

    while queue:
        size = len(queue)
        for _ in range(size):
            i, j = queue.pop(0)
            for di, dj in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                ni, nj = i + di, j + dj
                if 0 <= ni < rows and 0 <= nj < cols and grid[ni][nj] == 1 and not visited[ni][nj]:
                    queue.append((ni, nj))
                    visited[ni][nj] = True
                    total_water += 1

    # Calculate the maximum number of times the buckets need to be lowered
    max_water = total_water
    for i in range(rows):
        for j in range(cols):
            if grid[i][j] == 1 and not visited[i][j]:
                queue = [(i, j)]
                visited[i][j] = True
                total_water = 1
                while queue:
                    size = len(queue)
                    for _ in range(size):
                        i, j = queue.pop(0)
                        for di, dj in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                            ni, nj = i + di, j + dj
                            if 0 <= ni < rows and 0 <= nj < cols and grid[ni][nj] == 1 and not visited
