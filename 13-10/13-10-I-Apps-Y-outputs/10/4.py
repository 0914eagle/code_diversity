
def get_adjacent_bombs(grid, row, col):
    # Initialize a dictionary to count the number of bombs adjacent to each empty square
    adjacent_bombs = {}

    # Loop through the rows and columns of the grid
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            # If the current square is empty, check if it has any bombs adjacent to it
            if grid[i][j] == ".":
                # Initialize a count variable to keep track of the number of bombs adjacent to the current empty square
                count = 0

                # Check if there are any bombs in the row above the current square
                if i > 0 and grid[i - 1][j] == "#":
                    count += 1

                # Check if there are any bombs in the row below the current square
                if i < len(grid) - 1 and grid[i + 1][j] == "#":
                    count += 1

                # Check if there are any bombs in the column to the left of the current square
                if j > 0 and grid[i][j - 1] == "#":
                    count += 1

                # Check if there are any bombs in the column to the right of the current square
                if j < len(grid[0]) - 1 and grid[i][j + 1] == "#":
                    count += 1

                # Check if there are any bombs in the top-left diagonal of the current square
                if i > 0 and j > 0 and grid[i - 1][j - 1] == "#":
                    count += 1

                # Check if there are any bombs in the top-right diagonal of the current square
                if i > 0 and j < len(grid[0]) - 1 and grid[i - 1][j + 1] == "#":
                    count += 1

                # Check if there are any bombs in the bottom-left diagonal of the current square
                if i < len(grid) - 1 and j > 0 and grid[i + 1][j - 1] == "#":
                    count += 1

                # Check if there are any bombs in the bottom-right diagonal of the current square
                if i < len(grid) - 1 and j < len(grid[0]) - 1 and grid[i + 1][j + 1] == "#":
                    count += 1

                # Add the number of bombs adjacent to the current empty square to the dictionary
                adjacent_bombs[(i, j)] = count

    return adjacent_bombs

def solve(grid):
    # Initialize a list to store the solved grid
    solved_grid = []

    # Loop through the rows of the grid
    for i in range(len(grid)):
        # Initialize a string to store the solved row
        solved_row = ""

        # Loop through the columns of the grid
        for j in range(len(grid[0])):
            # If the current square is a bomb, add a # to the solved row
            if grid[i][j] == "#":
                solved_row += "#"
            # If the current square is empty, add the number of bombs adjacent to it to the solved row
            else:
                solved_row += str(get_adjacent_bombs(grid, i, j)[(i, j)])

        # Add the solved row to the list of solved rows
        solved_grid.append(solved_row)

    # Return the solved grid
    return solved_grid

def main():
    # Read the dimensions of the grid from the input
    H, W = map(int, input().split())

    # Read the grid from the input
    grid = [input() for _ in range(H)]

    # Solve the grid
    solved_grid = solve(grid)

    # Print the solved grid
    for row in solved_grid:
        print(row)

if __name__ == '__main__':
    main()

