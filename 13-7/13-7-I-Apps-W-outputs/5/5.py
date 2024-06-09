
def surviving_islands(num_islands, island_data):
    # Initialize a list to keep track of the number of surviving islands
    surviving_islands = [1]

    # Loop through each island after the first one
    for i in range(1, num_islands):
        # Check if the island has enough goods to survive
        if island_data[i][0] <= sum(island_data[i][1:]):
            # Add the island to the list of surviving islands
            surviving_islands.append(i + 1)

    # Return the number of surviving islands
    return len(surviving_islands)

