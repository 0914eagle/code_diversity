
def is_grid_symmetric(grid):
    # Check if the grid is symmetric by checking if the letters in the top half of the grid are the same as the letters in the bottom half of the grid
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j] != grid[len(grid) - i - 1][len(grid[0]) - j - 1]:
                return False
    return True

def solve():
    H, W = map(int, input().split())
    grid = [input() for _ in range(H)]
    if is_grid_symmetric(grid):
        print("YES")
    else:
        print("NO")

if __name__ == '__main__':
    solve()

