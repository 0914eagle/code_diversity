
def mad(grid, area_bounds, statisticians):
    # Initialize empty list to store densities
    densities = []
    
    # Loop through all possible rectangles
    for h in range(area_bounds[0], area_bounds[1] + 1):
        for w in range(area_bounds[0], area_bounds[1] + 1):
            # Calculate rectangle area
            area = h * w
            
            # Check if rectangle area is within bounds
            if area >= area_bounds[0] and area <= area_bounds[1]:
                # Initialize count of statisticians in rectangle
                count = 0
                
                # Loop through grid and count statisticians in rectangle
                for i in range(len(grid)):
                    for j in range(len(grid[0])):
                        if grid[i][j] == 1 and i >= h and j >= w:
                            count += 1
                
                # Calculate density and append to list
                density = count / area
                densities.append(density)
    
    # Calculate median of densities
    med = sum(densities) / len(densities)
    
    # Return median of densities
    return med

