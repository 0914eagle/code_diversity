
def get_minimum_panels(defective_cells):
    # Initialize a set to store the coordinates of the defective cells
    defective_cells_set = set(defective_cells)
    # Initialize a dictionary to store the number of panels needed for each cell
    panels_needed = {}
    # Iterate over the defective cells
    for cell in defective_cells:
        # Get the x, y, and z coordinates of the cell
        x, y, z = cell
        # Initialize the number of panels needed for this cell to 0
        panels_needed[cell] = 0
        # Iterate over the six faces of the cell
        for face in [(x, y, z), (x, y+1, z), (x, y, z+1), (x, y+1, z+1), (x+1, y, z), (x+1, y+1, z)]:
            # If the face is not a defective cell, increment the number of panels needed for this cell
            if face not in defective_cells_set:
                panels_needed[cell] += 1
    # Initialize the minimum number of panels needed to contain all the defective cells to 0
    minimum_panels = 0
    # Iterate over the defective cells
    for cell in defective_cells:
        # Add the number of panels needed for this cell to the minimum number of panels needed
        minimum_panels += panels_needed[cell]
    # Return the minimum number of panels needed to contain all the defective cells
    return minimum_panels

