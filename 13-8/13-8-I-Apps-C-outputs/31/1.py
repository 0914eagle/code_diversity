
def is_grid_symmetric(grid):
    # Check if the grid is symmetric by comparing the letters in the top row with the letters in the bottom row, and the letters in the left column with the letters in the right column
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j] != grid[len(grid) - i - 1][len(grid[0]) - j - 1]:
                return False
    return True

def solve():
    # Read the input data from stdin
    H, W = map(int, input().split())
    grid = [input() for _ in range(H)]

    # Check if the grid is symmetric
    if is_grid_symmetric(grid):
        print("YES")
    else:
        print("NO")

if __name__ == '__main__':
    solve()

