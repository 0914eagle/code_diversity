
def get_minimum_panels(defective_cells):
    # Initialize a set to store the coordinates of the defective cells
    defective_cells_set = set(defective_cells)
    # Initialize a dictionary to store the number of panels required for each cell
    panels_required = {}
    # Iterate over the defective cells
    for cell in defective_cells:
        # Get the x, y, and z coordinates of the cell
        x, y, z = cell
        # Initialize the number of panels required for the current cell to 0
        panels_required[cell] = 0
        # Check if the cell is on the edge of the grid
        if x == 0 or x == 9 or y == 0 or y == 9 or z == 0 or z == 9:
            # If the cell is on the edge of the grid, it requires 3 panels to be contained
            panels_required[cell] += 3
        else:
            # If the cell is not on the edge of the grid, it requires 2 panels to be contained
            panels_required[cell] += 2
        # Check if the cell has any defective neighbors
        for neighbor in [(x-1, y, z), (x+1, y, z), (x, y-1, z), (x, y+1, z), (x, y, z-1), (x, y, z+1)]:
            if neighbor in defective_cells_set:
                # If the cell has a defective neighbor, it requires an additional panel to be contained
                panels_required[cell] += 1
    # Return the minimum number of panels required to contain all the defective cells
    return min(panels_required.values())

