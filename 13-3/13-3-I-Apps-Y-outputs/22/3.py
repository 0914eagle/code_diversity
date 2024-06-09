
def solve(grid):
    n, m = len(grid), len(grid[0])
    stars = []
    for i in range(n):
        for j in range(m):
            if grid[i][j] == '*':
                stars.append((i, j))
    for star in stars:
        i, j = star
        for k in range(4):
            x, y = i + (k // 2) - 1, j + (k % 2) - 1
            if 0 <= x < n and 0 <= y < m and grid[x][y] == '*':
                return -1
    return stars

