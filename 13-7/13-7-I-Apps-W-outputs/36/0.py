
def battleship(n, k, grid, ships):
    # Initialize a dictionary to store the number of ways to place each ship
    ship_placements = {ship: 0 for ship in ships}
    
    # Iterate over each row of the grid
    for i in range(n):
        # Iterate over each column of the grid
        for j in range(n):
            # If the current square is marked as a hit (O)
            if grid[i][j] == "O":
                # Get the size of the ship that was hit
                ship = ships[i]
                # Increment the number of ways to place the ship
                ship_placements[ship] += 1
    
    # Return the product of the number of ways to place each ship
    return math.prod(ship_placements.values())

