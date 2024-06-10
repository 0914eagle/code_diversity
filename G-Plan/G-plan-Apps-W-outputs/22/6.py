
from itertools import permutations

def is_adjacent(tile1, tile2):
    row1, col1 = divmod(tile1, 13)
    row2, col2 = divmod(tile2, 13)
    return abs(row1 - row2) <= 1 and abs(col1 - col2) <= 1

def construct_grid(path):
    grid = [['' for _ in range(13)] for _ in range(2)]
    for i, tile in enumerate(path):
        row, col = divmod(i, 13)
        grid[row][col] = chr(ord('A') + tile)
    return grid

def find_path(s):
    tiles = list(range(26))
    for perm in permutations(tiles):
        if all(is_adjacent(perm[i], perm[i+1]) for i in range(25)):
            grid = construct_grid(perm)
            return grid
    return "Impossible"

if __name__ == "__main__":
    s = input().strip()
    grid = find_path(s)
    if grid == "Impossible":
        print(grid)
    else:
        for row in grid:
            print(''.join(row))
