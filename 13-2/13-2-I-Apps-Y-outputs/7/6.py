
def count_black_squares(grid):
    # Initialize a counter for the number of black squares
    black_squares = 0

    # Iterate over the grid
    for row in grid:
        for square in row:
            # If the current square is black, increment the counter
            if square == '#':
                black_squares += 1

    # Return the number of black squares
    return black_squares

def count_choices(grid, k):
    # Initialize a counter for the number of choices
    choices = 0

    # Iterate over the grid
    for row in grid:
        for square in row:
            # If the current square is black, increment the counter
            if square == '#':
                choices += 1

    # Return the number of choices
    return choices

def main():
    # Read the input grid
    h, w, k = map(int, input().split())
    grid = []
    for _ in range(h):
        grid.append(list(input()))

    # Count the number of black squares
    black_squares = count_black_squares(grid)

    # Count the number of choices
    choices = count_choices(grid, k)

    # Print the number of choices
    print(choices)

if __name__ == '__main__':
    main()

