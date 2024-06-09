
def count_black_squares(grid):
    # Initialize a counter for the number of black squares
    black_squares = 0

    # Loop through the grid and count the number of black squares
    for row in grid:
        for square in row:
            if square == '#':
                black_squares += 1

    # Return the number of black squares
    return black_squares

def count_choices(grid, k):
    # Initialize a counter for the number of choices
    choices = 0

    # Loop through the grid and count the number of choices that result in k black squares
    for row in grid:
        for square in row:
            if square == '#':
                choices += 1

    # Return the number of choices
    return choices

if __name__ == '__main__':
    # Read the input grid from stdin
    h, w, k = map(int, input().split())
    grid = []
    for _ in range(h):
        grid.append(list(input()))

    # Count the number of black squares in the grid
    black_squares = count_black_squares(grid)

    # Count the number of choices that result in k black squares
    choices = count_choices(grid, k)

    # Print the number of choices
    print(choices)

