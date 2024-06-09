
def count_polygons(r, c):
    # Initialize a list to store the polygons
    polygons = []
    
    # Loop through each row
    for i in range(r):
        # Loop through each column
        for j in range(c):
            # Check if the current cell is empty
            if i == 0 and j == 0:
                # If it is empty, add a polygon with only one cell
                polygons.append([(i, j)])
            else:
                # If it is not empty, check if it can be combined with any existing polygon
                for polygon in polygons:
                    # Check if the current cell is adjacent to any cell in the polygon
                    if (i, j) in polygon or (i-1, j) in polygon or (i+1, j) in polygon or (i, j-1) in polygon or (i, j+1) in polygon:
                        # If it is adjacent, add the current cell to the polygon
                        polygon.append((i, j))
                        break
                else:
                    # If it is not adjacent to any existing polygon, create a new polygon with the current cell
                    polygons.append([(i, j)])
    
    # Return the number of polygons
    return len(polygons)

