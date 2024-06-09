
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

        # Add the current cell to the visited cells set
        visited_cells.add(current_cell)

        # Get the neighbors of the current cell
        neighbors = get_neighbors(current_cell, island)

        # Loop through the neighbors
        for neighbor in neighbors:
            # If the neighbor is not visited and is not a witch cell, add it to the queue
            if neighbor not in visited_cells and neighbor not in witch_cells:
                queue.append(neighbor)

    # If the queue is empty and the treasure cell has not been reached, return -1
    return -1

# Function to get the neighbors of a cell
def get_neighbors(cell, island):
    # Get the row and column of the cell
    row, col = cell

    # Initialize the neighbors list
    neighbors = []

    # Check if the cell has a neighbor in the next row
    if row + 1 <= len(island):
        neighbors.append((row + 1, col))

    # Check if the cell has a neighbor in the previous row
    if row - 1 >= 0:
        neighbors.append((row - 1, col))

    # Check if the cell has a neighbor in the next column
    if col + 1 <= len(island[0]):
        neighbors.append((row, col + 1))

    # Check if the cell has a neighbor in the previous column
    if col - 1 >= 0:
        neighbors.append((row, col - 1))

    # Return the neighbors list
    return neighbors

