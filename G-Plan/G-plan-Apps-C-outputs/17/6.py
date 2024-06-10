
def is_valid(grid, row, col, num):
    for i in range(len(grid)):
        if grid[row][i] == num or grid[i][col] == num:
            return False
    return True

def solve_superdoku(grid, row, col):
    if row == len(grid):
        return True
    
    if col == len(grid):
        return solve_superdoku(grid, row + 1, 0)
    
    if grid[row][col] != 0:
        return solve_superdoku(grid, row, col + 1)
    
    for num in range(1, len(grid) + 1):
        if is_valid(grid, row, col, num):
            grid[row][col] = num
            if solve_superdoku(grid, row, col + 1):
                return True
            grid[row][col] = 0
    
    return False

def superdoku_solver(n, k, filled_rows):
    grid = [[0 for _ in range(n)] for _ in range(n)]
    
    for i in range(k):
        for j in range(n):
            grid[i][j] = filled_rows[i][j]
    
    if solve_superdoku(grid, k, 0):
        print("yes")
        for row in grid:
            print(" ".join(map(str, row)))
    else:
        print("no")

if __name__ == "__main__":
    n, k = map(int, input().split())
    filled_rows = [list(map(int, input().split())) for _ in range(k)]
    superdoku_solver(n, k, filled_rows)
