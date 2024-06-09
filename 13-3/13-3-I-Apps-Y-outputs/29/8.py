
import sys

def get_number_of_black_squares(grid):
    num_black_squares = 0
    for row in grid:
        for square in row:
            if square == '#':
                num_black_squares += 1
    return num_black_squares

def get_choices(grid, num_black_squares):
    choices = []
    for row in range(len(grid)):
        for col in range(len(grid[0])):
            if grid[row][col] == '#':
                choices.append((row, col))
    return choices

def count_valid_choices(grid, num_black_squares, choices):
    valid_choices = 0
    for choice in choices:
        row, col = choice
        if get_number_of_black_squares(grid) - num_black_squares == num_black_squares:
            valid_choices += 1
    return valid_choices

def main():
    h, w, k = map(int, input().split())
    grid = []
    for _ in range(h):
        grid.append(list(input()))
    num_black_squares = get_number_of_black_squares(grid)
    choices = get_choices(grid, num_black_squares)
    valid_choices = count_valid_choices(grid, num_black_squares, choices)
    print(valid_choices)

if __name__ == '__main__':
    main()

