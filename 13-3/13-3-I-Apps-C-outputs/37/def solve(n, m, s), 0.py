
def solve(n, m, s):
    # Initialize variables
    witch_cells = set()
    treasure_cell = (n, m)
    visited = set()
    queue = [(1, 1)]

    # Loop through the cells
    while queue:
        current_cell = queue.pop(0)
        visited.add(current_cell)

        # If the current cell is the treasure cell, return the number of witch cells
        if current_cell == treasure_cell:
            return len(witch_cells)

        # If the current cell is not passable, add it to the witch cells
        if s[current_cell[0] - 1][current_cell[1] - 1] == "#":
            witch_cells.add(current_cell)

        # Add the neighboring cells to the queue
        for neighbor in get_neighbors(current_cell, n, m):
            if neighbor not in visited and neighbor not in queue:
                queue.append(neighbor)

    # If the treasure cell is not reachable, return -1
    return -1

def get_neighbors(cell, n, m):
    neighbors = []
    if cell[0] < n:
        neighbors.append((cell[0] + 1, cell[1]))
    if cell[1] < m:
        neighbors.append((cell[0], cell[1] + 1))
    return neighbors

