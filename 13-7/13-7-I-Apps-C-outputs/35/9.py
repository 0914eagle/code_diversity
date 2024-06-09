
import math

def get_closest_distance(contour_lines):
    # Initialize the closest distance to a large value
    closest_distance = 1000000
    # Iterate over each contour line
    for contour in contour_lines:
        # Get the inner and outer heights of the contour
        inner_height, outer_height = contour[0], contour[1]
        # Get the number of vertices in the contour
        num_vertices = contour[2]
        # Iterate over each vertex in the contour
        for i in range(num_vertices):
            # Get the x and y coordinates of the vertex
            x, y = contour[3 + 2*i], contour[4 + 2*i]
            # Calculate the distance from the vertex to the target
            distance = math.sqrt(x**2 + y**2)
            # If the distance is less than the closest distance, update the closest distance
            if distance < closest_distance:
                closest_distance = distance
    # Return the closest distance
    return closest_distance

