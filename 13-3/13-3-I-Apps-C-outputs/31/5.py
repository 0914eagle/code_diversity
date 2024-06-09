
def get_minimum_panels(defective_cells):
    # Initialize a set to store the coordinates of the defective cells
    defective_cells_set = set(defective_cells)
    # Initialize a dictionary to store the number of panels required for each cell
    panels_required = {}
    # Iterate over the defective cells
    for cell in defective_cells:
        # Get the x, y, and z coordinates of the cell
        x, y, z = cell
        # Initialize a set to store the coordinates of the adjacent cells
        adjacent_cells = set()
        # Check if the cell is on the edge of the grid
        if x == 0 or x == 9 or y == 0 or y == 9 or z == 0 or z == 9:
            # If the cell is on the edge of the grid, add it to the set of adjacent cells
            adjacent_cells.add(cell)
        else:
            # If the cell is not on the edge of the grid, add the coordinates of the adjacent cells to the set
            adjacent_cells.add((x-1, y, z))
            adjacent_cells.add((x+1, y, z))
            adjacent_cells.add((x, y-1, z))
            adjacent_cells.add((x, y+1, z))
            adjacent_cells.add((x, y, z-1))
            adjacent_cells.add((x, y, z+1))
        # Iterate over the adjacent cells
        for adjacent_cell in adjacent_cells:
            # If the adjacent cell is not already in the set of defective cells, add it to the set
            if adjacent_cell not in defective_cells_set:
                defective_cells_set.add(adjacent_cell)
        # Add the number of panels required for the current cell to the dictionary
        panels_required[cell] = len(adjacent_cells)
    # Return the minimum number of panels required to contain all the defective cells
    return min(panels_required.values())

