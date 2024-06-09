
def count_polygons(rows, cols):
    # Initialize a list to store the polygons
    polygons = []
    
    # Loop through each row
    for i in range(rows):
        # Loop through each column
        for j in range(cols):
            # Check if the current cell is empty
            if i == 0 and j == 0:
                # If it is empty, add a polygon to the list
                polygons.append([(i, j)])
            else:
                # If it is not empty, check if it can be connected to any existing polygon
                for polygon in polygons:
                    # Check if the current cell is connected to any of the existing polygons
                    if (i, j) in polygon or (i-1, j) in polygon or (i, j-1) in polygon:
                        # If it is connected, add it to the polygon
                        polygon.append((i, j))
                        break
                else:
                    # If it is not connected to any existing polygon, create a new polygon
                    polygons.append([(i, j)])
    
    # Return the number of polygons
    return len(polygons)

