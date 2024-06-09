
def count_polygons(rows, cols):
    # Initialize a list to store the polygons
    polygons = []
    
    # Loop through each row
    for r in range(rows):
        # Loop through each column
        for c in range(cols):
            # Check if the current cell is empty
            if r == 0 and c == 0:
                # If it is empty, add a polygon to the list
                polygons.append([(r, c)])
            else:
                # If it is not empty, check if it can be added to any existing polygon
                for polygon in polygons:
                    # Check if the current cell is connected to any of the cells in the polygon
                    if (r, c) in polygon or (polygon[0][0], polygon[0][1]) == (r, c):
                        # If it is connected, add it to the polygon
                        polygon.append((r, c))
                        break
    
    # Return the number of polygons
    return len(polygons)

if __name__ == '__main__':
    rows, cols = map(int, input().split())
    print(count_polygons(rows, cols))

