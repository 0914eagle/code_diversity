
def count_valid_colorings(n, grid):
    # Initialize a dictionary to store the number of valid colorings for each hexagon
    valid_colorings = {}

    # Loop through each hexagon in the grid
    for i in range(1, n + 1):
        for j in range(1, n + 1):
            # Get the value of the current hexagon
            value = grid[i - 1][j - 1]

            # If the value is -1, skip this hexagon
            if value == -1:
                continue

            # Get the number of valid colorings for this hexagon
            num_valid_colorings = count_valid_colorings_helper(i, j, value, grid, valid_colorings)

            # Add the number of valid colorings to the total
            valid_colorings[(i, j)] = num_valid_colorings

    # Return the total number of valid colorings
    return sum(valid_colorings.values())

def count_valid_colorings_helper(i, j, value, grid, valid_colorings):
    # If this hexagon has already been counted, return the number of valid colorings
    if (i, j) in valid_colorings:
        return valid_colorings[(i, j)]

    # Initialize the number of valid colorings to 0
    num_valid_colorings = 0

    # Loop through all possible colors for this hexagon
    for color in range(1, 7):
        # If the color is not the same as the value of the hexagon, skip this color
        if color == value:
            continue

        # Get the number of valid colorings for the neighboring hexagons
        num_valid_colorings_neighbors = 0
        for neighbor in get_neighbors(i, j, grid):
            num_valid_colorings_neighbors += count_valid_colorings_helper(neighbor[0], neighbor[1], color, grid, valid_colorings)

        # Add the number of valid colorings for this hexagon and its neighbors to the total
        num_valid_colorings += num_valid_colorings_neighbors

    # Return the number of valid colorings for this hexagon
    return num_valid_colorings

def get_neighbors(i, j, grid):
    # Get the number of rows and columns in the grid
    num_rows = len(grid)
    num_cols = len(grid[0])

    # Initialize a list to store the neighbors
    neighbors = []

    # Loop through all possible neighbors
    for di in range(-1, 2):
        for dj in range(-1, 2):
            # If the neighbor is out of bounds, skip this neighbor
            if i + di < 1 or i + di > num_rows or j + dj < 1 or j + dj > num_cols:
                continue

            # If the neighbor is the same as the current hexagon, skip this neighbor
            if di == 0 and dj == 0:
                continue

            # Add the neighbor to the list of neighbors
            neighbors.append((i + di, j + dj))

    # Return the list of neighbors
    return neighbors

