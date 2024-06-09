
def cake_eater(grid):
    rows, cols = len(grid), len(grid[0])
    visited = [[False for _ in range(cols)] for _ in range(rows)]
    count = 0

    for i in range(rows):
        for j in range(cols):
            if grid[i][j] == "." and not visited[i][j]:
                count += 1
                dfs(grid, visited, i, j)

    return count

def dfs(grid, visited, i, j):
    rows, cols = len(grid), len(grid[0])
    if i < 0 or i >= rows or j < 0 or j >= cols or grid[i][j] == "S" or visited[i][j]:
        return

    visited[i][j] = True
    dfs(grid, visited, i+1, j)
    dfs(grid, visited, i-1, j)
    dfs(grid, visited, i, j+1)
    dfs(grid, visited, i, j-1)

