
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
                if k == i and l == j:
                    continue
                if grid[k][l] == '*':
                    return "-1"
    return str(len(stars)) + "\n" + "\n".join(str(i+1) + " " + str(j+1) + " " + str(1) for i, j in stars)

