
def solve(n, vertices):
    # Sort the vertices by their x-coordinate
    sorted_vertices = sorted(vertices, key=lambda x: x[0])

    # Get the leftmost and rightmost vertices
    leftmost = sorted_vertices[0]
    rightmost = sorted_vertices[-1]

    # Get the topmost and bottommost vertices
    topmost = min(sorted_vertices, key=lambda x: x[1])
    bottommost = max(sorted_vertices, key=lambda x: x[1])

    # Calculate the area of the initial rectangle
    area = (rightmost[0] - leftmost[0]) * (topmost[1] - bottommost[1])

    # If the area is positive, return it
    if area > 0:
        return area
    # Otherwise, return -1
    else:
        return -1

