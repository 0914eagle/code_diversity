
def f1(n):
    # Calculate the area of the polygon
    area = n * (n - 3) / 2
    
    # Initialize the minimum weight to infinity
    min_weight = float('inf')
    
    # Iterate over all possible ways to cut the polygon into triangles
    for i in range(n):
        for j in range(i + 1, n):
            for k in range(j + 1, n):
                # Calculate the weight of the current triangle
                weight = i * j * k
                
                # Check if the current triangle has non-zero area
                if weight != 0:
                    # Calculate the area of the current triangle
                    triangle_area = (i + j + k) / 2
                    
                    # Check if the current triangle has non-zero area
                    if triangle_area != 0:
                        # Calculate the ratio of the current triangle to the total area
                        ratio = triangle_area / area
                        
                        # Check if the current triangle has the minimum weight
                        if ratio < min_weight:
                            min_weight = ratio
    
    # Return the minimum weight
    return min_weight

