
def solve(n, m, island):
    # Initialize variables
    witch_cells = set()
    treasure_cell = (n, m)
    visited_cells = set()
    queue = [(1, 1)]

    # Loop through the queue
    while queue:
        # Get the current cell
        current_cell = queue.pop(0)

        # If the current cell is the treasure cell, return the number of witch cells
        if current_cell == treasure_cell:
            return len(witch_cells)

        # If the current cell has already been visited, skip it
        if current_cell in visited_cells:
            continue

        # Mark the current cell as visited
        visited_cells.add(current_cell)

        # Get the neighbors of the current cell
        neighbors = get_neighbors(current_cell, n, m, island)

        # Add the neighbors to the queue
        queue += neighbors

        # If the current cell is a witch cell, add it to the set of witch cells
        if island[current_cell[0] - 1][current_cell[1] - 1] == "#":
            witch_cells.add(current_cell)

    # If the queue is empty and the treasure cell has not been reached, return -1
    return -1

# Function to get the neighbors of a cell
def get_neighbors(cell, n, m, island):
    # Initialize the neighbors list
    neighbors = []

    # Get the row and column of the cell
    row, col = cell

    # If the cell is not on the border of the island, add the neighboring cells to the list
    if row > 1:
        neighbors.append((row - 1, col))
    if col > 1:
        neighbors.append((row, col - 1))
    if row < n:
        neighbors.append((row + 1, col))
    if col < m:
        neighbors.append((row, col + 1))

    # Return the list of neighbors
    return neighbors

