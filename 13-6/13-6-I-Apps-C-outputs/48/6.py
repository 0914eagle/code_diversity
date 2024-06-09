
def find_celery(vertices, sightings):
    # Convert the vertices and sightings to numpy arrays for easier computation
    vertices = np.array(vertices)
    sightings = np.array(sightings)

    # Initialize the minimum polygon with all the vertices of Alexa Forest
    min_polygon = vertices

    # Loop through each sighting of Celery
    for sighting in sightings:
        # Find the polygon that contains the sighting and has the smallest number of vertices
        containing_polygon = find_containing_polygon(sighting, vertices)
        if len(containing_polygon) < len(min_polygon):
            min_polygon = containing_polygon

    return len(min_polygon)

def find_containing_polygon(sighting, vertices):
    # Find the polygon that contains the sighting and has the smallest number of vertices
    containing_polygon = []
    for vertex in vertices:
        if is_inside_polygon(sighting, vertex):
            containing_polygon.append(vertex)

    return containing_polygon

def is_inside_polygon(point, polygon):
    # Check if a point is inside a polygon
    # Using the ray casting algorithm
    x, y = point
    poly = np.array(polygon)
    n = len(polygon)
    inside = False
    p1x, p1y = poly[0]
    for i in range(n+1):
        p2x, p2y = poly[i % n]
        if y > min(p1y, p2y):
            if y <= max(p1y, p2y):
                if x <= max(p1x, p2x):
                    if p1y != p2y:
                        xints = (y-p1y)*(p2x-p1x)/(p2y-p1y)+p1x
                        if p1x == p2x or x <= xints:
                            inside = not inside
        p1x, p1y = p2x, p2y

    return inside

