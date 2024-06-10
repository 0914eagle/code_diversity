
def is_valid(grid, row, col, num):
    # Check if the number can be placed in the given row and column
    for i in range(len(grid)):
        if grid[row][i] == num or grid[i][col] == num:
            return False
    return True

def solve_superdoku(grid, row, col, n):
    if row == n:
        return True

    next_row = row + 1 if col == n - 1 else row
    next_col = 0 if col == n - 1 else col + 1

    if grid[row][col] != 0:
        return solve_superdoku(grid, next_row, next_col, n)

    for num in range(1, n + 1):
        if is_valid(grid, row, col, num):
            grid[row][col] = num
            if solve_superdoku(grid, next_row, next_col, n):
                return True
            grid[row][col] = 0

    return False

def superdoku_solver(n, k, filled_rows):
    grid = [[0 for _ in range(n)] for _ in range(n)]

    for i in range(k):
        for j in range(n):
            grid[i][j] = filled_rows[i][j]

    if solve_superdoku(grid, 0, 0, n):
        print("yes")
        for row in grid:
            print(" ".join(map(str, row)))
    else:
        print("no")

if __name__ == "__main__":
    n, k = map(int, input().split())
    filled_rows = [list(map(int, input().split())) for _ in range(k)]
    superdoku_solver(n, k, filled_rows)
