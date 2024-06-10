
def is_valid(grid, row, col, num):
    # Check if the number is already in the row
    if num in grid[row]:
        return False
    
    # Check if the number is already in the column
    if num in [grid[i][col] for i in range(len(grid))]:
        return False
    
    return True

def solve_superdoku(grid, n, k, row=0, col=0):
    if row == n:
        return True
    
    next_row = row if col == n - 1 else row + 1
    next_col = 0 if col == n - 1 else col + 1
    
    if row < k:
        if solve_superdoku(grid, n, k, next_row, next_col):
            return True
    else:
        for num in range(1, n + 1):
            if is_valid(grid, row, col, num):
                grid[row][col] = num
                if solve_superdoku(grid, n, k, next_row, next_col):
                    return True
                grid[row][col] = 0
    
    return False

if __name__ == "__main__":
    n, k = map(int, input().split())
    filled_rows = [list(map(int, input().split())) for _ in range(k)]
    
    grid = [[0 for _ in range(n)] for _ in range(n)]
    for i in range(k):
        grid[i] = filled_rows[i]
    
    if solve_superdoku(grid, n, k):
        print("yes")
        for row in grid:
            print(" ".join(map(str, row)))
    else:
        print("no")
