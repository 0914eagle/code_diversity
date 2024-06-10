djacent(tile1, tile2):
    return abs(ord(tile1[0]) - ord(tile2[0])) <= 1 and abs(ord(tile1[1]) - ord(tile2[1])) <= 1

def find_path(grid, s, row, col, index):
    if index == len(s):
        return True
    if row < 0 or row >= 2 or col < 0 or col >= 13 or grid[row][col] != s[index]:
        return False
    temp = grid[row][col]
    grid[row][col] = ' '
    if (col < 12 and is_adjacent(temp, grid[row][col + 1]) and find_path(grid, s, row, col + 1, index + 1)) or \
       (col > 0 and is_adjacent(temp, grid[row][col - 1]) and find_path(grid, s, row, col - 1, index + 1)) or \
       (row < 1 and is_adjacent(temp, grid[row + 1][col]) and find_path(grid, s, row + 1, col, index + 1)) or \
       (row > 0 and is_adjacent(temp, grid[row - 1][col]) and find_path(grid, s, row - 1, col, index + 1)):
        return True
    grid[row][col] = temp
    return False

def construct_grid(s):
    grid = [[' ' for _ in range(13)] for _ in range(2)]
    if find_path(grid, s, 0, 0, 0):
        return grid
    return None

def print_grid(grid):
    if grid is None:
        print("Impossible")
    else:
        for row in grid:
            print(''.join(row))

if __name__ == "__main__":
    s = input().strip()
    grid = construct_grid(s)
    print_grid(grid