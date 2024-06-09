
def count_paths(map):
    # Initialize the number of paths to 0
    paths = 0

    # Loop through each row of the map
    for row in map:
        # Loop through each column of the row
        for col in row:
            # If the current cell is the castle, increment the number of paths
            if col == "@":
                paths += 1

    # Return the number of paths modulo 1000003
    return paths % 1000003

