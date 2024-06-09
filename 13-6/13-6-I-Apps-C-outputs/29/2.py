
def mad(h, w, a, b, square_map):
    # Initialize an empty list to store the densities
    densities = []
    
    # Loop through each possible rectangle
    for i in range(h):
        for j in range(w):
            # Calculate the area of the current rectangle
            area = (j + 1) * (i + 1)
            
            # Check if the area is within the given range
            if a <= area <= b:
                # Calculate the density of statisticians in the current rectangle
                density = sum(square_map[i][j:j+area]) / area
                
                # Add the density to the list of densities
                densities.append(density)
    
    # Return the median of the densities
    return median(densities)

