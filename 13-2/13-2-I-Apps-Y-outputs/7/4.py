
def count_black_squares(grid):
    # Initialize a counter for the number of black squares
    black_squares = 0

    # Iterate through the grid and count the number of black squares
    for row in grid:
        for square in row:
            if square == '#':
                black_squares += 1

    return black_squares

def count_choices(grid, k):
    # Initialize a counter for the number of choices
    choices = 0

    # Iterate through the grid and count the number of choices that result in k black squares
    for row in grid:
        for col in range(len(row)):
            # Count the number of black squares in the current row and column
            black_squares = 0
            for i in range(len(grid)):
                if grid[i][col] == '#':
                    black_squares += 1
            for j in range(len(grid[0])):
                if grid[row][j] == '#':
                    black_squares += 1

            # If the number of black squares is equal to k, increment the counter
            if black_squares == k:
                choices += 1

    return choices

def main():
    # Read the input grid and the number of black squares
    h, w, k = map(int, input().split())
    grid = []
    for _ in range(h):
        grid.append(list(input()))

    # Count the number of black squares and the number of choices
    black_squares = count_black_squares(grid)
    choices = count_choices(grid, k)

    # Print the number of choices
    print(choices)

if __name__ == '__main__':
    main()

