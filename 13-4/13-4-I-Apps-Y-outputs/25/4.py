
def solve(grid):
    n, m = len(grid), len(grid[0])
    stars = []
    for i in range(n):
        for j in range(m):
            if grid[i][j] == '*':
                stars.append((i, j))
    for i in range(len(stars)):
        for j in range(i+1, len(stars)):
            x1, y1 = stars[i]
            x2, y2 = stars[j]
            if x1 == x2 and y1 == y2:
                return -1
            if x1 == x2 or y1 == y2:
                continue
            if abs(x1-x2) == abs(y1-y2):
                return -1
    return stars

