
def solve(n, m, island):
    # Initialize variables
    witch_cells = set()
    treasure_cell = (n, m)
    visited_cells = set()
    queue = [(1, 1)]

    # Loop through the queue
    while queue:
        current_cell = queue.pop(0)
        visited_cells.add(current_cell)

        # If the current cell is the treasure cell, return the number of witch cells
        if current_cell == treasure_cell:
            return len(witch_cells)

        # Get the neighbors of the current cell
        neighbors = get_neighbors(current_cell, island)

        # Add the neighbors to the queue if they are not visited and not witch cells
        for neighbor in neighbors:
            if neighbor not in visited_cells and neighbor not in witch_cells:
                queue.append(neighbor)

    # If the queue is empty, return -1
    return -1

# Get the neighbors of a cell
def get_neighbors(cell, island):
    (row, col) = cell
    neighbors = []

    # Check if the cell has a neighbor in the next row
    if row + 1 <= len(island):
        neighbors.append((row + 1, col))

    # Check if the cell has a neighbor in the next column
    if col + 1 <= len(island[0]):
        neighbors.append((row, col + 1))

    return neighbors

