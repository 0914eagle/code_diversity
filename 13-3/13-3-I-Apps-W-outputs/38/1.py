
def swimming_pool(n, vertices):
    # Sort the vertices by their x-coordinate
    sorted_vertices = sorted(vertices, key=lambda x: x[0])

    # Get the leftmost and rightmost vertices
    leftmost = sorted_vertices[0]
    rightmost = sorted_vertices[-1]

    # Get the topmost and bottommost vertices
    topmost = min(sorted_vertices, key=lambda x: x[1])
    bottommost = max(sorted_vertices, key=lambda x: x[1])

    # Calculate the width and height of the rectangle
    width = rightmost[0] - leftmost[0]
    height = topmost[1] - bottommost[1]

    # Calculate the area of the rectangle
    area = width * height

    # Check if the area is positive
    if area > 0:
        return area
    else:
        return -1

