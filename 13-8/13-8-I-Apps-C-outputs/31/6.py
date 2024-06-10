
def is_symmetric(grid):
    # Check if the grid is symmetric by comparing the top half of the grid with the bottom half
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j] != grid[len(grid) - i - 1][len(grid[0]) - j - 1]:
                return False
    return True

def solve(grid):
    # Check if the grid is already symmetric
    if is_symmetric(grid):
        return "YES"
    
    # Check if the grid can be made symmetric by swapping two rows or two columns
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            # Swap two rows
            if i != len(grid) - i - 1:
                grid[i], grid[len(grid) - i - 1] = grid[len(grid) - i - 1], grid[i]
                if is_symmetric(grid):
                    return "YES"
                grid[i], grid[len(grid) - i - 1] = grid[len(grid) - i - 1], grid[i]
            # Swap two columns
            if j != len(grid[0]) - j - 1:
                for k in range(len(grid)):
                    grid[k][j], grid[k][len(grid[0]) - j - 1] = grid[k][len(grid[0]) - j - 1], grid[k][j]
                if is_symmetric(grid):
                    return "YES"
                for k in range(len(grid)):
                    grid[k][j], grid[k][len(grid[0]) - j - 1] = grid[k][len(grid[0]) - j - 1], grid[k][j]
    
    # If the grid cannot be made symmetric, return "NO"
    return "NO"

if __name__ == '__main__':
    H, W = map(int, input().split())
    grid = []
    for i in range(H):
        grid.append(input())
    print(solve(grid))

