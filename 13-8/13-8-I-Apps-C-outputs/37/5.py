
def get_paths(map):
    # Initialize variables
    paths = 0
    visited = set()
    queue = [(0, 0)]

    # Loop through the queue
    while queue:
        row, col = queue.pop(0)

        # Check if the current position is the destination
        if map[row][col] == "@":
            paths += 1
            continue

        # Check if the current position is already visited
        if (row, col) in visited:
            continue

        # Mark the current position as visited
        visited.add((row, col))

        # Get the neighbors of the current position
        neighbors = get_neighbors(map, row, col)

        # Add the neighbors to the queue
        queue.extend(neighbors)

    # Return the number of paths
    return paths % 1000003

# Get the neighbors of a given position
def get_neighbors(map, row, col):
    neighbors = []

    # Check if the current position is on the right side of the map
    if col < len(map[0]) - 1 and map[row][col + 1] != "#":
        neighbors.append((row, col + 1))

    # Check if the current position is on the left side of the map
    if col > 0 and map[row][col - 1] != "#":
        neighbors.append((row, col - 1))

    # Check if the current position is on the top side of the map
    if row > 0 and map[row - 1][col] != "#":
        neighbors.append((row - 1, col))

    # Check if the current position is on the bottom side of the map
    if row < len(map) - 1 and map[row + 1][col] != "#":
        neighbors.append((row + 1, col))

    return neighbors

