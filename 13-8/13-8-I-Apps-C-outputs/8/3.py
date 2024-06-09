
def solve(street, tiles):
    # Initialize a dictionary to store the number of untileable cells for each length of tile
    untileable_cells = {1: 0, 2: 0, 3: 0, 4: 0, 5: 0}

    # Loop through each tile pattern
    for tile in tiles:
        # Get the length of the tile pattern
        tile_length = len(tile)

        # Loop through each position in the street
        for i in range(len(street) - tile_length + 1):
            # Check if the tile pattern matches the street substring
            if tile == street[i:i+tile_length]:
                # If it matches, increment the number of untileable cells for the length of the tile pattern
                untileable_cells[tile_length] += 1

    # Return the total number of untileable cells
    return sum(untileable_cells.values())

