
def battleship(n, k, grid, ships):
    # Initialize a dictionary to store the number of ways to place each ship
    ship_placements = {}
    
    # Iterate over each ship size
    for ship in ships:
        # Initialize a variable to store the number of ways to place the current ship
        num_placements = 0
        
        # Iterate over each row in the grid
        for i in range(n):
            # Iterate over each column in the grid
            for j in range(n):
                # Check if the current square is empty
                if grid[i][j] == '.':
                    # Check if the current ship fits in the grid
                    if j + ship - 1 < n:
                        # Check if the current ship fits in the row
                        if i + ship - 1 < n:
                            # Increment the number of ways to place the current ship
                            num_placements += 1
        
        # Add the number of ways to place the current ship to the dictionary
        ship_placements[ship] = num_placements
    
    # Initialize a variable to store the total number of ways to place all ships
    total_placements = 1
    
    # Iterate over each ship size
    for ship in ships:
        # Multiply the total number of ways to place all ships by the number of ways to place the current ship
        total_placements *= ship_placements[ship]
    
    # Return the total number of ways to place all ships
    return total_placements

