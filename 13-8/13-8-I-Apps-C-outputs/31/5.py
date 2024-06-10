
def get_grid(H, W):
    grid = []
    for i in range(H):
        grid.append(input())
    return grid

def swap_rows(grid, i, j):
    temp = grid[i]
    grid[i] = grid[j]
    grid[j] = temp
    return grid

def swap_columns(grid, i, j):
    for row in grid:
        temp = row[i]
        row[i] = row[j]
        row[j] = temp
    return grid

def is_symmetric(grid):
    H, W = len(grid), len(grid[0])
    for i in range(H):
        for j in range(W):
            if grid[i][j] != grid[H-i-1][W-j-1]:
                return False
    return True

def solve(grid):
    H, W = len(grid), len(grid[0])
    for i in range(H):
        for j in range(W):
            if grid[i][j] != grid[H-i-1][W-j-1]:
                return "YES"
    return "NO"

if __name__ == '__main__':
    H, W = map(int, input().split())
    grid = get_grid(H, W)
    print(solve(grid))

