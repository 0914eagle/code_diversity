
def find_closest_distance(contour_lines):
    # Initialize the closest distance to a large value
    closest_distance = 1000000
    
    # Iterate over each contour line
    for line in contour_lines:
        # Get the start and end points of the line
        start_point = line[0]
        end_point = line[1]
        
        # Calculate the distance between the start and end points
        distance = ((end_point[0] - start_point[0]) ** 2 + (end_point[1] - start_point[1]) ** 2) ** 0.5
        
        # If the distance is less than the current closest distance, update the closest distance
        if distance < closest_distance:
            closest_distance = distance
    
    # Return the closest distance
    return closest_distance

