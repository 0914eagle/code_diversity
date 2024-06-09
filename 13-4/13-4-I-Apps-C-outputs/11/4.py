
def mad(h, w, a, b, s):
    # Initialize an empty list to store the densities
    densities = []
    
    # Iterate over all possible rectangles
    for i in range(h):
        for j in range(w):
            # Calculate the area of the current rectangle
            area = (j + 1) * (i + 1)
            
            # Check if the area is within the given range
            if a <= area <= b:
                # Calculate the density of statisticians in the current rectangle
                density = sum(s[i][j:j+area]) / area
                
                # Add the density to the list of densities
                densities.append(density)
    
    # Return the median of the densities
    return median(densities)

