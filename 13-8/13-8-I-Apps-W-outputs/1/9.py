
def check_lair(grid):
    N = len(grid)
    for i in range(N):
        for j in range(N):
            if grid[i][j] != 0:
                break
        else:
            return "No"
    for i in range(N):
        for j in range(N):
            if grid[i][j] != 0:
                break
        else:
            return "No"
    for i in range(N):
        for j in range(N):
            if grid[i][j] != 0:
                break
        else:
            return "No"
    for i in range(N):
        for j in range(N):
            if grid[i][j] != 0:
                break
        else:
            return "No"
    return "Yes"

