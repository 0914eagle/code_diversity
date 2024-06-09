
import sys

def get_number_of_black_squares(grid):
    number_of_black_squares = 0
    for row in grid:
        for square in row:
            if square == '#':
                number_of_black_squares += 1
    return number_of_black_squares

def get_choices(grid, k):
    number_of_rows = len(grid)
    number_of_columns = len(grid[0])
    choices = 0
    for row in range(number_of_rows):
        for column in range(number_of_columns):
            current_number_of_black_squares = get_number_of_black_squares(grid)
            if current_number_of_black_squares == k:
                choices += 1
            grid[row][column] = 'R'
            current_number_of_black_squares = get_number_of_black_squares(grid)
            if current_number_of_black_squares == k:
                choices += 1
            grid[row][column] = '.'
    return choices

def main():
    h, w, k = map(int, input().split())
    grid = []
    for _ in range(h):
        grid.append(list(input()))
    print(get_choices(grid, k))

if __name__ == '__main__':
    main()

