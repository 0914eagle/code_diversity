
def solve(grid):
    n, m = len(grid), len(grid[0])
    stars = []
    for i in range(n):
        for j in range(m):
            if grid[i][j] == '*':
                stars.append((i, j))
    for star in stars:
        x, y = star
        for i in range(x-1, x+2):
            for j in range(y-1, y+2):
                if 0 <= i < n and 0 <= j < m and (i, j) not in stars:
                    stars.append((i, j))
    return stars

