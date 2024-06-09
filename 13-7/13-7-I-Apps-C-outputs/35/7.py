
def get_closest_distance(contour_lines):
    # Initialize the closest distance to a large value
    closest_distance = 1000000
    # Iterate over each contour line
    for contour in contour_lines:
        # Get the coordinates of the contour line
        x_coords, y_coords = zip(*contour)
        # Calculate the slope of the contour line
        slope = (y_coords[-1] - y_coords[0]) / (x_coords[-1] - x_coords[0])
        # Calculate the y-intercept of the contour line
        y_intercept = y_coords[0] - slope * x_coords[0]
        # Calculate the distance from the contour line to the target point (0, 0)
        distance = abs(slope * 0 + y_intercept) / math.sqrt(slope ** 2 + 1)
        # Update the closest distance if the current distance is smaller
        closest_distance = min(closest_distance, distance)
    # Return the closest distance
    return closest_distance

