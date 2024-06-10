
def input_grid():
    grid = []
    for i in range(4):
        grid.append(list(map(int, input().split())))
    return grid

def move(grid, direction):
    if direction == 0:  # left
        for i in range(4):
            grid[i].reverse()
        grid = merge(grid)
        for i in range(4):
            grid[i].reverse()
    elif direction == 1:  # up
        grid = transpose(grid)
        grid = move(grid, 0)
        grid = transpose(grid)
    elif direction == 2:  # right
        grid = move(grid, 0)
        grid = transpose(grid)
        grid = move(grid, 0)
        grid = transpose(grid)
    elif direction == 3:  # down
        grid = move(grid, 1)
        grid = transpose(grid)
        grid = move(grid, 1)
        grid = transpose(grid)
    return grid

def merge(grid):
    for i in range(4):
        for j in range(3):
            if grid[i][j] == grid[i][j+1] and grid[i][j] != 0:
                grid[i][j] *= 2
                grid[i][j+1] = 0
    return grid

def transpose(grid):
    return list(map(list, zip(*grid)))

def print_grid(grid):
    for i in range(4):
        print(*grid[i])

def main():
    grid = input_grid()
    direction = int(input())
    grid = move(grid, direction)
    print_grid(grid)

if __name__ == '__main__':
    main()

