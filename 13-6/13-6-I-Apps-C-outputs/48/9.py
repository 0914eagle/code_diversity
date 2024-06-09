
def find_smallest_polygon(vertices, sightings):
    # Sort the vertices and sightings
    vertices = sorted(vertices)
    sightings = sorted(sightings)
    
    # Initialize the smallest polygon with the whole Alexa Forest
    smallest_polygon = vertices
    
    # Iterate through each sighting and check if it is inside the current smallest polygon
    for sighting in sightings:
        # Check if the sighting is inside the current smallest polygon
        if not is_inside_polygon(smallest_polygon, sighting):
            # If the sighting is not inside the current smallest polygon, find the polygon that includes the sighting and is smallest
            smallest_polygon = find_smallest_polygon_including_sighting(vertices, sighting)
    
    # Return the smallest polygon with the required properties
    return smallest_polygon

def find_smallest_polygon_including_sighting(vertices, sighting):
    # Initialize the smallest polygon with the whole Alexa Forest
    smallest_polygon = vertices
    
    # Iterate through each vertex and check if it is inside the current smallest polygon
    for vertex in vertices:
        # Check if the vertex is inside the current smallest polygon
        if is_inside_polygon(smallest_polygon, vertex):
            # If the vertex is inside the current smallest polygon, check if the sighting is also inside the polygon
            if is_inside_polygon(smallest_polygon, sighting):
                # If the sighting is also inside the polygon, update the smallest polygon with the current vertex and the sighting
                smallest_polygon = [vertex, sighting]
    
    # Return the smallest polygon with the required properties
    return smallest_polygon

def is_inside_polygon(polygon, point):
    # Initialize the number of intersections to 0
    intersections = 0
    
    # Iterate through each edge of the polygon
    for i in range(len(polygon) - 1):
        # Check if the point is inside the edge
        if is_inside_edge(polygon[i], polygon[i + 1], point):
            # If the point is inside the edge, increment the number of intersections
            intersections += 1
    
    # Check if the point is inside the final edge
    if is_inside_edge(polygon[-1], polygon[0], point):
        # If the point is inside the final edge, increment the number of intersections
        intersections += 1
    
    # Return True if the point is inside the polygon and False otherwise
    return intersections % 2 == 1

def is_inside_edge(vertex1, vertex2, point):
    # Calculate the slope of the edge
    slope = (vertex2[1] - vertex1[1]) / (vertex2[0] - vertex1[0])
    
    # Calculate the y-intercept of the edge
    y_intercept = vertex1[1] - slope * vertex1[0]
    
    # Calculate the y-coordinate of the point on the edge
    edge_y = slope * point[0] + y_intercept
    
    # Return True if the point is inside the edge and False otherwise
    return point[1] < edge_y

