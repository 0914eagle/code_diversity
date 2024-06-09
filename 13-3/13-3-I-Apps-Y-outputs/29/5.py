
import sys

def get_black_squares(grid):
    black_squares = 0
    for row in grid:
        for square in row:
            if square == '#':
                black_squares += 1
    return black_squares

def get_choices(grid, k):
    rows = len(grid)
    cols = len(grid[0])
    choices = 0
    for i in range(rows):
        for j in range(cols):
            if grid[i][j] == '#':
                continue
            grid[i][j] = 'R'
            if get_black_squares(grid) == k:
                choices += 1
            grid[i][j] = '.'
    return choices

def main():
    h, w, k = map(int, input().split())
    grid = []
    for _ in range(h):
        grid.append(list(input()))
    print(get_choices(grid, k))

if __name__ == '__main__':
    main()

