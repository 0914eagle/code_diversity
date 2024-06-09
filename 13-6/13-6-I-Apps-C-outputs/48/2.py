
def find_celery(vertices, sightings):
    # Sort the vertices and sightings
    vertices = sorted(vertices)
    sightings = sorted(sightings)
    
    # Initialize the minimum polygon with all vertices
    min_polygon = vertices
    
    # Iterate through the sightings
    for sighting in sightings:
        # Check if the sighting is inside the minimum polygon
        if sighting in min_polygon:
            # If the sighting is already in the minimum polygon, continue
            continue
        # If the sighting is not in the minimum polygon, find the closest vertex to the sighting
        closest_vertex = find_closest_vertex(min_polygon, sighting)
        # Add the sighting and the closest vertex to the minimum polygon
        min_polygon.append(sighting)
        min_polygon.append(closest_vertex)
        # Sort the minimum polygon
        min_polygon = sorted(min_polygon)
    
    # Return the number of vertices in the minimum polygon
    return len(min_polygon)

def find_closest_vertex(vertices, point):
    # Initialize the closest vertex as the first vertex
    closest_vertex = vertices[0]
    # Initialize the minimum distance as the distance between the point and the first vertex
    min_distance = distance(point, closest_vertex)
    
    # Iterate through the vertices
    for vertex in vertices:
        # Calculate the distance between the point and the current vertex
        distance = distance(point, vertex)
        # If the distance is less than the minimum distance, update the closest vertex and the minimum distance
        if distance < min_distance:
            closest_vertex = vertex
            min_distance = distance
    
    # Return the closest vertex
    return closest_vertex

def distance(point1, point2):
    # Calculate the distance between the two points
    return ((point1[0] - point2[0]) ** 2 + (point1[1] - point2[1]) ** 2) ** 0.5

