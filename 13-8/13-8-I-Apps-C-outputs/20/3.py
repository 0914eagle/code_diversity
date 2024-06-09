
def solve(h, w, altitudes, i, j):
    # Initialize the total volume of water drained to 0
    total_volume = 0

    # Loop through each row of the grid
    for row in range(h):
        # Loop through each column of the grid
        for col in range(w):
            # If the current cell is covered by water and is not the cell where the draining device is placed
            if altitudes[row][col] < 0 and not (row == i and col == j):
                # Find the shortest path from the current cell to the cell where the draining device is placed
                path = find_path(altitudes, row, col, i, j)

                # If a path exists
                if path:
                    # Add the volume of water in the current cell to the total volume of water drained
                    total_volume += abs(altitudes[row][col])

                    # Update the altitude of the current cell and the cells in the path to 0
                    for cell in path:
                        altitudes[cell[0]][cell[1]] = 0

    # Return the total volume of water drained
    return total_volume

def find_path(altitudes, start_row, start_col, end_row, end_col):
    # Initialize the queue with the starting cell
    queue = [(start_row, start_col)]

    # Initialize the visited cells to an empty set
    visited = set()

    # Loop until the queue is empty
    while queue:
        # Get the current cell from the queue
        row, col = queue.pop(0)

        # If the current cell is the end cell, return the path
        if row == end_row and col == end_col:
            return True

        # If the current cell has not been visited before
        if (row, col) not in visited:
            # Mark the current cell as visited
            visited.add((row, col))

            # Add the neighbors of the current cell to the queue
            for neighbor in get_neighbors(altitudes, row, col):
                queue.append(neighbor)

    # If no path exists, return False
    return False

def get_neighbors(altitudes, row, col):
    # Get the neighbors of the current cell
    neighbors = [(row-1, col), (row+1, col), (row, col-1), (row, col+1)]

    # Filter out neighbors that are not valid cells or are covered by water
    valid_neighbors = []
    for neighbor in neighbors:
        if 0 <= neighbor[0] < len(altitudes) and 0 <= neighbor[1] < len(altitudes[0]) and altitudes[neighbor[0]][neighbor[1]] < 0:
            valid_neighbors.append(neighbor)

    # Return the valid neighbors
    return valid_neighbors

