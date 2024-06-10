
def is_symmetric(grid):
    # Check if the grid is symmetric
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j] != grid[len(grid) - i - 1][len(grid[0]) - j - 1]:
                return False
    return True

def solve(grid):
    # Check if the grid is already symmetric
    if is_symmetric(grid):
        return "YES"
    
    # Check if the grid can be made symmetric by swapping rows or columns
    for i in range(len(grid)):
        for j in range(i + 1, len(grid)):
            if grid[i] != grid[j]:
                grid[i], grid[j] = grid[j], grid[i]
                if is_symmetric(grid):
                    return "YES"
                grid[i], grid[j] = grid[j], grid[i]
    
    return "NO"

if __name__ == '__main__':
    H, W = map(int, input().split())
    grid = [input() for _ in range(H)]
    print(solve(grid))

