
import sys

def get_black_squares(grid):
    black_squares = 0
    for row in grid:
        for square in row:
            if square == '#':
                black_squares += 1
    return black_squares

def get_possible_choices(grid, k):
    possible_choices = 0
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j] == '#':
                continue
            grid[i][j] = 'R'
            if get_black_squares(grid) == k:
                possible_choices += 1
            grid[i][j] = '.'
    return possible_choices

def main():
    h, w, k = map(int, input().split())
    grid = []
    for i in range(h):
        grid.append(list(input()))
    print(get_possible_choices(grid, k))

if __name__ == "__main__":
    main()

