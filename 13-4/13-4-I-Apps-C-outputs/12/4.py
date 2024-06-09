
def count_polygons(r, c):
    # Initialize a list to store the number of polygons for each row
    num_polygons = [0] * r
    num_polygons[0] = 1
    
    # Iterate over the rows
    for i in range(1, r):
        # Initialize the number of polygons for the current row
        num_polygons[i] = 1
        
        # Iterate over the previous rows
        for j in range(i):
            # Calculate the number of polygons that can be formed by combining the current row with the previous row
            num_polygons[i] += num_polygons[j] * (c - j)
    
    # Return the total number of polygons
    return sum(num_polygons)

