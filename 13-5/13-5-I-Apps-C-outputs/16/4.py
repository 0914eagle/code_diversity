
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
                for k in range(1, n+1):
                    if is_safe(grid, i, j, k):
                        grid[i][j] = k
                        if solve(grid):
                            return True
                        grid[i][j] = 0
                return False
    return True

def is_safe(grid, row, col, num):
    for i in range(len(grid)):
        if grid[row][i] == num or grid[i][col] == num:
            return False
    for i in range(row//3*3, row//3*3+3):
        for j in range(col//3*3, col//3*3+3):
            if grid[i][j] == num:
                return False
    return True

def main():
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

if __name__ == '__main__':
    main()

