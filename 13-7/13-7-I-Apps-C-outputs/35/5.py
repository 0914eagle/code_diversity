
def get_closest_distance(contour_lines):
    # Initialize the closest distance to a large value
    closest_distance = 1000000
    
    # Iterate over each contour line
    for contour in contour_lines:
        # Get the height of the contour line
        height = contour[0]
        
        # Get the number of vertices in the contour line
        num_vertices = contour[1]
        
        # Iterate over each vertex in the contour line
        for i in range(2, num_vertices * 2, 2):
            # Get the x and y coordinates of the vertex
            x = contour[i]
            y = contour[i + 1]
            
            # Calculate the distance from the vertex to the target
            distance = (x - 0) ** 2 + (y - 0) ** 2
            
            # If the distance is less than the closest distance, update the closest distance
            if distance < closest_distance:
                closest_distance = distance
    
    # Return the closest distance
    return closest_distance

