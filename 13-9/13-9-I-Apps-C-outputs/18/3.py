
def largest_corn_area(vertices, canal_points):
    
    # Sort the vertices in counterclockwise order
    vertices = sorted(vertices, key=lambda x: x[0])

    # Find the indices of the vertices on either side of the canal
    left_vertices = []
    right_vertices = []
    for i in range(len(vertices)):
        if vertices[i][0] < canal_points[0][0]:
            left_vertices.append(vertices[i])
        else:
            right_vertices.append(vertices[i])

    # Find the area of the polygon on either side of the canal
    left_area = polygon_area(left_vertices)
    right_area = polygon_area(right_vertices)

    # Return the larger of the two areas
    return max(left_area, right_area)

def polygon_area(vertices):
    
    area = 0
    for i in range(len(vertices)):
        x1, y1 = vertices[i]
        x2, y2 = vertices[(i + 1) % len(vertices)]
        area += (x1 * y2 - x2 * y1)
    return abs(area / 2)

