
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

        # Check if the current cell is the treasure cell
        if current_cell == treasure_cell:
            break

        # Get the neighbors of the current cell
        neighbors = get_neighbors(current_cell, island)

        # Add the neighbors to the queue that have not been visited yet
        for neighbor in neighbors:
            if neighbor not in visited_cells and neighbor not in witch_cells:
                queue.append(neighbor)

    # Return the number of cells the witch needs to turn into impassable forests
    return len(witch_cells)

# Function to get the neighbors of a cell
def get_neighbors(cell, island):
    (row, col) = cell
    neighbors = []

    # Check if the cell is not on the border of the island
    if row > 1 and col > 1:
        neighbors.append((row-1, col-1))
    if row > 1:
        neighbors.append((row-1, col))
    if row > 1 and col < len(island[0]):
        neighbors.append((row-1, col+1))
    if col > 1:
        neighbors.append((row, col-1))
    if col < len(island[0]):
        neighbors.append((row, col+1))

    return neighbors

