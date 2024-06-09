
def count_valid_colorings(n, grid):
    # Initialize a dictionary to store the number of valid colorings for each hexagon
    valid_colorings = {}

    # Loop through each hexagon in the grid
    for i in range(1, n + 1):
        for j in range(1, n + 1):
            # Get the current hexagon's value
            value = grid[i - 1][j - 1]

            # If the hexagon's value is -1, it can be colored with any value
            if value == -1:
                valid_colorings[(i, j)] = 6
            # If the hexagon's value is not -1, it can only be colored with that value
            else:
                valid_colorings[(i, j)] = 1

    # Loop through each hexagon in the grid again
    for i in range(1, n + 1):
        for j in range(1, n + 1):
            # Get the current hexagon's value and the number of valid colorings for it
            value = grid[i - 1][j - 1]
            num_valid_colorings = valid_colorings[(i, j)]

            # If the hexagon's value is not -1, we need to update the number of valid colorings for its neighbors
            if value != -1:
                # Loop through the hexagon's neighbors
                for neighbor in get_neighbors(i, j, n):
                    # Get the neighbor's value and the number of valid colorings for it
                    neighbor_value = grid[neighbor[0] - 1][neighbor[1] - 1]
                    neighbor_num_valid_colorings = valid_colorings[neighbor]

                    # If the neighbor's value is -1, it can be colored with any value
                    if neighbor_value == -1:
                        neighbor_num_valid_colorings = 6
                    # If the neighbor's value is not -1, it can only be colored with that value
                    else:
                        neighbor_num_valid_colorings = 1

                    # Update the number of valid colorings for the neighbor
                    valid_colorings[neighbor] = min(neighbor_num_valid_colorings, num_valid_colorings)

    # Return the total number of valid colorings
    return sum(valid_colorings.values())

# Function to get the neighbors of a hexagon
def get_neighbors(i, j, n):
    neighbors = []

    # Add the neighboring hexagons to the list of neighbors
    if i % 2 == 1:
        if j > 1:
            neighbors.append((i, j - 1))
        if j < n:
            neighbors.append((i, j + 1))
    else:
        if j > 1:
            neighbors.append((i, j - 1))
        if j < n - 1:
            neighbors.append((i, j + 1))
        if i < n:
            neighbors.append((i + 1, j))

    return neighbors

