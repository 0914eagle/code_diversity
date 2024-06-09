
def is_signature_forgable(grid):
    n, m = len(grid), len(grid[0])
    for i in range(n):
        for j in range(m):
            if grid[i][j] == '#':
                for k in range(i, min(i+3, n)):
                    for l in range(j, min(j+3, m)):
                        if grid[k][l] == '#':
                            return "YES"
    return "NO"

