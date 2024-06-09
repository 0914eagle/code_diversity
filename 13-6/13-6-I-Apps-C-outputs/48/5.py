
def find_smallest_polygon(vertices, sightings):
    # Sort the vertices and sightings
    vertices.sort()
    sightings.sort()
    
    # Initialize the minimum polygon with all vertices
    min_polygon = vertices.copy()
    
    # Iterate through the sightings and check if they are inside the polygon
    for sighting in sightings:
        if sighting not in min_polygon:
            # If the sighting is not in the polygon, find the closest vertex and add it to the polygon
            closest_vertex = min(min_polygon, key=lambda vertex: abs(sighting - vertex))
            min_polygon.append(closest_vertex)
    
    # Return the smallest polygon with the minimum number of vertices
    return len(min_polygon)

