
def solve(N, data):
    # Initialize a list to store the number of surviving islands
    surviving_islands = []

    # Loop through each island
    for i in range(N):
        # Get the threshold and the number of incoming goods for the current island
        threshold, incoming_goods = data[i]

        # Check if the current island has already collapsed
        if threshold == 0:
            continue

        # Check if the current island has enough incoming goods to survive
        if incoming_goods >= threshold:
            # Add the current island to the list of surviving islands
            surviving_islands.append(i)

    # Return the number of surviving islands
    return len(surviving_islands)

