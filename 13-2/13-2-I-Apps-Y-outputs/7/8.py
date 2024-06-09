
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

def choose_rows_and_columns(grid, k):
    # Initialize a list to store the choices of rows and columns
    choices = []

    # Loop through the grid and find the k black squares
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j] == '#':
                # Add the current row and column to the choices list
                choices.append((i, j))
                # If we have found k black squares, return the choices list
                if len(choices) == k:
                    return choices

    # If we have not found k black squares, return an empty list
    return []

def main():
    # Read the input from stdin
    h, w, k = map(int, input().split())
    grid = [input() for _ in range(h)]

    # Count the number of black squares in the grid
    black_squares = count_black_squares(grid)

    # Choose the rows and columns with k black squares
    choices = choose_rows_and_columns(grid, k)

    # Print the number of choices
    print(len(choices))

if __name__ == '__main__':
    main()

