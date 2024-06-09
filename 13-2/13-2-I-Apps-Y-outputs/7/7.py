
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

def choose_rows_and_columns(grid, k):
    # Initialize a list to store the choices of rows and columns
    choices = []

    # Iterate over the grid
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            # If the current square is black, add the current row and column to the choices
            if grid[i][j] == '#':
                choices.append((i, j))

    # Return the number of choices that result in exactly k black squares
    return len([choice for choice in choices if count_black_squares(grid) == k])

if __name__ == '__main__':
    # Read the input grid and the number of black squares
    h, w, k = map(int, input().split())
    grid = [input() for _ in range(h)]

    # Call the choose_rows_and_columns function and print the result
    print(choose_rows_and_columns(grid, k))

