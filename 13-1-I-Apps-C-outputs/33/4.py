
def solve(n, m, k, a):
    # Initialize variables
    changed_cells = 0
    rows, cols = n, m
    table = [[0] * cols for _ in range(rows)]

    # Fill the table with the given values
    for i in range(rows):
        for j in range(cols):
            table[i][j] = a[i][j]

    # Loop through each row
    for i in range(rows):
        # Loop through each column
        for j in range(cols):
            # If the current cell is not zero and is not part of a connected component, find the connected component and mark it as changed
            if table[i][j] != 0 and table[i][j] != 1:
                component = find_connected_component(table, i, j)
                changed_cells += len(component)
                for cell in component:
                    table[cell[0]][cell[1]] = 1

    # Check if the number of changed cells is less than or equal to k
    if changed_cells <= k:
        return changed_cells
    else:
        return -1

# Find the connected component of the same values starting from the given cell
def find_connected_component(table, i, j):
    component = []
    queue = [(i, j)]

    while queue:
        current_cell = queue.pop(0)
        component.append(current_cell)

        # Add the neighbors of the current cell to the queue if they are not zero and are not part of a connected component
        for neighbor in get_neighbors(table, current_cell[0], current_cell[1]):
            if table[neighbor[0]][neighbor[1]] != 0 and table[neighbor[0]][neighbor[1]] != 1:
                queue.append(neighbor)

    return component

# Get the neighbors of the given cell
def get_neighbors(table, i, j):
    neighbors = []

    # Top neighbor
    if i > 0:
        neighbors.append((i-1, j))

    # Bottom neighbor
    if i < len(table) - 1:
        neighbors.append((i+1, j))

    # Left neighbor
    if j > 0:
        neighbors.append((i, j-1))

    # Right neighbor
    if j < len(table[0]) - 1:
        neighbors.append((i, j+1))

    return neighbors

