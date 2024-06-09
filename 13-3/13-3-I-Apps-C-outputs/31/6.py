
def get_minimum_panels(defective_cells):
    # Initialize a set to store the coordinates of the defective cells
    defective_cells_set = set(defective_cells)
    # Initialize a dictionary to store the number of panels required for each cell
    panels_required = {}
    # Iterate over the defective cells
    for cell in defective_cells:
        # Get the x, y, and z coordinates of the cell
        x, y, z = cell
        # Initialize a set to store the coordinates of the cells that are adjacent to the current cell
        adjacent_cells = set()
        # Check if the current cell is on the edge of the grid
        if x == 0 or x == 9 or y == 0 or y == 9 or z == 0 or z == 9:
            # If the current cell is on the edge of the grid, add it to the set of defective cells
            defective_cells_set.add(cell)
        else:
            # If the current cell is not on the edge of the grid, iterate over its adjacent cells
            for dx in range(-1, 2):
                for dy in range(-1, 2):
                    for dz in range(-1, 2):
                        # Check if the current cell is adjacent to the current adjacent cell
                        if (x+dx, y+dy, z+dz) in defective_cells_set:
                            # If the current cell is adjacent to the current adjacent cell, add it to the set of defective cells
                            defective_cells_set.add(cell)
                            # Add the current cell to the set of adjacent cells
                            adjacent_cells.add((x+dx, y+dy, z+dz))
            # Add the number of panels required for the current cell to the dictionary
            panels_required[cell] = 6
            # Iterate over the adjacent cells
            for adjacent_cell in adjacent_cells:
                # Check if the current cell is already in the set of defective cells
                if adjacent_cell in defective_cells_set:
                    # If the current cell is already in the set of defective cells, add the number of panels required for the current cell to the dictionary
                    panels_required[adjacent_cell] = panels_required.get(adjacent_cell, 0) + panels_required[cell]
    # Initialize a variable to store the minimum number of panels required
    minimum_panels = 0
    # Iterate over the cells in the grid
    for cell in [(x, y, z) for x in range(10) for y in range(10) for z in range(10)]:
        # Check if the current cell is in the set of defective cells
        if cell in defective_cells_set:
            # If the current cell is in the set of defective cells, add the number of panels required for the current cell to the minimum number of panels required
            minimum_panels += panels_required[cell]
    # Return the minimum number of panels required
    return minimum_panels

