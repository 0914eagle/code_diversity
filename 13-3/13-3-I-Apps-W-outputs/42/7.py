
def is_signature_forgable(grid):
    n, m = len(grid), len(grid[0])
    for i in range(n):
        for j in range(m):
            if grid[i][j] == '#':
                for k in range(i, min(n, i + 3)):
                    for l in range(j, min(m, j + 3)):
                        if grid[k][l] == '#' and (k, l) != (i + 1, j + 1):
                            return "YES"
    return "NO"

