
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
        neighbors = get_neighbors(current_cell, n, m, island)

        # Add the neighbors to the queue if they are not visited before
        for neighbor in neighbors:
            if neighbor not in visited_cells and neighbor not in witch_cells:
                queue.append(neighbor)

    # Return the number of witch cells needed to block Vasya's path
    return len(witch_cells)

# Function to get the neighbors of a cell
def get_neighbors(cell, n, m, island):
    neighbors = []
    for i in range(cell[0] - 1, cell[0] + 2):
        for j in range(cell[1] - 1, cell[1] + 2):
            if 0 <= i <= n and 0 <= j <= m and (i, j) != cell and island[i - 1][j - 1] != "#":
                neighbors.append((i, j))
    return neighbors

