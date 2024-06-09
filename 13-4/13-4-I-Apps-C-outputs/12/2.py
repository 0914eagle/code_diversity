
def count_polygons(r, c):
    # Initialize a list to store the polygons
    polygons = []

    # Loop through each row
    for i in range(r):
        # Loop through each column
        for j in range(c):
            # Check if the current cell is empty
            if i == 0 and j == 0:
                # If it is empty, add a polygon to the list
                polygons.append([(i, j)])
            else:
                # If it is not empty, check if it can be added to any existing polygon
                for polygon in polygons:
                    # Check if the current cell is on the border of the polygon
                    if (i, j) in polygon or (i, j-1) in polygon or (i-1, j) in polygon:
                        # If it is on the border, add it to the polygon
                        polygon.append((i, j))
                        break
                else:
                    # If it is not on the border of any existing polygon, create a new polygon with it as the first cell
                    polygons.append([(i, j)])

    # Return the number of polygons
    return len(polygons)

