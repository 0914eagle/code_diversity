
def f1(grid, move):
    # Convert the grid to a list of lists
    grid = [list(map(int, row)) for row in grid.split()]
    # Get the number of rows and columns
    n = len(grid)
    # Define the directions
    directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    # Define the move function
    def move_tile(i, j, di, dj):
        # Get the current tile
        tile = grid[i][j]
        # If the tile is not zero, move it in the given direction
        if tile != 0:
            # Get the new position
            new_i = i + di
            new_j = j + dj
            # If the new position is valid, move the tile and merge if necessary
            if 0 <= new_i < n and 0 <= new_j < n:
                if grid[new_i][new_j] == 0:
                    grid[new_i][new_j] = tile
                    grid[i][j] = 0
                elif grid[new_i][new_j] == tile:
                    grid[new_i][new_j] *= 2
                    grid[i][j] = 0
        return grid
    # Make the move
    for di, dj in directions[move]:
        grid = move_tile(n//2, n//2, di, dj)
    # Return the new grid
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

