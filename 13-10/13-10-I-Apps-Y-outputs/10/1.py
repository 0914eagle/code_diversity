
def get_grid_size(line):
    return [int(x) for x in line.split()]

def get_grid(size, lines):
    grid = []
    for line in lines:
        grid.append(list(line.strip()))
    return grid

def get_adjacent_bombs(grid, row, col):
    num_bombs = 0
    for i in range(row-1, row+2):
        for j in range(col-1, col+2):
            if 0 <= i < len(grid) and 0 <= j < len(grid[0]) and grid[i][j] == '#':
                num_bombs += 1
    return num_bombs

def update_grid(grid):
    updated_grid = []
    for i, row in enumerate(grid):
        updated_row = []
        for j, col in enumerate(row):
            if col == '.':
                updated_row.append(str(get_adjacent_bombs(grid, i, j)))
            else:
                updated_row.append(col)
        updated_grid.append("".join(updated_row))
    return updated_grid

def main():
    size = get_grid_size(input())
    grid = get_grid(size, iter(input, ''))
    updated_grid = update_grid(grid)
    for row in updated_grid:
        print(row)

if __name__ == '__main__':
    main()

