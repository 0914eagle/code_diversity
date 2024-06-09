
def get_surviving_islands(islands):
    # Initialize a list to keep track of the surviving islands
    surviving_islands = []

    # Loop through each island
    for i, island in enumerate(islands):
        # Check if the island has enough goods to survive
        if island[0] <= island[1]:
            # Add the island to the list of surviving islands
            surviving_islands.append(i)

    # Return the number of surviving islands
    return len(surviving_islands)

