
def count_polygons(rows, cols):
    # Initialize a list to store the polygons
    polygons = []
    
    # Loop through each row
    for i in range(rows):
        # Loop through each column
        for j in range(cols):
            # Check if the current cell is empty
            if j < cols - 1 and i < rows - 1:
                # Check if the current cell and the cell to the right and below are empty
                if j < cols - 2 and i < rows - 2:
                    # Check if the current cell, the cell to the right, and the cell below are empty
                    if j < cols - 3 and i < rows - 3:
                        # Check if the current cell, the cell to the right, and the cell below are empty
                        if j < cols - 4 and i < rows - 4:
                            # Add the polygon to the list
                            polygons.append((i, j))
    
    # Return the number of polygons
    return len(polygons)

