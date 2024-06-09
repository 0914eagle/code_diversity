
def swimming_pool_area(n, vertices):
    # Sort the vertices by their x-coordinate
    sorted_vertices = sorted(vertices, key=lambda x: x[0])

    # Find the leftmost and rightmost vertices
    leftmost = sorted_vertices[0]
    rightmost = sorted_vertices[-1]

    # Find the topmost and bottommost vertices
    topmost = min(sorted_vertices, key=lambda x: x[1])
    bottommost = max(sorted_vertices, key=lambda x: x[1])

    # Calculate the area of the rectangle
    area = (rightmost[0] - leftmost[0]) * (topmost[1] - bottommost[1])

    # Check if the area is positive
    if area > 0:
        return area
    else:
        return -1

