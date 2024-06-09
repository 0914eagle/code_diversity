
import sys

def get_black_squares(grid):
    black_squares = 0
    for row in grid:
        for square in row:
            if square == '#':
                black_squares += 1
    return black_squares

def count_choices(grid, k):
    h, w = len(grid), len(grid[0])
    count = 0
    for rows in range(h+1):
        for cols in range(w+1):
            if get_black_squares(grid) - rows - cols == k:
                count += 1
    return count

h, w, k = map(int, input().split())
grid = [input() for _ in range(h)]
print(count_choices(grid, k))

