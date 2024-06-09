
def count_polygons(r, c):
    # Initialize a list to store the number of polygons for each row
    num_polygons = [0] * r
    num_polygons[0] = 1
    
    # Iterate through each row
    for i in range(1, r):
        # Initialize the number of polygons for the current row
        num_polygons[i] = 1
        
        # Iterate through each column in the current row
        for j in range(i):
            # Add the number of polygons from the previous row to the current row
            num_polygons[i] += num_polygons[i-1]
    
    # Return the total number of polygons
    return sum(num_polygons)

