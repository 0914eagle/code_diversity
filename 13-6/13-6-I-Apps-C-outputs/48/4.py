
def find_celery(vertices, sightings):
    # Sort the vertices and sightings
    vertices.sort()
    sightings.sort()
    
    # Initialize the minimum number of vertices as the total number of vertices
    min_vertices = len(vertices)
    
    # Iterate through all possible polygons
    for i in range(len(vertices)):
        # Create a polygon with the current vertex and the next K-1 vertices
        polygon = [vertices[i]] + vertices[i+1:i+K]
        
        # Check if all sightings are inside the polygon
        if all(is_inside_polygon(polygon, sighting) for sighting in sightings):
            # If all sightings are inside the polygon, update the minimum number of vertices
            min_vertices = min(min_vertices, len(polygon))
    
    return min_vertices

def is_inside_polygon(polygon, point):
    # Get the total angle between the point and the vertices of the polygon
    total_angle = 0
    for i in range(len(polygon)):
        vertex1 = polygon[i]
        vertex2 = polygon[(i+1) % len(polygon)]
        total_angle += get_angle(vertex1, vertex2, point)
    
    # If the total angle is 360 degrees, the point is inside the polygon
    return total_angle == 360

def get_angle(vertex1, vertex2, point):
    # Get the sides of the triangle
    a = get_distance(vertex1, point)
    b = get_distance(vertex2, point)
    c = get_distance(vertex1, vertex2)
    
    # Calculate the cosine of the angle
    angle = acos((b**2 + c**2 - a**2) / (2 * b * c))
    
    # Convert the angle to degrees
    return angle * 180 / math.pi

def get_distance(point1, point2):
    # Get the difference between the x and y coordinates
    diff_x = point1[0] - point2[0]
    diff_y = point1[1] - point2[1]
    
    # Calculate the Euclidean distance
    return (diff_x**2 + diff_y**2)**0.5

