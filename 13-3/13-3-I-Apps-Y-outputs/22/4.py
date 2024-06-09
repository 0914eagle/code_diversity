
def solve(grid):
    n, m = len(grid), len(grid[0])
    stars = []
    for i in range(n):
        for j in range(m):
            if grid[i][j] == "*":
                stars.append((i, j))
    # Check if the grid can be covered with at most n*m stars
    if len(stars) > n*m:
        return -1
    # Check if the stars are valid
    for i, j in stars:
        if i < 0 or i >= n or j < 0 or j >= m:
            return -1
        if grid[i][j] != "*":
            return -1
    # Draw the grid with the given stars
    for i, j in stars:
        grid[i][j] = "*"
    return stars

