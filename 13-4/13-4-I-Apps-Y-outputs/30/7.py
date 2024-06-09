
def solve_2048(grid, move):
    # Convert the grid to a 2D list for easier manipulation
    grid = [[int(x) for x in grid[i * 4:(i + 1) * 4]] for i in range(4)]
    
    # Define the possible moves and their corresponding directions
    moves = {0: "left", 1: "up", 2: "right", 3: "down"}
    directions = {
        "left": (0, 1),
        "up": (1, 0),
        "right": (0, -1),
        "down": (-1, 0)
    }
    
    # Get the current move direction
    direction = directions[moves[move]]
    
    # Initialize the new grid with the same values as the original grid
    new_grid = [[x for x in row] for row in grid]
    
    # Iterate through the grid and move the tiles
    for i in range(4):
        for j in range(4):
            # Get the current tile and its position
            tile = grid[i][j]
            pos = (i, j)
            
            # If the tile is not zero, move it in the current direction
            if tile != 0:
                # Get the new position of the tile
                new_pos = (pos[0] + direction[0], pos[1] + direction[1])
                
                # If the new position is valid, move the tile to that position
                if 0 <= new_pos[0] < 4 and 0 <= new_pos[1] < 4:
                    new_grid[new_pos[0]][new_pos[1]] = tile
                    new_grid[pos[0]][pos[1]] = 0
    
    # Merge the tiles that have collided
    for i in range(4):
        for j in range(3):
            if new_grid[i][j] != 0 and new_grid[i][j + 1] != 0 and new_grid[i][j] == new_grid[i][j + 1]:
                new_grid[i][j] *= 2
                new_grid[i][j + 1] = 0
    
    # Return the new grid as a string
    return "\n".join([" ".join(map(str, row)) for row in new_grid])

