
def get_max_points(grid_size, energy, start_x, start_y, cans):
    # Initialize a grid to keep track of the cans and their timestamps
    grid = [[0] * grid_size for _ in range(grid_size)]
    for can in cans:
        grid[can[0]][can[1]] = can[2]

    # Initialize the maximum points to be 0
    max_points = 0

    # Loop through each second of the game
    for second in range(1, max(grid[0]) + 1):
        # Loop through each cell in the grid
        for i in range(grid_size):
            for j in range(grid_size):
                # If the cell has a can in it and it's the current second, collect the can and update the grid
                if grid[i][j] == second:
                    grid[i][j] = 0
                    max_points += 1

        # If the robot has energy, move it to the cell with the highest timestamp
        if energy > 0:
            max_timestamp = max(max(row) for row in grid)
            if max_timestamp > 0:
                energy -= 1
                grid[start_x][start_y] = max_timestamp
                start_x, start_y = get_next_cell(grid, start_x, start_y)

    return max_points

def get_next_cell(grid, x, y):
    # Get the indices of the adjacent cells
    adjacents = [(x-1, y), (x+1, y), (x, y-1), (x, y+1)]

    # Find the first adjacent cell with the highest timestamp
    for adjacent in adjacents:
        if 0 <= adjacent[0] < len(grid) and 0 <= adjacent[1] < len(grid[0]) and grid[adjacent[0]][adjacent[1]] > 0:
            return adjacent

    # If no adjacent cell has a can, return the current cell
    return x, y

# Test the function with the sample inputs
grid_size = 3
energy = 1
start_x = 1
start_y = 1
cans = [(1, 2, 2), (1, 1, 1), (2, 1, 1), (1, 2, 1), (1, 2, 2), (2, 2, 3), (0, 2, 5), (1, 2, 6)]
print(get_max_points(grid_size, energy, start_x, start_y, cans)) # Output: 4

grid_size = 3
energy = 1
start_x = 0
start_y = 0
cans = [(1, 2, 2), (1, 1, 1), (2, 1, 1), (1, 2, 1), (1, 2, 2), (2, 2, 3), (0, 2, 5), (1, 2, 6)]
print(get_max_points(grid_size, energy, start_x, start_y, cans)) # Output: 0

