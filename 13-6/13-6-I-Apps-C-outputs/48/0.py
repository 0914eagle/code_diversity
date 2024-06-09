
def find_smallest_polygon(vertices, sightings):
    # Sort the vertices of the polygon in counterclockwise order
    sorted_vertices = sorted(vertices, key=lambda x: x[0])

    # Create a list to store the vertices of the smallest polygon
    smallest_polygon = []

    # Iterate through the sightings of Celery
    for sighting in sightings:
        # Check if the sighting is inside the polygon
        if is_inside_polygon(sorted_vertices, sighting):
            # If the sighting is inside the polygon, add it to the smallest polygon
            smallest_polygon.append(sighting)

    # Return the number of vertices of the smallest polygon
    return len(smallest_polygon)

def is_inside_polygon(vertices, point):
    # Get the angle between the point and the first vertex of the polygon
    angle = get_angle(vertices[0], point, vertices[1])

    # Iterate through the vertices of the polygon
    for i in range(1, len(vertices)):
        # Get the angle between the point and the current vertex of the polygon
        current_angle = get_angle(vertices[i], point, vertices[i-1])

        # Check if the point is inside the polygon
        if current_angle >= angle:
            # If the point is inside the polygon, return True
            return True

    # If the point is not inside the polygon, return False
    return False

def get_angle(v1, v2, v3):
    # Get the dot product of the vectors v1-v2 and v1-v3
    dot_product = (v1[0]-v2[0]) * (v1[0]-v3[0]) + (v1[1]-v2[1]) * (v1[1]-v3[1])

    # Get the magnitude of the vectors v1-v2 and v1-v3
    mag_v1v2 = ((v1[0]-v2[0]) ** 2 + (v1[1]-v2[1]) ** 2) ** 0.5
    mag_v1v3 = ((v1[0]-v3[0]) ** 2 + (v1[1]-v3[1]) ** 2) ** 0.5

    # Calculate the angle between the vectors v1-v2 and v1-v3
    angle = acos(dot_product / (mag_v1v2 * mag_v1v3))

    # Return the angle in radians
    return angle

