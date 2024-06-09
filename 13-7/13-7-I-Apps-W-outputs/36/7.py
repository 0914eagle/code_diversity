
def battleship(grid, ships):
    # Initialize a dictionary to store the number of ships for each size
    ship_counts = {size: 0 for size in ships}

    # Iterate over the grid and count the number of ships for each size
    for row in grid:
        for col in row:
            if col in ships:
                ship_counts[col] += 1

    # Calculate the total number of ships
    total_ships = sum(ship_counts.values())

    # Calculate the number of possible ship placements
    num_placements = 1
    for size in ship_counts:
        num_placements *= ship_counts[size] + 1

    # Return the number of possible ship placements
    return num_placements - total_ships

