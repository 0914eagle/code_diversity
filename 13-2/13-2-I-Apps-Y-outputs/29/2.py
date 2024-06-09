
def f1(grid, move):
    # Convert the grid to a list of lists
    grid = [list(map(int, row)) for row in grid.split()]
    # Get the number of rows and columns
    n = len(grid)
    # Define the directions
    directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    # Define the move function
    def move_tiles(i, j, di, dj):
        # Move the tiles in the current direction
        while 0 <= i + di < n and 0 <= j + dj < n and grid[i + di][j + dj] != 0:
            if grid[i][j] == grid[i + di][j + dj] and grid[i][j] != 0:
                grid[i][j] *= 2
                grid[i + di][j + dj] = 0
            else:
                grid[i][j], grid[i + di][j + dj] = grid[i + di][j + dj], grid[i][j]
            i += di
            j += dj
        return i, j
    # Make the move
    i, j = move_tiles(move // 2, move % 2, directions[move][0], directions[move][1])
    # Return the new grid
    return "\n".join(" ".join(map(str, row)) for row in grid)

def f2(grid, move):
    # Convert the grid to a list of lists
    grid = [list(map(int, row)) for row in grid.split()]
    # Get the number of rows and columns
    n = len(grid)
    # Define the directions
    directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    # Define the move function
    def move_tiles(i, j, di, dj):
        # Move the tiles in the current direction
        while 0 <= i + di < n and 0 <= j + dj < n and grid[i + di][j + dj] != 0:
            if grid[i][j] == grid[i + di][j + dj] and grid[i][j] != 0:
                grid[i][j] *= 2
                grid[i + di][j + dj] = 0
            else:
                grid[i][j], grid[i + di][j + dj] = grid[i + di][j + dj], grid[i][j]
            i += di
            j += dj
        return i, j
    # Make the move
    i, j = move_tiles(move // 2, move % 2, directions[move][0], directions[move][1])
    # Return the new grid
    return "\n".join(" ".join(map(str, row)) for row in grid)

if __name__ == '__main__':
    grid = "2 0 0 2\n4 16 8 2\n2 64 32 4\n1024 1024 64 0"
    move = 0
    print(f1(grid, move))
    print(f2(grid, move))

