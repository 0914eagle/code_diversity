
def is_valid_grid(grid):
    H, W = len(grid), len(grid[0])
    for i in range(H):
        for j in range(W):
            if grid[i][j] == '#':
                if i > 0 and grid[i-1][j] == '#':
                    return False
                if j > 0 and grid[i][j-1] == '#':
                    return False
    return True

def paint_grid(grid):
    H, W = len(grid), len(grid[0])
    for i in range(H):
        for j in range(W):
            if grid[i][j] == '#':
                if i > 0:
                    grid[i-1][j] = '#'
                if j > 0:
                    grid[i][j-1] = '#'
    return grid

def main():
    H, W = map(int, input().split())
    grid = [input() for _ in range(H)]
    if is_valid_grid(grid):
        print("Yes")
    else:
        print("No")

if __name__ == '__main__':
    main()

