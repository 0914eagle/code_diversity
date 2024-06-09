
def get_minimum_panels(defective_cells):
    # Initialize a set to store the coordinates of the defective cells
    defective_cells_set = set(defective_cells)
    # Initialize a dictionary to store the number of panels needed for each cell
    panels_needed = {}
    # Iterate over the defective cells
    for cell in defective_cells:
        # Get the x, y, and z coordinates of the cell
        x, y, z = cell
        # Initialize a set to store the coordinates of the adjacent cells
        adjacent_cells = set()
        # Iterate over the eight adjacent cells
        for dx in range(-1, 2):
            for dy in range(-1, 2):
                for dz in range(-1, 2):
                    # Skip the current cell
                    if dx == 0 and dy == 0 and dz == 0:
                        continue
                    # Get the coordinates of the adjacent cell
                    adjacent_cell = (x+dx, y+dy, z+dz)
                    # If the adjacent cell is not defective, add it to the set of adjacent cells
                    if adjacent_cell not in defective_cells_set:
                        adjacent_cells.add(adjacent_cell)
        # Add the number of panels needed for the current cell to the dictionary
        panels_needed[cell] = len(adjacent_cells)
    # Initialize a set to store the coordinates of the contained cells
    contained_cells = set()
    # Initialize a queue to store the cells to be processed
    queue = []
    # Add the first cell to the queue
    queue.append(defective_cells[0])
    # Loop until the queue is empty
    while queue:
        # Get the first cell from the queue
        cell = queue.pop(0)
        # If the cell is not contained, add it to the set of contained cells
        if cell not in contained_cells:
            contained_cells.add(cell)
            # Add the adjacent cells to the queue
            for adjacent_cell in adjacent_cells[cell]:
                queue.append(adjacent_cell)
    # Return the number of panels needed
    return sum(panels_needed.values())

