
def count_black_squares(grid):
    # Initialize a counter for the number of black squares
    black_squares = 0

    # Iterate through the grid and count the number of black squares
    for row in grid:
        for square in row:
            if square == "#":
                black_squares += 1

    return black_squares

def count_choices(grid, k):
    # Initialize a counter for the number of choices
    choices = 0

    # Iterate through the grid and count the number of choices that result in k black squares
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if count_black_squares(grid) == k:
                choices += 1

    return choices

if __name__ == '__main__':
    h, w, k = map(int, input().split())
    grid = []
    for _ in range(h):
        grid.append(list(input()))
    print(count_choices(grid, k))

