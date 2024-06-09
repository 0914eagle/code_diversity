
def f1(grid, move):
    # Convert the grid to a list of lists
    grid = [list(map(int, row)) for row in grid.split()]
    # Get the number of rows and columns
    n = len(grid)
    # Define the directions
    directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    # Define the move function
    def move_tiles(i, j, di, dj):
        # Get the current tile
        tile = grid[i][j]
        # If the tile is zero, return
        if tile == 0:
            return
        # Get the next tile
        next_tile = grid[i+di][j+dj]
        # If the next tile is zero, move the current tile to the next position
        if next_tile == 0:
            grid[i+di][j+dj] = tile
            grid[i][j] = 0
        # If the next tile is the same as the current tile, merge the tiles and set the current tile to zero
        elif next_tile == tile:
            grid[i+di][j+dj] = tile + next_tile
            grid[i][j] = 0
    # Move the tiles in the selected direction
    move_tiles(move, 0, directions[move][0], directions[move][1])
    # Return the updated grid
    return grid

def f2(grid):
    # Convert the grid to a list of lists
    grid = [list(map(int, row)) for row in grid.split()]
    # Get the number of rows and columns
    n = len(grid)
    # Initialize the score to zero
    score = 0
    # Iterate over the grid
    for i in range(n):
        for j in range(n):
            # If the current tile is not zero, add its value to the score
            if grid[i][j] != 0:
                score += grid[i][j]
    # Return the score
    return score

if __name__ == '__main__':
    grid = "2 0 0 2 4 16 8 2 2 64 32 4 1024 1024 64 0"
    move = 0
    print(f1(grid, move))
    print(f2(grid))

