
def is_solvable(grid):
    n = len(grid)
    for i in range(n):
        for j in range(n):
            if grid[i][j] == 0:
                return True
    return False

def solve(grid):
    n = len(grid)
    for i in range(n):
        for j in range(n):
            if grid[i][j] == 0:
                for num in range(1, n+1):
                    if is_safe(grid, i, j, num):
                        grid[i][j] = num
                        if solve(grid):
                            return True
                        grid[i][j] = 0
                return False
    return True

def is_safe(grid, row, col, num):
    n = len(grid)
    for i in range(n):
        if grid[row][i] == num or grid[i][col] == num:
            return False
    for i in range(row//3*3, row//3*3+3):
        for j in range(col//3*3, col//3*3+3):
            if grid[i][j] == num:
                return False
    return True

if __name__ == '__main__':
    n, k = map(int, input().split())
    grid = [[0] * n for _ in range(n)]
    for i in range(k):
        grid[i] = list(map(int, input().split()))
    if is_solvable(grid):
        solve(grid)
        for row in grid:
            print(*row)
    else:
        print("No solution exists")

