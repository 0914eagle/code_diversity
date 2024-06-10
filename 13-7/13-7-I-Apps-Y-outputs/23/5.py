
def get_input():
    grid = []
    for i in range(4):
        grid.append(list(map(int, input().split())))
    direction = int(input())
    return grid, direction

def move_tiles(grid, direction):
    if direction == 0: # left
        for i in range(4):
            grid[i] = sorted(grid[i], reverse=True)
    elif direction == 1: # up
        for i in range(4):
            grid[i] = sorted(grid[i], reverse=True)
        grid = list(map(list, zip(*grid)))
        grid.reverse()
    elif direction == 2: # right
        for i in range(4):
            grid[i] = sorted(grid[i])
    elif direction == 3: # down
        for i in range(4):
            grid[i] = sorted(grid[i])
        grid = list(map(list, zip(*grid)))
    return grid

def merge_tiles(grid):
    for i in range(4):
        for j in range(3):
            if grid[i][j] == grid[i][j+1]:
                grid[i][j] *= 2
                grid[i].pop(j+1)
    return grid

def get_output(grid):
    return [' '.join(map(str, row)) for row in grid]

def main():
    grid, direction = get_input()
    grid = move_tiles(grid, direction)
    grid = merge_tiles(grid)
    output = get_output(grid)
    print('\n'.join(output))

if __name__ == '__main__':
    main()

