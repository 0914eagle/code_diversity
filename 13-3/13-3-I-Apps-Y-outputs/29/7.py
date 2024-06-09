
import sys

def get_black_squares(grid):
    black_squares = 0
    for row in grid:
        for square in row:
            if square == '#':
                black_squares += 1
    return black_squares

def count_choices(grid, k):
    rows, cols = len(grid), len(grid[0])
    count = 0
    for i in range(rows):
        for j in range(cols):
            grid[i][j] = 'R'
            if get_black_squares(grid) == k:
                count += 1
            grid[i][j] = '.'
    return count

def main():
    h, w, k = map(int, input().split())
    grid = [input() for _ in range(h)]
    print(count_choices(grid, k))

if __name__ == '__main__':
    main()

