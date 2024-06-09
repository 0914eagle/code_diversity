
import sys

def get_black_squares(grid):
    black_squares = 0
    for row in grid:
        for square in row:
            if square == '#':
                black_squares += 1
    return black_squares

def get_choices(grid, k):
    num_rows = len(grid)
    num_cols = len(grid[0])
    choices = 0
    for rows in range(num_rows+1):
        for cols in range(num_cols+1):
            black_squares = get_black_squares(grid)
            if black_squares == k:
                choices += 1
    return choices

def main():
    h, w, k = map(int, input().split())
    grid = []
    for _ in range(h):
        grid.append(input())
    print(get_choices(grid, k))

if __name__ == "__main__":
    main()

