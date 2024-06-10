
def is_valid(grid, row, col, num):
    for i in range(len(grid)):
        if grid[row][i] == num or grid[i][col] == num:
            return False
    return True

def solve_superdoku(grid, n, k):
    if k == n:
        return True

    for i in range(n):
        for j in range(n):
            if grid[i][j] == 0:
                for num in range(1, n + 1):
                    if is_valid(grid, i, j, num):
                        grid[i][j] = num
                        if solve_superdoku(grid, n, k):
                            return True
                        grid[i][j] = 0
                return False
    return True

if __name__ == "__main__":
    n, k = map(int, input().split())
    filled_rows = [list(map(int, input().split())) for _ in range(k)]
    grid = [[0 for _ in range(n)] for _ in range(n)]
    
    for i in range(k):
        for j in range(n):
            grid[i][j] = filled_rows[i][j]
    
    if solve_superdoku(grid, n, k):
        print("yes")
        for row in grid:
            print(" ".join(map(str, row)))
    else:
        print("no")
