
def count_adjacent_bombs(grid):
    # Initialize a dictionary to store the number of adjacent bombs for each empty square
    adjacent_bombs = {}

    # Loop through each row in the grid
    for i in range(len(grid)):
        # Loop through each column in the row
        for j in range(len(grid[i])):
            # If the current square is empty, count the number of bombs adjacent to it
            if grid[i][j] == ".":
                # Count the number of bombs above, below, left, and right of the current square
                above = i - 1 >= 0 and grid[i - 1][j] == "#"
                below = i + 1 < len(grid) and grid[i + 1][j] == "#"
                left = j - 1 >= 0 and grid[i][j - 1] == "#"
                right = j + 1 < len(grid[i]) and grid[i][j + 1] == "#"

                # Count the number of adjacent bombs
                num_adjacent_bombs = above + below + left + right

                # Add the number of adjacent bombs to the dictionary
                adjacent_bombs[(i, j)] = num_adjacent_bombs

    return adjacent_bombs

def print_grid(grid, adjacent_bombs):
    # Loop through each row in the grid
    for i in range(len(grid)):
        # Loop through each column in the row
        for j in range(len(grid[i])):
            # If the current square is empty, print the number of adjacent bombs
            if grid[i][j] == ".":
                print(adjacent_bombs[(i, j)], end="")
            # Otherwise, print the current square
            else:
                print(grid[i][j], end="")
        print()

def main():
    # Read the input grid
    grid = []
    for _ in range(int(input())):
        grid.append(input())

    # Count the number of adjacent bombs for each empty square
    adjacent_bombs = count_adjacent_bombs(grid)

    # Print the grid with the number of adjacent bombs for each empty square
    print_grid(grid, adjacent_bombs)

if __name__ == '__main__':
    main()

