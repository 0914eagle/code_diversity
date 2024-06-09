
def get_surviving_islands(islands):
    # Initialize a list to keep track of the surviving islands
    surviving_islands = []

    # Iterate through the list of islands
    for island in islands:
        # Check if the island has enough goods to survive
        if island[0] <= sum(island[2:]):
            # Add the island to the list of surviving islands
            surviving_islands.append(island)

    # Return the number of surviving islands
    return len(surviving_islands)

