
def is_valid(grid, row, col, num):
    for i in range(len(grid)):
        if grid[row][i] == num or grid[i][col] == num:
            return False
    return True

def solve_superdoku(grid, n, k):
    def solve(row, col):
        if row == n:
            return True
        if col == n:
            return solve(row + 1, 0)
        if grid[row][col] != 0:
            return solve(row, col + 1)
        
        for num in range(1, n + 1):
            if is_valid(grid, row, col, num):
                grid[row][col] = num
                if solve(row, col + 1):
                    return True
                grid[row][col] = 0
        
        return False

    if solve(0, 0):
        return grid
    return None

if __name__ == "__main__":
    n, k = map(int, input().split())
    grid = [[0 for _ in range(n)] for _ in range(n)]
    for i in range(k):
        row = list(map(int, input().split()))
        for j in range(n):
            grid[i][j] = row[j]
    
    solution = solve_superdoku(grid, n, k)
    if solution:
        print("yes")
        for row in solution:
            print(" ".join(map(str, row)))
    else:
        print("no")
