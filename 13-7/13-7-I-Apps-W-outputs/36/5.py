
def battleship(grid, ships):
    # Initialize a dictionary to store the number of ways to place each ship
    ship_placements = {ship: 0 for ship in ships}
    
    # Iterate over each row of the grid
    for i in range(len(grid)):
        # Iterate over each column of the grid
        for j in range(len(grid[0])):
            # Check if the current square is occupied by a ship
            if grid[i][j] == 'X':
                # Find the size of the ship by looking at the number of adjacent occupied squares
                ship_size = 1
                for di in range(-1, 2):
                    for dj in range(-1, 2):
                        if 0 <= i+di < len(grid) and 0 <= j+dj < len(grid[0]) and grid[i+di][j+dj] == 'X':
                            ship_size += 1
                # Update the number of ways to place the ship
                ship_placements[ship_size] += 1
    
    # Return the product of the number of ways to place each ship
    return math.prod(ship_placements.values())

