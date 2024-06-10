
def is_valid(grid, row, col, num):
    # Check if the current number placement is valid in the row and column
    for i in range(len(grid)):
        if grid[row][i] == num or grid[i][col] == num:
            return False
    return True

def solve_superdoku(grid, n, k):
    # Recursive backtracking function to solve the Superdoku problem
    def backtrack(row, col):
        if row == n:
            return True

        next_row = row + 1 if col == n - 1 else row
        next_col = 0 if col == n - 1 else col + 1

        if grid[row][col] != 0:
            return backtrack(next_row, next_col)

        for num in range(1, n + 1):
            if is_valid(grid, row, col, num):
                grid[row][col] = num
                if backtrack(next_row, next_col):
                    return True
                grid[row][col] = 0

        return False

    if backtrack(0, 0):
        return grid
    return None

if __name__ == "__main__":
    n, k = map(int, input().split())
    grid = [[0 for _ in range(n)] for _ in range(n)]

    for i in range(k):
        row_values = list(map(int, input().split()))
        for j in range(n):
            grid[i][j] = row_values[j]

    solution = solve_superdoku(grid, n, k)
    if solution:
        print("yes")
        for row in solution:
            print(" ".join(map(str, row)))
    else:
        print("no")
