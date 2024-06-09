
def battleship(n, k, grid, ships):
    # Initialize a dictionary to store the number of ways each ship can be placed
    ship_placements = {ship: 0 for ship in ships}
    
    # Iterate over each row of the grid
    for i in range(n):
        # Iterate over each column of the grid
        for j in range(n):
            # If the current square is not occupied by a ship
            if grid[i][j] == ".":
                # Iterate over each ship size
                for ship in ships:
                    # If the current square is not the start of a ship of the current size
                    if j + ship - 1 >= n or grid[i][j + ship - 1] != "X":
                        continue
                    
                    # If the current square is the start of a ship of the current size
                    # and the ship has not been placed yet
                    if ship_placements[ship] == 0:
                        # Increment the number of ways the ship can be placed
                        ship_placements[ship] += 1
                    
                    # If the current square is the start of a ship of the current size
                    # and the ship has already been placed
                    else:
                        # Decrement the number of ways the ship can be placed
                        ship_placements[ship] -= 1
    
    # Initialize a variable to store the total number of ways the ships can be placed
    total_placements = 1
    
    # Iterate over each ship size
    for ship in ships:
        # Multiply the total number of ways the ships can be placed by the number of ways the current ship can be placed
        total_placements *= ship_placements[ship]
    
    # Return the total number of ways the ships can be placed
    return total_placements

