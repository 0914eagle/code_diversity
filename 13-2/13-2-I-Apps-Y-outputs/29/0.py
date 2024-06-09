
def move_left(grid):
    # Move tiles to the left
    for i in range(4):
        for j in range(3, -1, -1):
            if grid[i][j] != 0:
                for k in range(j, -1, -1):
                    if grid[i][k] == 0:
                        grid[i][k] = grid[i][j]
                        grid[i][j] = 0
                        break
                    elif grid[i][k] == grid[i][j]:
                        grid[i][k] *= 2
                        grid[i][j] = 0
                        break
    return grid

def move_up(grid):
    # Move tiles up
    for j in range(4):
        for i in range(3, -1, -1):
            if grid[i][j] != 0:
                for k in range(i, -1, -1):
                    if grid[k][j] == 0:
                        grid[k][j] = grid[i][j]
                        grid[i][j] = 0
                        break
                    elif grid[k][j] == grid[i][j]:
                        grid[k][j] *= 2
                        grid[i][j] = 0
                        break
    return grid

def move_right(grid):
    # Move tiles to the right
    for i in range(4):
        for j in range(3, -1, -1):
            if grid[i][j] != 0:
                for k in range(j, -1, -1):
                    if grid[i][k] == 0:
                        grid[i][k] = grid[i][j]
                        grid[i][j] = 0
                        break
                    elif grid[i][k] == grid[i][j]:
                        grid[i][k] *= 2
                        grid[i][j] = 0
                        break
    return grid

def move_down(grid):
    # Move tiles down
    for j in range(4):
        for i in range(3, -1, -1):
            if grid[i][j] != 0:
                for k in range(i, -1, -1):
                    if grid[k][j] == 0:
                        grid[k][j] = grid[i][j]
                        grid[i][j] = 0
                        break
                    elif grid[k][j] == grid[i][j]:
                        grid[k][j] *= 2
                        grid[i][j] = 0
                        break
    return grid

def get_new_grid(grid, direction):
    # Get the new grid based on the direction
    if direction == 0:
        return move_left(grid)
    elif direction == 1:
        return move_up(grid)
    elif direction == 2:
        return move_right(grid)
    else:
        return move_down(grid)

def solve(grid, direction):
    # Get the new grid based on the direction
    new_grid = get_new_grid(grid, direction)
    
    # Check if the new grid is the same as the original grid
    if new_grid == grid:
        return grid
    
    # Recursively call the solve function with the new grid
    return solve(new_grid, direction)

if __name__ == '__main__':
    grid = [[2, 0, 0, 2], [4, 16, 8, 2], [2, 64, 32, 4], [1024, 1024, 64, 0]]
    direction = 0
    new_grid = solve(grid, direction)
    print(new_grid)

