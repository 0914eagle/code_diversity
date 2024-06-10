djacent(tile1, tile2):
    return abs(ord(tile1[0]) - ord(tile2[0])) <= 1 and abs(ord(tile1[1]) - ord(tile2[1])) <= 1

def find_path(grid, s, row, col, index):
    if index == len(s):
        return True
    for i in range(-1, 2):
        for j in range(-1, 2):
            if i == 0 and j == 0:
                continue
            new_row = row + i
            new_col = col + j
            if 0 <= new_row < 2 and 0 <= new_col < 13 and grid[new_row][new_col] == s[index]:
                if find_path(grid, s, new_row, new_col, index + 1):
                    return True
    return False

def construct_grid(s):
    grid = [['' for _ in range(13)] for _ in range(2)]
    for i in range(13):
        grid[0][i] = s[i]
    for i in range(13, 26):
        grid[1][i - 13] = s[i]
    if find_path(grid, s, 0, 0, 13):
        return grid
    return None

def print_grid(grid):
    for row in grid:
        print(''.join(row))

if __name__ == "__main__":
    s = input().strip()
    grid = construct_grid(s)
    if grid:
        print_grid(grid)
    else:
        print("Impossible"