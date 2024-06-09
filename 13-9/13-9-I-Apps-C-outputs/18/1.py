
def get_largest_corn_area(vertices, canal_points):
    # Convert the vertices to a list of tuples
    vertices = [(x, y) for x, y in vertices]
    # Convert the canal points to a list of tuples
    canal_points = [(x, y) for x, y in canal_points]
    # Initialize the largest area
    largest_area = 0
    # Iterate over each vertex
    for vertex in vertices:
        # Find the distance between the vertex and the canal
        distance = get_distance(vertex, canal_points)
        # If the distance is positive, it means the vertex is on the same side of the canal as the canal points
        if distance > 0:
            # Find the area of the polygon using the Shoelace formula
            area = get_area(vertices)
            # If the area is larger than the largest area, update the largest area
            if area > largest_area:
                largest_area = area
    # Return the largest area
    return largest_area

def get_distance(point, points):
    # Initialize the minimum distance
    min_distance = float('inf')
    # Iterate over each point
    for p in points:
        # Calculate the distance between the point and the current point
        distance = get_distance_between_points(point, p)
        # If the distance is smaller than the minimum distance, update the minimum distance
        if distance < min_distance:
            min_distance = distance
    # Return the minimum distance
    return min_distance

def get_distance_between_points(point1, point2):
    # Calculate the distance between the two points
    distance = ((point1[0] - point2[0]) ** 2 + (point1[1] - point2[1]) ** 2) ** 0.5
    # Return the distance
    return distance

def get_area(vertices):
    # Initialize the area
    area = 0
    # Iterate over the vertices
    for i in range(len(vertices)):
        # Calculate the area of the triangle using the Shoelace formula
        area += vertices[i][0] * vertices[i-1][1] - vertices[i-1][0] * vertices[i][1]
    # Return the absolute value of the area
    return abs(area / 2)

