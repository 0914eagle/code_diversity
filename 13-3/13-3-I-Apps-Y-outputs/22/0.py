
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
        for k in range(i-1, i+2):
            for l in range(j-1, j+2):
                if 0 <= k < n and 0 <= l < m and grid[k][l] == '*' and (k, l) != star:
                    return -1
    return stars

