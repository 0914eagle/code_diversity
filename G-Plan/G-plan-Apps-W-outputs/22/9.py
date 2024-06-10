alid_path(grid, path):
    def is_adjacent(tile1, tile2):
        return abs(grid.index(tile1) - grid.index(tile2)) in [1, 13]

    for i in range(len(path) - 1):
        if not is_adjacent(path[i], path[i + 1]):
            return False
    return True

def generate_grid(path):
    grid = [''] * 26
    grid[0] = path[0]
    for i in range(1, len(path)):
        for j in range(26):
            if grid[j] == '' and is_adjacent(path[i], grid[j - 1]):
                grid[j] = path[i]
                break
    return grid

def find_grid(s):
    for i in range(26):
        grid = generate_grid(s[i:] + s[:i])
        if is_valid_path(grid, s):
            return grid
    return None

def print_grid(grid):
    for i in range(0, 26, 13):
        print(''.join(grid[i:i+13]))

if __name__ == '__main__':
    s = input().strip()
    grid = find_grid(s)
    if grid:
        print_grid(grid)
    else:
        print("Impossible"