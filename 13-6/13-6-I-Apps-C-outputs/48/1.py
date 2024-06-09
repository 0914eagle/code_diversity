
def find_smallest_polygon(sightings, vertices):
    # Sort the sightings by their x-coordinate
    sightings.sort(key=lambda x: x[0])

    # Initialize the smallest polygon with the first sighting
    smallest_polygon = [sightings[0]]

    # Iterate through the remaining sightings
    for sighting in sightings[1:]:
        # If the current sighting is not on the border of the smallest polygon, add it to the polygon
        if is_inside_polygon(smallest_polygon, sighting):
            smallest_polygon.append(sighting)

    # Return the smallest polygon
    return smallest_polygon

def is_inside_polygon(polygon, point):
    # Get the angle between the line from the point to the next vertex and the line from the point to the previous vertex
    angle = get_angle(polygon, point)

    # If the angle is less than 180 degrees, the point is inside the polygon
    if angle < 180:
        return True
    else:
        return False

def get_angle(polygon, point):
    # Get the vector from the point to the next vertex
    vector_1 = (polygon[1][0] - point[0], polygon[1][1] - point[1])

    # Get the vector from the point to the previous vertex
    vector_2 = (polygon[0][0] - point[0], polygon[0][1] - point[1])

    # Calculate the dot product of the two vectors
    dot_product = vector_1[0] * vector_2[0] + vector_1[1] * vector_2[1]

    # Calculate the magnitude of the two vectors
    magnitude_1 = (vector_1[0] ** 2 + vector_1[1] ** 2) ** 0.5
    magnitude_2 = (vector_2[0] ** 2 + vector_2[1] ** 2) ** 0.5

    # Calculate the cosine of the angle between the two vectors
    cosine = dot_product / (magnitude_1 * magnitude_2)

    # Calculate the angle in degrees
    angle = math.degrees(math.acos(cosine))

    # Return the angle
    return angle

