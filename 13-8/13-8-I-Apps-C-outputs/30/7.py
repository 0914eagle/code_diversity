
def canyon_mapping(n, k, vertices):
    # Sort the vertices in clockwise order
    sorted_vertices = sorted(vertices, key=lambda x: x[0] * x[1])

    # Calculate the area of the polygon
    area = calculate_area(sorted_vertices)

    # Calculate the side length for each map
    side_length = area ** 0.5 / k

    return round(side_length, 2)

def calculate_area(vertices):
    area = 0
    for i in range(len(vertices)):
        v1 = vertices[i]
        v2 = vertices[(i + 1) % len(vertices)]
        area += v1[0] * v2[1] - v1[1] * v2[0]
    return abs(area / 2)

