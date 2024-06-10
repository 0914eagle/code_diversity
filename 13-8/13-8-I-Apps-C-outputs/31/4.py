
def is_symmetric(grid):
    # Check if the grid is symmetric by checking if the letters in the top half of the grid are the same as the letters in the bottom half of the grid
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j] != grid[len(grid) - i - 1][len(grid[0]) - j - 1]:
                return False
    return True

def make_symmetric(grid):
    # Swap the rows of the grid to make it symmetric
    for i in range(len(grid) // 2):
        grid[i], grid[len(grid) - i - 1] = grid[len(grid) - i - 1], grid[i]
    return grid

def main():
    h, w = map(int, input().split())
    grid = [input() for _ in range(h)]
    if is_symmetric(grid):
        print("YES")
    else:
        print("NO")
        grid = make_symmetric(grid)
        print(*grid, sep='\n')

if __name__ == '__main__':
    main()

