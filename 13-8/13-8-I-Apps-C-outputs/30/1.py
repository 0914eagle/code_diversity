
def canyon_mapping(n, k, vertices):
    # Sort the vertices by their x-coordinate
    sorted_vertices = sorted(vertices, key=lambda x: x[0])

    # Find the minimum and maximum x-coordinates of the canyon
    min_x = sorted_vertices[0][0]
    max_x = sorted_vertices[-1][0]

    # Find the minimum and maximum y-coordinates of the canyon
    min_y = sorted_vertices[0][1]
    max_y = sorted_vertices[-1][1]

    # Calculate the width and height of the canyon
    width = max_x - min_x
    height = max_y - min_y

    # Calculate the side length of the square maps
    side_length = width / k

    return round(side_length, 2)

