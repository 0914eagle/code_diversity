
import sys

def get_number_of_black_squares(grid):
    num_black_squares = 0
    for row in grid:
        for square in row:
            if square == '#':
                num_black_squares += 1
    return num_black_squares

def get_choices(grid, num_black_squares):
    num_rows = len(grid)
    num_cols = len(grid[0])
    choices = 0
    for row in range(num_rows):
        for col in range(num_cols):
            if grid[row][col] == '#':
                continue
            grid[row][col] = 'R'
            num_black_squares_after_painting = get_number_of_black_squares(grid)
            if num_black_squares_after_painting == num_black_squares:
                choices += 1
            grid[row][col] = '.'
    return choices

def main():
    h, w, k = map(int, input().split())
    grid = []
    for _ in range(h):
        grid.append(list(input()))
    print(get_choices(grid, k))

if __name__ == '__main__':
    main()

