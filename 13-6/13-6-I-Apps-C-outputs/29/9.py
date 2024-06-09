
def find_mad(grid_height, grid_width, area_range, grid):
    # Initialize a list to store the densities
    densities = []
    
    # Iterate over each possible rectangle
    for i in range(grid_height):
        for j in range(grid_width):
            # Calculate the area of the current rectangle
            area = (j + 1) * (i + 1)
            
            # Check if the area is within the given range
            if area_range[0] <= area <= area_range[1]:
                # Calculate the density of statisticians in the current rectangle
                density = sum(grid[i][j:j+area]) / area
                
                # Add the density to the list of densities
                densities.append(density)
    
    # Return the median of the densities
    return median(densities)

