
def solve(grid):
    n, m = len(grid), len(grid[0])
    stars = []
    for i in range(n):
        for j in range(m):
            if grid[i][j] == '*':
                stars.append((i, j))
    for star in stars:
        i, j = star
        for k in range(n):
            for l in range(m):
                if grid[k][l] == '*' and (k, l) != star:
                    return -1
        for k in range(4):
            for l in range(1, m):
                if grid[i + k][j + l] == '*':
                    return -1
            for l in range(1, n):
                if grid[i + l][j + k] == '*':
                    return -1
    return stars

