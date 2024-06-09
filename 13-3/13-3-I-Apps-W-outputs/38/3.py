
def get_area(n, vertices):
    # Sort the vertices by their x-coordinates
    sorted_vertices = sorted(vertices, key=lambda x: x[0])

    # Get the unique x-coordinates of the vertices
    x_coords = list(set(v[0] for v in sorted_vertices))

    # If there are less than 2 unique x-coordinates, it's not possible to determine the area
    if len(x_coords) < 2:
        return -1

    # Get the unique y-coordinates of the vertices
    y_coords = list(set(v[1] for v in sorted_vertices))

    # If there are less than 2 unique y-coordinates, it's not possible to determine the area
    if len(y_coords) < 2:
        return -1

    # Get the width and height of the rectangle
    width = x_coords[1] - x_coords[0]
    height = y_coords[1] - y_coords[0]

    # Calculate the area of the rectangle
    area = width * height

    return area

