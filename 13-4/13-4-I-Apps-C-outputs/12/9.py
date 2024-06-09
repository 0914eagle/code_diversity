
def count_polygons(R, C):
    # Initialize a list to store the number of polygons for each row
    num_polygons = [0] * R
    num_polygons[0] = 1
    
    # Loop through each row
    for i in range(1, R):
        # Initialize the number of polygons for the current row
        num_polygons[i] = 1
        
        # Loop through each column in the current row
        for j in range(1, C+1):
            # If the current cell is not the first or last cell in the row,
            # and the cell above it is not zero, then we can form a polygon
            if j != 1 and j != C and num_polygons[i-1][j-1] != 0:
                num_polygons[i][j] = num_polygons[i-1][j-1] + num_polygons[i-1][j+1]
            # If the current cell is the first cell in the row and the cell above it is not zero,
            # then we can form a polygon
            elif j == 1 and num_polygons[i-1][j] != 0:
                num_polygons[i][j] = num_polygons[i-1][j]
            # If the current cell is the last cell in the row and the cell above it is not zero,
            # then we can form a polygon
            elif j == C and num_polygons[i-1][j-1] != 0:
                num_polygons[i][j] = num_polygons[i-1][j-1]
    
    # Return the total number of polygons
    return sum(num_polygons)

