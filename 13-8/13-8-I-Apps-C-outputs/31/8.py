
def is_symmetric(grid):
    # Check if the grid is symmetric by comparing the letters in each row with the letters in the mirrored row
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            if grid[i][j] != grid[len(grid) - i - 1][len(grid[i]) - j - 1]:
                return False
    return True

def solve(grid):
    # Check if the grid is already symmetric
    if is_symmetric(grid):
        return "YES"
    
    # Check if the grid can be made symmetric by swapping two rows or two columns
    for i in range(len(grid)):
        for j in range(i + 1, len(grid)):
            if is_symmetric(swap_rows(grid, i, j)) or is_symmetric(swap_columns(grid, i, j)):
                return "YES"
    
    # If the grid cannot be made symmetric, return "NO"
    return "NO"

def swap_rows(grid, i, j):
    # Swap the ith and jth rows of the grid
    grid[i], grid[j] = grid[j], grid[i]
    return grid

def swap_columns(grid, i, j):
    # Swap the ith and jth columns of the grid
    for row in grid:
        row[i], row[j] = row[j], row[i]
    return grid

if __name__ == '__main__':
    H, W = map(int, input().split())
    grid = [input() for _ in range(H)]
    print(solve(grid))

