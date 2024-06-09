
def solve(grid):
    n, m = len(grid), len(grid[0])
    stars = []
    for i in range(n):
        for j in range(m):
            if grid[i][j] == '*':
                stars.append((i, j))
    for star in stars:
        i, j = star
        size = 1
        while valid_star(stars, i, j, size):
            size += 1
        if size > n * m:
            return -1
        stars.append((i, j, size))
    return stars

def valid_star(stars, i, j, size):
    for star in stars:
        x, y, s = star
        if x == i and y == j and s == size:
            return False
    for x in range(i - size + 1, i + size):
        for y in range(j - size + 1, j + size):
            if not (0 <= x < len(grid) and 0 <= y < len(grid[0]) and grid[x][y] == '*'):
                return False
    return True

grid = [
    list("....*..."),
    list("...**..."),
    list("..*****."),
    list("...**..."),
    list("....*..."),
    list("........"),
]
result = solve(grid)
print(result)

