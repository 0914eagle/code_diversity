
def get_area(n, vertices):
    # Sort the vertices by their x-coordinate
    sorted_vertices = sorted(vertices, key=lambda x: x[0])

    # Get the unique x-coordinates of the vertices
    x_coords = list(set(v[0] for v in sorted_vertices))

    # Check if there are at least 2 unique x-coordinates
    if len(x_coords) < 2:
        return -1

    # Get the unique y-coordinates of the vertices
    y_coords = list(set(v[1] for v in sorted_vertices))

    # Check if there are at least 2 unique y-coordinates
    if len(y_coords) < 2:
        return -1

    # Calculate the area of the rectangle
    area = (x_coords[1] - x_coords[0]) * (y_coords[1] - y_coords[0])

    return area

