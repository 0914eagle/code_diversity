
def is_valid(grid, row, col, num):
    # Check if the number is already present in the row
    if num in grid[row]:
        return False
    
    # Check if the number is already present in the column
    for i in range(len(grid)):
        if grid[i][col] == num:
            return False
    
    return True

def solve_superdoku(grid, row, col):
    if row == len(grid):
        return True
    
    next_row = row + 1 if col == len(grid) - 1 else row
    next_col = 0 if col == len(grid) - 1 else col + 1
    
    if grid[row][col] != 0:
        return solve_superdoku(grid, next_row, next_col)
    
    for num in range(1, len(grid) + 1):
        if is_valid(grid, row, col, num):
            grid[row][col] = num
            if solve_superdoku(grid, next_row, next_col):
                return True
            grid[row][col] = 0
    
    return False

def superdoku_solver(n, k, filled_rows):
    grid = [[0 for _ in range(n)] for _ in range(n)]
    
    for i in range(k):
        grid[i] = filled_rows[i]
    
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
