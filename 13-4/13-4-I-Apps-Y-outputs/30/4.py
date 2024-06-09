
def solve_2048(grid, move):
    # Convert the grid to a list of lists
    grid = [list(map(int, row)) for row in grid.split()]
    # Get the number of rows and columns
    n = len(grid)
    # Define the directions
    directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    # Define the move functions
    move_functions = {0: move_left, 1: move_up, 2: move_right, 3: move_down}
    # Make the move
    move_functions[move](grid)
    # Return the new grid
    return "\n".join(" ".join(map(str, row)) for row in grid)

def move_left(grid):
    # Loop through the rows
    for i in range(len(grid)):
        # Loop through the columns
        for j in range(len(grid[0])):
            # Check if the current cell is not empty
            if grid[i][j] != 0:
                # Loop through the previous cells
                for k in range(j):
                    # Check if the previous cell is empty
                    if grid[i][k] == 0:
                        # Move the current cell to the previous cell
                        grid[i][k] = grid[i][j]
                        grid[i][j] = 0
                        break
                # Loop through the next cells
                for k in range(j+1, len(grid[0])):
                    # Check if the next cell is empty
                    if grid[i][k] == 0:
                        # Move the current cell to the next cell
                        grid[i][k] = grid[i][j]
                        grid[i][j] = 0
                        break

def move_up(grid):
    # Transpose the grid
    grid = list(map(list, zip(*grid)))
    # Move left
    move_left(grid)
    # Transpose the grid back
    grid = list(map(list, zip(*grid)))

def move_right(grid):
    # Reverse the grid
    grid = [row[::-1] for row in grid]
    # Move left
    move_left(grid)
    # Reverse the grid back
    grid = [row[::-1] for row in grid]

def move_down(grid):
    # Transpose the grid
    grid = list(map(list, zip(*grid)))
    # Move up
    move_up(grid)
    # Transpose the grid back
    grid = list(map(list, zip(*grid)))

def main():
    grid = "2 0 0 2\n4 16 8 2\n2 64 32 4\n1024 1024 64 0"
    move = 0
    print(solve_2048(grid, move))

if __name__ == "__main__":
    main()

