
def get_minimum_panels(defective_cells):
    # Initialize a set to store the coordinates of the defective cells
    defective_set = set(defective_cells)
    # Initialize a dictionary to store the number of panels needed for each cell
    panel_count = {}
    # Loop through each cell in the grid
    for i in range(10):
        for j in range(10):
            for k in range(10):
                # If the cell is defective, add it to the set and initialize the panel count to 0
                if (i, j, k) in defective_set:
                    panel_count[(i, j, k)] = 0
                # If the cell is not defective, check if it is on the edge of the grid or not
                else:
                    if i == 0 or j == 0 or k == 0 or i == 9 or j == 9 or k == 9:
                        # If the cell is on the edge of the grid, initialize the panel count to 2
                        panel_count[(i, j, k)] = 2
                    else:
                        # If the cell is not on the edge of the grid, initialize the panel count to 3
                        panel_count[(i, j, k)] = 3
    # Loop through each cell in the grid and update the panel count based on the number of defective cells in the surrounding 26 cells
    for i in range(1, 9):
        for j in range(1, 9):
            for k in range(1, 9):
                # If the cell is not defective, check if any of the surrounding 26 cells are defective
                if (i, j, k) not in defective_set:
                    surrounding_defective_cells = 0
                    for di in range(-1, 2):
                        for dj in range(-1, 2):
                            for dk in range(-1, 2):
                                if (i+di, j+dj, k+dk) in defective_set:
                                    surrounding_defective_cells += 1
                    # If there are any defective cells in the surrounding 26 cells, update the panel count for the current cell
                    if surrounding_defective_cells > 0:
                        panel_count[(i, j, k)] += surrounding_defective_cells
    # Return the minimum panel count across all cells
    return min(panel_count.values())

