
def battleship(n, k, grid, ship_sizes):
    # Initialize a dictionary to store the number of ways each ship can be placed
    ship_placements = {ship_size: 0 for ship_size in ship_sizes}
    
    # Iterate over each row of the grid
    for row in range(n):
        # Iterate over each column of the grid
        for col in range(n):
            # If the current square is a hit (O)
            if grid[row][col] == "O":
                # Find the size of the ship that was hit
                ship_size = ship_sizes[grid[row][col - 1]]
                # Decrement the number of ways the ship can be placed
                ship_placements[ship_size] -= 1
    
    # Initialize a variable to store the total number of ways the ships can be placed
    total_placements = 1
    
    # Iterate over each ship size
    for ship_size in ship_sizes:
        # Multiply the total number of ways the ships can be placed by the number of ways the current ship can be placed
        total_placements *= ship_placements[ship_size]
    
    # Return the total number of ways the ships can be placed
    return total_placements

